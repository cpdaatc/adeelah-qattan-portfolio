# Canonical portfolio asset repair — execution prompt

Work only in `cpdaatc/adeelah-qattan-portfolio`. Do not use Replit. Diagnose before changing production and do not claim success without fresh verification.

## User-visible failures to fix
1. Hero portrait is severely pixelated on mobile.
2. Royal Honour certificate renders only at the top and then becomes a large gray block.
3. Downloadable CV PDF shows a gray portrait placeholder.

## Root-cause evidence already established
- Current `assets/Dr_Adeelah_Qattan_Portrait_Original.jpg` is only ~7.5 KB and is not the full-quality source.
- Repository contains `assets/portrait.jpg` at ~147 KB, previously restored as the approved full-quality portrait.
- Current `assets/King_Fahd_Medal_Third_Degree_2019.jpg` is only ~7.1 KB and is visibly truncated/corrupt.
- Current CV PDF is a stale generated artifact containing a placeholder.

## Required implementation
- Create new immutable asset names to defeat browser/CDN cache.
- Reuse the verified full-quality portrait binary already in repository history; never upscale the 7.5 KB broken derivative.
- Restore the certificate only from a complete verified source. Never reconstruct a JPEG by concatenating incomplete Base64 chunks. If no complete source exists in Git history, fail closed rather than publishing a fake/partial certificate.
- Update every HTML reference, download link, preload/social reference, and generated-document source to the new canonical asset names.
- Regenerate the CV PDF with the real portrait embedded into the document (not a gray placeholder and not a fragile remote relative URL).
- Remove obsolete temporary reconstruction workflows/chunks from the final production diff.

## Acceptance gates
- JPEG decode succeeds through EOF; dimensions are plausible and file size is not a tiny broken derivative.
- Portrait displayed on mobile is the full-quality source and download returns the same canonical portrait.
- Certificate decodes fully and displays the complete document with no gray truncation.
- CV PDF opens and contains the actual portrait, not a placeholder.
- Search repository for old broken asset references and ensure none remain in production HTML.
- Verify the deployed GitHub Pages URL, not only repository files.
- Merge to `main` only after all gates pass; otherwise report the exact blocker.