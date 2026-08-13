# Executive Healthcare Portfolio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a bilingual, responsive and print-ready executive healthcare portfolio for Dr. Adeelah Talat Qattan using the verified CV content, the teal visual identity of the latest source file, and the original supplied portrait.

**Architecture:** A dependency-light static single-page site in `index.html`. The original portrait is embedded as a data URI so the GitHub Pages build has no fragile image-path dependency. English is the default; Arabic is applied client-side with RTL direction. Interactions are native JavaScript and print output uses dedicated A4 CSS.

**Tech Stack:** Semantic HTML5, CSS3, vanilla JavaScript, Google Fonts with system fallbacks, GitHub Pages-compatible static hosting.

## Global Constraints

- Preserve the supplied portrait; do not redraw or generate the person.
- Keep the visual identity teal/white with restrained gold reserved for Royal Honour emphasis.
- Treat `ROYAL HONOUR · 2019 — King Fahd Medal — Third Degree` as the primary recognition moment.
- Current roles must remain active: Assistant Hospital Director for Academic Affairs; Director, Medical Education & Training; Consultant, Restorative Dentistry.
- Do not publish third-party reference phone numbers or emails on the public portfolio.
- Include responsive navigation, bilingual EN/AR switching, motion with `prefers-reduced-motion`, activity tabs, mobile menu, scroll progress, and Print / Save PDF controls.
- Print mode must be A4-friendly and hide interactive navigation controls.

---

### Task 1: Executive visual system and first viewport

**Files:**
- Create: `index.html`

**Interfaces:**
- Produces: Teal/gold design tokens, executive hero, supplied portrait, current roles, navigation controls.

- [x] Build the hero around the supplied portrait and three current roles.
- [x] Apply the latest CV teal identity and restrained gold accent.
- [x] Add responsive desktop/mobile navigation.
- [x] Verify no horizontal overflow at desktop and mobile widths.

### Task 2: Royal Honour signature section

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: Global color/motion tokens.
- Produces: Primary Royal Honour section and direct navigation anchor `#royal`.

- [x] Create a dedicated full-width Royal Honour band immediately after the hero.
- [x] Emphasize `ROYAL HONOUR · 2019`, `King Fahd Medal`, and `Third Degree` without inventing an official medal image.
- [x] Add restrained halo motion and print-safe styling.

### Task 3: Curated executive content

**Files:**
- Modify: `index.html`

**Interfaces:**
- Produces: Profile, leadership impact, career, credentials, governance, activities, honours, references, contact.

- [x] Reconcile overlapping career records and keep only verified/current titles active.
- [x] Replace unverified committee-count claims with separated Chair / Standing / Strategic Initiative groups.
- [x] Preserve key qualifications, accreditation work, LMS, Saudi Board, pathways and scholarship planning.
- [x] Keep reference identities while withholding third-party personal contact details on the public page.

### Task 4: Interactions, bilingual mode and print

**Files:**
- Modify: `index.html`

**Interfaces:**
- Produces: `setLang()`, mobile menu, tabs, activity expansion, count-up, reveal observers, scroll spy, print styles.

- [x] Add English/Arabic switching with RTL layout.
- [x] Add mobile menu and active section navigation.
- [x] Add activity tabs and expandable full activity list.
- [x] Add scroll reveal, count-up, progress line and reduced-motion handling.
- [x] Add `window.print()` buttons and A4 print CSS.

### Task 5: Verification and repository handoff

**Files:**
- Create: `.nojekyll`
- Modify: `README.md`

**Interfaces:**
- Produces: GitHub Pages-ready repository contents.

- [x] Validate HTML structure and embedded portrait dimensions.
- [x] Exercise language toggle, tabs, expansion and mobile menu in Chromium.
- [x] Verify desktop/mobile horizontal overflow is false.
- [x] Verify print media hides navigation and has no horizontal overflow.
- [ ] Enable GitHub Pages in repository settings when Pages API access is available to the connected tool.
