# Anti-Slop Checklist — VoiceForm

Tailored from [[anti-slop]] to this project. Run through this before recording the final demo and before writing the README.

## Visual
- [ ] No purple-to-indigo gradients, no glowing blobs — palette is off-white/saffron/indigo/green per [[design-system]], nothing else
- [ ] No glassmorphism cards — solid surfaces, one consistent radius/elevation
- [ ] No generic Inter-only hierarchy — Noto Sans Devanagari + Inter/Noto Sans pairing, used consistently
- [ ] No "Revolutionizing X with AI" hero + feature cards — opens directly on the mic button / the task
- [ ] No emoji as icons or headers — one icon (mic) is likely sufficient
- [ ] No fake stats — the ONLY numbers shown are the real Qualcomm AI Hub benchmark figures
- [ ] No stock dashboard or decorative charts — there is no dashboard in this app, by design
- [ ] No dark-mode neon — light, calm, high-contrast, matches a government-form-adjacent tone
- [ ] No decorative 3D or particle backgrounds
- [ ] Every screen's padding/density matches actual task density (one field/action at a time, not padded-out empty space)
- [ ] On-screen Hindi text is real Devanagari script, not English captions describing it (checked against [[design-system]]'s specific warning)

## Code
- [ ] No giant single files or over-abstracted layers — small modules, plain functions (`ponytail-review` passed)
- [ ] No dead code, unused dependencies, or commented-out blocks before submission
- [ ] No hardcoded API keys; env vars used; any mocked/sample data clearly labeled as such in code and README
- [ ] Every external call (ASR, LLM, AI Hub API) has visible error and loading states — a low-literacy user never sees a raw stack trace
- [ ] README states plainly what's real vs. simulated (per [[verdict]] Decision #13) — no emoji walls, no vague feature-list-only README
- [ ] Steady commits show progress, not one giant end-of-project commit
- [ ] You (the solo builder) can explain every module in plain language — if not, simplify or delete it (explain-back pass from [[claude-playbook]])

## Copy
- [ ] No slop words: leverage, seamless, cutting-edge, revolutionize, empower, unlock, harness, robust, game-changer, next-generation, "in today's fast-paced world", delve
- [ ] Every claim names the user, the task, and a number where possible — e.g. "fills a real NSP scholarship form field-by-field via voice" beats "empowers users with seamless AI-driven form assistance"
- [ ] "146M farmers" / market-size-style framing avoided — this pitch is about one named user and one named form, not a TAM slide

## Pitch
- [ ] No trillion-dollar market-size slide — the pitch names the specific user (a low-literacy NSP applicant) and the specific channel (CSC/NGO distribution), not a vague addressable market
- [ ] "AI-powered" is never the whole value proposition — the value prop is "fills a real form by voice, with mistakes correctable by voice, entirely on-device"
- [ ] No architecture slide full of logos — one mermaid diagram showing the actual hard part (ASR → GBNF-constrained LLM → confirm/correct loop), with the live-demo-vs-cloud-benchmark distinction clearly labeled
- [ ] Demo does NOT open on a login/settings screen — opens directly on the human problem, per [[pitch-plan]]
- [ ] Proof included: the real AI Hub benchmark table — not a vague "it's fast" claim
- [ ] The demo video tells a story with a person in it, not a slide-reading voiceover

## Proof of real engineering (pick at least two — this project should hit at least these three)
- [x] A measured evaluation: real Qualcomm AI Hub latency/tokens-per-sec benchmark, NPU vs CPU, named device
- [x] A non-trivial integration: GBNF-constrained structured output from a local GGUF LLM via GenieX, tied to a real government form's schema
- [x] A working edge case judges can see live in the video: the deliberate ASR-error-then-correction moment in the demo script
- [ ] (Optional, if time allows) A clear statement of limitations and next steps in the README — Hindi-only, single-form, no training, stated plainly rather than hidden

## Tools that help (from [[toolkit]])
- `pbakaus/impeccable` → `npx impeccable detect` for automated AI-UI tell flags
- `DietrichGebert/ponytail` → `/ponytail-review` to keep code minimal and reviewable
