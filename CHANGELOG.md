# Changelog — Mr Wolf (webapp 40 of 59)

## [2.4.0] - 2026-11-06
### Changed
- Removed the duplicate title, tagline, generic explainer and case disclaimer; the shared Cedwyn header supplies the page title.
- Replaced hard-coded per-lead markup with an A2UI v0.9 template repeated over the backend rows.
- Added a validated build that treats leaderboard.json as the source database and publishes /_db/view.json, /_db/leaderboard.json and /_ui/index.surface.a2ui.json.
- The initial data view shows each lead's score, weakest-gate progress and four individual limb values; explanations, next actions and source records expand within each card.
- The procedural route and scoring qualifications are rendered from the same backend dataset.
- Build checks unique row IDs, score arithmetic, limb bounds and weakest-limb progress; no legal score or conclusion changed.


## [2.3.0] - 2026-11-06
### Changed
- Load the shared Cedwyn header and theme from the canonical site origin so the standalone PR preview receives the same navigation and day/night controls as the other webapps.
- Set Mr Wolf page identity explicitly for the shared header (webapp 40 of 59).
- Align typography, card surfaces, borders and signature colours with the shared Barlow / Cedwyn day-night design system.
- Preserve the v2.2.0 nested progressive-disclosure interface and the v2.1.0 legal scoring unchanged.


## [2.2.0] - 2026-11-05
### Changed
- Replaced long, always-visible lead details with compact score cards and progressive disclosure.
- Added nested accordions for lead context, each proof gate, next actions and linked records.
- Added nested disclosure for the CPR 52.30 route, scoring method and authorities.
- Added native keyboard-accessible controls, animated expansion where supported, and reduced-motion support; no JavaScript dependency.
- No changes to legal scoring, lead scores or procedural status.


## [2.1.0] - 2026-11-05
### Corrected
- Restricted the 200-point lead score to the four elements of a freestanding Takhar fraud action.
- Removed CPR 52.30 process-integrity requirements from individual lead scores; CPR 52.30 remains a separate case-wide route gateway.
- Split conscious dishonesty from attribution/actual court deception, and scored operative cause/materiality separately.
- Recalibrated the licence-rejection lead's materiality element to 40/50: the judgment supports conditional materiality, but no rejection document has been found.
- Retained four non-compensatory internal minima and weakest-limb progress. No lead reaches the floor; route remains unresolved and filing blocked.

## [2.0.0] - 2026-11-05
### Changed
- Introduced non-compensatory legal/evidential gates and a separate CPR 52.30 route review.
- Removed reasonable diligence from the Takhar limbs and tracked it separately.

## [1.0.0] - 2026-11-01
### Added
- Mr Wolf leaderboard with 15 leads, first-generation scoring and supporting record links.
