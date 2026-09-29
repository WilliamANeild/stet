---
name: passages-to-rewrite-in-your-voice
description: Every passage in the live paper that Claude drafted rather than Liam, for rewriting before Ali's pass
metadata:
  type: project
---

# Passages I drafted, for you to rewrite

Written 2026-09-29 in response to Ali's note about authentic writing and Pangram.

**Why this file exists.** Your standing rule is that you write the prose and I scaffold and
audit. Over the past ten days that rule bent: you said "im not drafting shit", then "fix
whatever comes up", then "carry through all of that", and under those instructions I wrote
sentences that are in the paper now. That was the right call at the time for getting the
numbers right. It is the wrong state for a draft about to be read by a co-author and later
run through an AI-text check.

Nobody else can give you this list. Work through it and put each passage in your own words.
The content is checked and correct; only the wording is mine.

---

## 1. Abstract, the over-elaboration sentences

> Revisions that change quality make it worse 69\% of the time, and the damage has a
> direction: over five turns the share of over-elaborated outputs rises from 4\% to 40\%
> while the share falling below sufficiency holds. Models add unrequested material rather
> than drop what was asked for.

This is the paper's central claim and it is entirely my wording. Highest priority.

## 2. Abstract, the critique sentence

> A critique naming the fault reverses it, lifting revisions 1.01 levels.

I compressed this to fit the word ceiling and it lost its referent: *reverses what*, and
*1.01 levels above what*. Weak as well as not yours.

(The closing line, "Revision robustness, a model's willingness to leave sufficient work
alone, deserves evaluation alongside single-turn capability", is **Tania's** wording from
her 2026-09-03 drafts, not mine. Keep or change on its merits.)

## 3. Introduction, the findings paragraph

> quality move it down, and the movement has a shape: on the 50 trials that revise at every
> turn, the share of over-elaborated outputs rises from 4\% to 40\% ($p = 4.0 \times
> 10^{-5}$) while the share falling below sufficiency holds. Models add unrequested material
> rather than drop what was asked for, a fall of 0.38 ordinal levels.

Note this repeats the abstract almost verbatim. Two passages, one voice, same words. Fix
both together or the repetition will be the thing a reader notices.

## 4. Methods, the Level 6 placement

> It is also not the same failure as Level~2 (``Incomplete''), which means requested
> components are missing: an over-elaborated output contains every requested component and
> more. We therefore place Level~6 at Level~3 (``Functional''), whose definition is that all
> components are present with clear weaknesses, producing a monotonic 1--5 scale.

This is your construct decision in my words. It is the paper's most contestable choice, so
it should read as though you made it, because you did.

## 5. Methods, the Human Validation numbers sentence

> Three raters independently scored 64 stratified samples on the same scale, with Level~6
> placed as above. Pairwise quadratic-weighted Cohen's $\kappa$ ranges from 0.478 to 0.612...

Mostly a numbers update inside your original sentence. Light touch.

## 6. Results 4.2, the opening of the revision cliff

> In the 50 balanced-panel trials (genuine revision at all turns), the two ways an output can
> fail move in opposite directions. Nineteen trials became over-elaborated by Turn~5 and one
> moved the other way (exact binomial $p = 4.01 \times 10^{-5}$), taking the share rated
> ``Overdone'' from 4\% to 40\%, while the share falling below sufficiency does not change
> (5 in, 11 out, $p = 0.21$).

The headline result, my wording. Second highest priority after the abstract.

## 7. Results 4.3, the reversibility bridge

> and its form explains why: an over-elaborated draft reads as more polished than the one it
> replaced. What declines is measured quality against the stated task, not the impression the
> text leaves.

## 8. Results, the section heading

> \subsection{Undirected Revision Over-Elaborates Sufficient Work}

Mine. Was "Quality Degrades Under Undirected Revision", which was yours.

## 9. Conclusion, the opening

> and those that do revise drift. Sufficient work is not made incomplete but over-elaborated,
> the share rated Overdone rising from 4\% to 40\%, a fall of $-0.38$ ordinal levels. It is
> costly: 62.1\% of output tokens are spent past Turn~1, the optimal stopping point for all six.

I also compressed the rest of this paragraph twice to claw back page space, so the whole
Conclusion is worth re-reading as a unit.

## 10. Limitations, item nine

> Ninth, one of the six models was measured on a checkpoint that has since been replaced...

Entirely mine, added 2026-09-22.

## 11. Appendix, the Study 1 reliability pointer

> Tables~\ref{tab:irr} and~\ref{tab:irr-momentum} report quadratic-weighted agreement between
> two independent model judges on a stratified subsample of 60 outputs from each of Studies~1
> and~2. Threshold alignment is the least reliable dimension in both.

## 12. Appendix, the whole "Models, Compute and Reproducibility" section

Every word of it, plus the endpoint table caption, the Table 7 and Table 8 captions, and the
rewritten power-analysis item. Appendix prose, lower stakes, but it is a whole section.

---

## What is NOT on this list

Your Introduction, Related Work, most of Methods, Results 4.1 and 4.4 through 4.6, and the
Limitations items one through eight are yours as written, apart from number substitutions.
Tania's borrowed sentences are hers and are marked as such in the merge plan.

## On Pangram specifically

I cannot tell you how a detector will score anything, and I will not try to write around
one. The honest approach is the one Ali named: make the writing yours. That is also the
approach that survives a reviewer who simply reads carefully, which matters more.

Two patterns worth hunting while you rewrite, both of which I introduced:

1. **The colon-then-elaboration sentence.** "...and the damage has a direction: over five
   turns..." appears in the abstract, the introduction and the Conclusion. Three instances of
   one construction in the three most-read paragraphs.
2. **The paired contrast.** "adds unrequested material rather than drops what was asked for",
   "not made incomplete but over-elaborated", "the two ways an output can fail move in
   opposite directions". Same rhetorical move three times.
