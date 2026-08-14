# Portfolio Canonical Repair Design

## Goal
Produce one stable, production-ready version of Dr. Adeelah Talat Qattan's portfolio that matches the user's approved requirements and cannot regress to earlier assets or UI states.

## Canonical assets
- Hero display portrait: exact user-provided portrait, web-optimized only for rendering; no face alteration, no generated replacement.
- Downloadable personal photo: the original user-provided 1254x1254 photo without any portfolio frame.
- Royal honour: full King Fahd Medal certificate, portrait orientation, shown in full with no crop, no click-to-open and no download control.
- CV: audited 2026 PDF containing current appointments, committee roles, both emails, and conference leadership 2023-2026.
- Speaker bio: one-page bilingual PDF using the approved Arabic 3-4 line bio and an equivalent English version.
- Social preview: 1200x630 JPG using the same approved portrait and executive portfolio branding.

## UI contract
- Hero: only one primary action, Royal Honour. Print/Save CV is not shown in the hero.
- Mobile side panel: solid opaque background, compact typography and compact action buttons.
- Side actions: Royal Honour, Download Personal Photo, Download Speaker Bio (PDF), Download CV (PDF), and Print / Save CV.
- Buttons use one teal treatment, approximately 40-44 px minimum height, compact text, clear icon/emoji, and no oversized Cormorant styling.
- English and Arabic labels are functionally equivalent; only the selected language is visible.
- Royal certificate remains display-only.

## Content contract
The portfolio must preserve and expose:
- Assistant Hospital Director for Academic Affairs & Training.
- Director, Medical Education & Training Department.
- Consultant, Restorative Dentistry.
- Current committee roles already supplied by the user.
- Both emails: atqattan@hotmail.com and adeelahqattan@gmail.com.
- Conference leadership 2023-2026, each with Conference Committee Chair / رئيسة لجنة المؤتمر and the approved theme/slogan.
- Quality/research content already accepted in the portfolio.

## Regression prevention
- Remove all obsolete one-off workflows that rewrite index.html or visual assets.
- Keep a single deterministic validation/deployment path.
- Asset integrity is checked by SHA-256, file signature, dimensions, and non-zero size before committing.
- HTML checks verify required bilingual labels, current content, side-action count, and display-only royal certificate.

## Acceptance tests
1. Required canonical files exist and match expected SHA-256 hashes.
2. Hero portrait source resolves to the canonical display portrait.
3. Personal-photo download resolves to the separate original no-frame image.
4. Royal certificate is full portrait orientation and is not wrapped in a link or download action.
5. Side-panel actions remain compact and bilingual.
6. Conference 2023-2026 content and both emails are present.
7. CV and speaker bio download targets are the updated files.
8. Open Graph/Twitter preview points to the corrected 1200x630 preview asset.
9. GitHub Pages builds successfully from the final commit.
10. Final mobile QA is performed against the public GitHub Pages URL before the version is accepted.
