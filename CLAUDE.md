# VoiceForm

## What this is
An on-device voice assistant that fills the NSP Post-Matric Scholarship form for a low-literacy Hindi speaker, with a spoken confirm-and-correct loop. Built for the Snapdragon® AI Lab Build & Present Challenge (Qualcomm, 2026). Spec: docs/idea-spec.md. Design: docs/design-system.md. Plan: docs/build-plan.md. Pitch: docs/pitch-plan.md. Anti-slop: docs/anti-slop-checklist.md.

## Stack
- ASR: Whisper-tiny/Distil-Whisper via Qualcomm AI Hub (ONNX export), profiled on Qualcomm AI Hub's cloud-hosted Snapdragon X device
- Slot-filling LLM: Llama-3.2-1B/3B or Phi-3.5-mini (GGUF) via GenieX, GBNF-constrained to the NSP JSON schema
- Frontend: Python (Streamlit or Flask + plain HTML/JS) — no heavy framework, per design-system.md's flat/static decision
- Fonts: Noto Sans Devanagari + Inter, bundled locally for offline demo

## Rules
- Build only what the current milestone in docs/build-plan.md needs. No auth, no dashboards, no multi-language, no "SDK" layer — see the cut line in docs/build-plan.md.
- Use design tokens from docs/design-system.md exactly (colors, type, spacing). Never introduce new colors or fonts.
- Real data or clearly labeled sample data only. The Qualcomm AI Hub benchmark numbers must come from an actual profiling job — never fabricate or estimate them.
- Keep the live-app-demo path and the AI-Hub-cloud-benchmark path visibly separate in code comments and UI — never blur "ran on my machine" with "ran on Snapdragon NPU."
- Prefer small files and plain functions over abstractions. Run `/ponytail-review` on every diff before considering a milestone done.
- Every external call (ASR, LLM, AI Hub API) has an error and loading state — a low-literacy user should never see a raw stack trace.
- The person building this is a beginner who vibe-codes: explain what you're doing in plain terms as you go, and flag anything generated that they should understand before moving on.
- Before declaring a milestone done, check it against docs/anti-slop-checklist.md.

## Commands
dev: `streamlit run app/main.py` (adjust once framework is picked) · test: manual walkthrough of docs/pitch-plan.md demo script · lint: n/a unless added · deploy: local only, no hosting needed for submission

## Not yet done (fill in as build progresses)
- [ ] Qualcomm AI Hub account created, first cloud device profiling benchmark obtained
- [ ] Live NSP Post-Matric Scholarship form field list pulled, JSON schema locked
- [ ] ASR pipeline working end-to-end locally
- [ ] GenieX + GBNF slot-filling working
- [ ] Confirm-and-correct loop implemented
- [ ] impeccable + ponytail review passes done
- [ ] Backup demo video recorded
- [ ] README finalized (real vs. simulated stated explicitly)
