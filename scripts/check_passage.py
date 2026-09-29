#!/usr/bin/env python3
"""
Score a candidate passage against Liam's own writing and against the project's voice rules.

Used while replacing passages Claude drafted with Liam's own prose, so the check is the
same every time instead of a judgment call that drifts. The baseline is measured from the
paper's existing prose with the known-Claude sentences excluded, so "matches the baseline"
means "reads like the rest of the paper", not "reads like anything in particular".

    python3 scripts/check_passage.py "candidate text here"
    python3 scripts/check_passage.py --file draft.txt
    python3 scripts/check_passage.py --baseline        recompute and print the baseline

Input:  the paper's live sections, for the baseline
Output: stdout only
"""
import argparse
import pathlib
import re
import statistics as st
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "paper" / "sections"
LIVE = ["abstract_v2", "introduction_v2", "related_work_v2", "methods",
        "results_v2", "conclusion", "limitations"]

# Sentences Claude drafted, excluded from the baseline so it reflects Liam's voice only.
# Keep in step with .workspace/notes/passages_to_rewrite_in_your_voice.md.
CLAUDE_MARKERS = [
    "the damage has a direction", "Models add unrequested material", "the movement has a shape",
    "It is also not the same failure", "the two ways an output can fail", "Nineteen trials became",
    "its form explains why", "those that do revise drift", "Sufficient work is not made incomplete",
    "Ninth, one of the six models", "We therefore place Level", "reads as more polished",
]

# From rules/writing-voice-core.md. Terms of art that survive are not listed.
BANNED = [
    "key ", "tracks ", "track ", "specific", "broader", "rests on", "rest on", "load-bearing",
    "dominant", "different", "actual", "actually", "pipeline", "headline", "in other words",
    "reassuringly", "scoped", "surface", "spine", "plumbing", "gate", "gating", "horserace",
    "playbook", "gloss", "lock in", "locked", "dial in", "dialed", "standing up", "stood up",
    "crucial", "significantly", "it is important to note",
]
HEDGES = ["may", "might", "could", "perhaps", "possibly", "suggests", "appears", "seems", "likely"]


def sentences(text):
    t = re.sub(r"(?<!\\)%.*", "", text)
    t = re.sub(r"\\(cite|citet|citep)[a-z]*\*?\{[^}]*\}", "CITE", t)
    t = re.sub(r"\$[^$]*\$", "MATH", t)
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?", " ", t)
    t = re.sub(r"[{}\\~]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return [s.strip() for s in re.split(r"(?<=[.!?]) ", t) if len(s.split()) >= 5]


def profile(ss):
    if not ss:
        return None
    lengths = [len(s.split()) for s in ss]
    return {
        "n": len(ss),
        "mean": st.mean(lengths),
        "sd": st.pstdev(lengths) if len(lengths) > 1 else 0.0,
        "longest": max(lengths),
        "commas": st.mean(s.count(",") for s in ss),
        "colon": sum(1 for s in ss if ":" in s) / len(ss),
        "semicolon": sum(1 for s in ss if ";" in s) / len(ss),
        "rather_than": sum(1 for s in ss if " rather than " in s) / len(ss),
    }


def baseline():
    ss = []
    for name in LIVE:
        p = SECTIONS / f"{name}.tex"
        if not p.exists():
            raise SystemExit(f"missing section: {p}")
        for s in sentences(p.read_text()):
            if not any(m in s for m in CLAUDE_MARKERS):
                ss.append(s)
    return profile(ss)


def flag(label, got, want, tol, unit="", pct=False):
    fmt = (lambda v: f"{v:.0%}") if pct else (lambda v: f"{v:.2f}{unit}")
    off = abs(got - want) > tol
    mark = "  <-- off" if off else ""
    print(f"    {label:<26} {fmt(got):>7}   baseline {fmt(want):>7}{mark}")
    return off


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("text", nargs="?")
    ap.add_argument("--file")
    ap.add_argument("--baseline", action="store_true")
    a = ap.parse_args()

    base = baseline()
    if a.baseline:
        print(f"  Liam's baseline over {base['n']} sentences:")
        for k, v in base.items():
            if k != "n":
                print(f"    {k:<14} {v:.2f}")
        return 0

    raw = pathlib.Path(a.file).read_text() if a.file else a.text
    if not raw:
        raise SystemExit("give a passage as an argument or with --file")
    ss = sentences(raw)
    if not ss:
        raise SystemExit("no sentences of five words or more found")
    p = profile(ss)

    print(f"\n  {p['n']} sentence(s), {sum(len(s.split()) for s in ss)} words\n")
    print("  STYLE, against the paper's own prose")
    off = 0
    off += flag("mean sentence length", p["mean"], base["mean"], 4.0, "w")
    off += flag("longest sentence", p["longest"], base["mean"] + 2 * base["sd"], 12.0, "w")
    off += flag("commas per sentence", p["commas"], base["commas"], 0.45)
    off += flag("share with a colon", p["colon"], base["colon"], 0.25, pct=True)
    off += flag("share with 'rather than'", p["rather_than"], base["rather_than"], 0.20, pct=True)

    print("\n  VOICE")
    low = raw.lower()
    hits = sorted({b.strip() for b in BANNED if re.search(r"\b" + re.escape(b.strip()) + r"\b", low)})
    print(f"    banned words           {hits if hits else 'none'}")
    if "—" in raw or "–" in raw:
        print("    em or en dash          PRESENT, rule is zero in prose")
        off += 1
    tail = [s.rstrip(".").split()[-1].lower() for s in ss]
    preps = {"of", "to", "in", "for", "with", "on", "at", "from", "by", "about", "into", "over"}
    ending = [w for w in tail if w in preps]
    print(f"    sentence-final preps   {ending if ending else 'none'}")
    hedge = [h for h in HEDGES if re.search(r"\b" + h + r"\b", low)]
    print(f"    hedges                 {hedge if hedge else 'none'}"
          + ("   (rule: one per claim, not three)" if len(hedge) > 2 else ""))
    off += len(hits) + len(ending)

    print(f"\n  {'LOOKS CONSISTENT WITH YOUR PROSE' if off == 0 else str(off) + ' item(s) to look at'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
