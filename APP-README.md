# Mr Wolf — webapp 40 of 59

Canonical source: `unclehowell/cedwyn-mr-wolf` (split-repo mode, 5 November 2026). The legacy `section/mr-wolf` branch in `unclehowell/cedwyn` is a compatibility mirror used by the consolidated Cedwyn build.

## Legal-readiness model v2.1.0

This is an internal evidence-readiness index for a possible freestanding fraud action under *Takhar v Gracefield Developments Ltd* [2019] UKSC 13. It is not a court-prescribed points test, legal advice, probability estimate or finding of any court.

Four non-compensatory elements, each 0–50:
1. Conscious and deliberate dishonesty.
2. Attribution to the successful party (or a person for whom it is responsible) and actual deception of the court.
3. Operative cause and materiality: the fraud was an operative cause and would have changed how the original court approached the evidence.
4. Admissible proof, provenance and particulars.

The internal floor requires at least 25/50 on **each** element. Raw total alone cannot pass a lead. Progress is the weakest limb divided by 25, capped at 100%; raw score remains a separate evidence index out of 200.

200/200 is the owner's double-lock target (50/50 on every element, twice the internal floor). It is not literally 200% statistical probability and cannot guarantee a judicial outcome.

CPR 52.30 is a distinct case-wide route, not part of the individual *Takhar* score. Its real-injustice, exceptional-circumstances and no-alternative-effective-remedy conditions remain unresolved; the app marks filing blocked pending independent advice. Reasonable diligence is not scored as a general element of a freestanding *Takhar* action, although abuse-of-process and other procedural issues remain separately relevant.

## Review and release

The existing consolidated Cedwyn Pages project is used for previews because Cloudflare's Pages-project quota prevents creating another connected project. For this review, the full-site v2.1.0 snapshot is staged at `staging/mr-wolf-v2.1.0-preview` in `unclehowell/cedwyn` and served at [the Cloudflare preview] (https://staging-mr-wolf-v2-1-0-previ.cedwyn-274.pages.dev/mr-wolf/). It is not production. The staging snapshot is separate from this PR and needs refreshing after changes to the PR.

On merge to `main`, Cedwyn's split-repository synchronisation copies the app to legacy `section/mr-wolf`; the consolidated site's section pin/build remains a separate release step. Do not edit the old mirror branch directly.
