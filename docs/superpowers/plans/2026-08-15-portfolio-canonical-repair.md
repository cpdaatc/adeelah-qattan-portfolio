# Portfolio Canonical Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace stale/broken portfolio assets and unstable UI state with one validated canonical release that satisfies the approved portrait, certificate, downloads, bilingual content, CV, bio, conferences, emails, and social-preview requirements.

**Architecture:** Stage exact binary assets as temporary base64 text files, decode them in one deterministic GitHub Action, patch `index.html` through one focused Python script, run integrity/content/UI assertions, remove obsolete mutation workflows and staging files, then commit the canonical result to `main`. GitHub Pages is accepted only after the public build completes and mobile output is checked.

**Tech Stack:** Static HTML/CSS/JS, GitHub Pages, GitHub Actions, Python 3 standard library, SHA-256/file signature validation.

## Global Constraints
- Do not generate, repaint, or alter Dr. Adeelah's face.
- Downloaded personal photo must be the original no-frame image.
- King Fahd Medal certificate must be complete, uncropped, display-only, and non-downloadable.
- Hero must not show Print / Save CV; printing remains in the side menu.
- Side actions must be compact, visually consistent, bilingual, and mobile-readable.
- Preserve both emails and the approved 2023-2026 conference leadership record.
- Do not claim publication or award wins beyond supplied evidence.
- Do not accept the release until the public GitHub Pages build is successful and mobile QA passes.

---

### Task 1: Stage canonical binary assets

**Files:**
- Create: `.canonical-release/portrait-display.b64`
- Create: `.canonical-release/personal-photo-original.b64`
- Create: `.canonical-release/king-fahd-certificate-full.b64`
- Create: `.canonical-release/cv-2026-final.b64`
- Create: `.canonical-release/speaker-bio-final.b64`
- Create: `.canonical-release/share-preview-final.b64`

**Interfaces:**
- Consumes: verified local files supplied/created in the current project.
- Produces: exact base64 payloads decoded by Task 3.

- [ ] Stage each asset as plain base64 with no line wrapping.
- [ ] Record expected SHA-256 values in the finalization script.
- [ ] Verify every base64 payload decodes locally before triggering GitHub Actions.

### Task 2: Write canonical repair tests first

**Files:**
- Modify: `scripts/canonical_finalize.py`

**Interfaces:**
- Consumes: decoded asset paths and current `index.html`.
- Produces: deterministic assertions that fail on stale images, wrong button wiring, language mismatch, missing conference data, wrong emails, or clickable certificate.

- [ ] Add failing assertions for canonical SHA-256 hashes and dimensions.
- [ ] Add assertions that hero uses display portrait while photo download uses separate original image.
- [ ] Add assertions for compact side buttons, opaque mobile panel, and exactly five side actions.
- [ ] Add assertions for Arabic/English labels, both emails, and 2023-2026 conference data.
- [ ] Add assertions that the royal certificate is display-only and full portrait orientation.
- [ ] Add assertions that OG/Twitter preview uses the canonical share-preview asset.

### Task 3: Decode exact assets and patch the portfolio

**Files:**
- Modify: `.github/workflows/canonical-finalize.yml`
- Modify: `index.html`
- Create/replace: `assets/portrait-display.jpg`
- Create/replace: `assets/Dr_Adeelah_Qattan_Personal_Photo_Original_No_Frame.jpg`
- Create/replace: `assets/King_Fahd_Medal_Certificate_Full_2019.jpg`
- Create/replace: `assets/Dr_Adeelah_Qattan_CV_2026.pdf`
- Create/replace: `assets/Dr_Adeelah_Qattan_Speaker_Bio_Bilingual.pdf`
- Create/replace: `assets/share-preview.jpg`

**Interfaces:**
- Consumes: `.canonical-release/*.b64` and `scripts/canonical_finalize.py`.
- Produces: stable static site assets and HTML.

- [ ] Decode all staged base64 payloads.
- [ ] Validate JPEG/PDF signatures, SHA-256, dimensions, and file sizes before modifying HTML.
- [ ] Patch hero portrait and side download targets.
- [ ] Replace Royal Honour section with a full certificate figure using `object-fit: contain` and no anchor/download behavior.
- [ ] Apply compact mobile menu typography and 40-44px action controls with a solid white panel background.
- [ ] Preserve bilingual content and conference/email data.
- [ ] Update OG/Twitter image URL with a release cache-busting version.
- [ ] Run the canonical audit and stop on any failure.

### Task 4: Remove regression sources

**Files:**
- Delete: obsolete one-off workflows under `.github/workflows/`.
- Delete: obsolete staging directories `.tmp`, `.canonical-upload`, `.canonical-release` after successful decoding.
- Delete: temporary repair scripts after the canonical commit.

**Interfaces:**
- Consumes: successful Task 3 validation.
- Produces: a repository with no background workflow capable of restoring stale assets.

- [ ] Remove all old mutation workflows except the normal Pages deployment mechanism, if present.
- [ ] Remove temporary staging payloads and repair-only scripts.
- [ ] Confirm no remaining workflow contains stale portrait/certificate paths.

### Task 5: Verify release and public mobile output

**Files:**
- No source changes unless verification exposes a defect.

**Interfaces:**
- Consumes: final canonical commit.
- Produces: GO/NO-GO release verdict.

- [ ] Verify final repository asset hashes and `index.html` references.
- [ ] Verify GitHub Pages build is `built`/successful for the final commit.
- [ ] Open the public URL with a cache-busting query and inspect mobile layout.
- [ ] Verify portrait renders correctly, certificate is complete, buttons are compact, selected-language content is isolated, and downloads point to the correct files.
- [ ] If any item fails, mark NO-GO and repair before issuing the final link.
