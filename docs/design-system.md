# Design System — VoiceForm

## Mood
Professional, calm, civic — not cinematic, not corporate-SaaS, not techy-dark-mode. This is a government-form-adjacent tool for a low-literacy user; every council advisor independently converged here (see [[verdict]] Decision #10). Judges are engineers grading on Technical Implementation first — flashy UI reads as compensating for weak substance.

## 2D/3D/motion decision
- 2D only. No 3D, no particle backgrounds, no decorative animation.
- Motion budget: a single pulsing mic icon while listening, and a field highlight/checkmark animation when a field is confirmed. Nothing else moves.
- Static-first layout: one dominant screen, one primary action at a time (listen → transcribe → confirm → next field).

## Color palette (hex tokens)
| Token | Light | Use |
|---|---|---|
| `--bg` | `#FAF7F2` | Background — warm off-white/cream, not clinical white or dark |
| `--text` | `#1C1C1C` | Primary text — near-black for max contrast/legibility |
| `--accent-active` | `#FF9933` | Saffron/amber — "listening" / active-mic state |
| `--accent-confirmed` | `#2E7D32` | Green — field confirmed / task complete |
| `--secondary` | `#1B2A4A` | Indigo — headings, secondary UI chrome, non-active elements |
| `--error` | `#C62828` | Red — used sparingly, only for a rejected/low-confidence field awaiting correction |

Dark mode: not a priority for this build (single demo screen, controlled recording environment) — if time allows, invert `--bg`/`--text` only; do not reintroduce accent colors that reduce contrast for the target user.

Rationale: saffron/indigo/off-white reads as Indian-civic without leaning into try-hard tricolor patriotism; avoids the generic purple-gradient/dark-mode-neon SaaS look every advisor flagged as slop for this audience.

## Typography
- **Devanagari text** (form labels, transcribed Hindi, confirmations): **Noto Sans Devanagari** — must render correctly; tofu boxes (☐☐☐) on a judge's machine is an instant credibility loss (Outsider advisor's specific warning).
- **Latin/UI chrome** (buttons, README-adjacent in-app text): **Inter** or **Noto Sans** — pair with Noto Sans Devanagari for consistent weight/x-height.
- Body text: 24px minimum — literacy/readability constraint, not aesthetic choice (Expansionist advisor).
- Type scale: 2 sizes only — one for form field labels/values, one larger for the current spoken prompt/status text. No decorative headline scale needed for a single-screen tool.

## Spacing and radius
- Generous touch targets: the mic button should be the single largest element on screen (minimum 120px diameter equivalent), thumb/tap-friendly even though this is likely demoed on a laptop.
- Radius: soft but not bubbly — 8-12px on cards/buttons, consistent throughout. Avoid the "everything is a rounded pill" AI-slop default and avoid sharp government-form starkness.
- One field visible at a time, or a short vertical list with the active field visually distinct (border or background tint using `--accent-active` at low opacity) — task density should stay low; this is not a dashboard.

## Visual references (3-5, with links)
1. AudioNova (analog contest 1st place) — for the "one clear before/after moment" demo structure: https://devpost.com/software/audionova
2. India Stack / DigiLocker mobile UI patterns — for a credible "real government service" visual register (large text, minimal chrome, official-feeling but not sterile)
3. Google's Noto Sans Devanagari specimen — for correct Devanagari rendering reference: Google Fonts
4. NSP (National Scholarship Portal) itself — the actual form being replaced; screenshotting its real field layout grounds the JSON schema and gives the demo an authentic "this is the real thing" anchor
5. Any WhatsApp/Google Assistant voice-input affordance (large mic button, waveform-on-listen) — familiar, non-templated pattern for "press and speak" that a low-literacy user likely already recognizes

## What the UI must never look like
- No purple-to-indigo gradient hero, no glassmorphism cards, no glowing blobs
- No chatbot-bubble conversation UI — this is a form, not a chat product; a bubble UI is the fastest way to look like every other team's default (Outsider advisor's specific warning)
- No dashboard with fake/decorative metrics or charts
- No emoji as icons or section headers — one real icon set if icons are needed at all (a single mic icon is likely sufficient)
- No dark-mode "techy" aesthetic — wrong tone for a government-form-adjacent, low-literacy-facing tool
- No English captions substituting for real Devanagari script — if the target user speaks Hindi, the on-screen text must actually be in Hindi, not an English gloss (Outsider advisor's specific warning against looking templated)
