# Idea Spec — VoiceForm

## One-line pitch
VoiceForm lets a low-literacy Hindi speaker fill the National Scholarship Portal (NSP) Post-Matric Scholarship form by talking — speech recognition and field extraction run on a Snapdragon NPU, and a spoken confirm-and-correct loop fixes mistakes without reading.

## Problem, with evidence
Every year, first-generation Indian students lose scholarship renewals to portal form errors — wrong IFSC digits, mismatched income figures, fields left blank because the applicant (or the parent filling it for them) can't read the form confidently in English or dense bureaucratic Hindi. This isn't a hypothetical: it's the exact failure mode the closest analog contest's 1st-place winner (AudioNova) solved for a different modality (voice restoration for speech-impaired users) — same principle: a task people can't do by reading/typing, solved by speaking. [[problem-space]] and [[past-winners]] both ground this pattern.

## Target user
A low-literacy or low-confidence-reading Hindi speaker applying for the NSP Post-Matric Scholarship — could be the student, a parent, or a Common Service Centre (CSC) operator filling it on their behalf. Real "buyer" for pitch purposes: state welfare departments, NGOs (e.g. Pratham-style education orgs), or the CSC network — not a direct consumer download. See [[verdict]] Decision #3.

## The one "wow" moment
The applicant speaks their details in Hindi ("मेरा नाम राम है, मेरी सालाना आय पचास हज़ार रुपये है...") — the form fields fill live on screen. One field gets misheard. The system reads it back, the applicant says "नहीं, बदलो" (no, change it), corrects just that field by voice, and the form completes — entirely offline, on-device, no typing at any point.

## Core features (max 3)
1. **Voice-to-form fill**: Whisper-class ASR (via Qualcomm AI Hub) transcribes Hindi speech; a small quantized on-device LLM (Llama-3.2-1B/3B or Phi-3.5-mini via GenieX) maps the transcript into the NSP form's JSON schema (name, DOB, annual income, caste category, bank IFSC, etc.), grammar-constrained (GBNF) so it always produces valid JSON.
2. **Confirm-and-correct loop**: each filled field is read back; low-confidence or explicitly-rejected fields trigger a same-language spoken re-prompt and re-fill without restarting the whole form.
3. **NPU benchmark proof**: a visible before/after latency/tokens-per-sec table from a real Qualcomm AI Hub cloud-device profiling job (named Snapdragon device) vs. CPU baseline — the non-negotiable Technical Implementation proof.

## Explicit non-goals
- No multi-language support (Hindi only — see [[verdict]] cut line)
- No multi-form support (NSP Post-Matric Scholarship only, hardcoded schema)
- No "reusable SDK" build (mentioned once in README as future work, never built)
- No user accounts, history, dashboard, or analytics
- No TTS voice replies beyond simple confirmation prompts (text/visual confirmation is an acceptable fallback if TTS integration runs short on time)
- No custom model training or fine-tuning — pre-built, pre-quantized Qualcomm AI Hub models only

## Why this beats the saturated ideas
Public entries already visible for this exact challenge are on-device security/deepfake detection (SnapShield) and an offline farmer assistant (Kisan Sahayak AI) — both already claimed, both requiring heavier ML pipelines than a beginner can safely ship solo in 15-40 hours. VoiceForm instead targets the one theme proven to win in the closest real analog contest (AudioNova, 1st place, accessibility/assistive voice tech) that remains completely unclaimed in this challenge's visible entries. See [[competitor-landscape]].

## Feasibility and viability notes
- All models are pre-built and pre-quantized (Whisper via AI Hub, small LLM via GenieX/GGUF) — no training required, matches beginner skill level.
- No physical Snapdragon hardware needed: the app itself demos on the participant's own machine; the NPU benchmark comes from a genuine Qualcomm AI Hub cloud-device profiling job. This distinction must be stated explicitly in the README and video (see [[verdict]] Decision #13) to avoid an overclaiming accusation.
- Post-event viability: open-sourceable as a "voice-to-structured-form" pattern applicable to any low-literacy digital-inclusion use case (mentioned in README only, not built as a platform for the submission itself).

## Scoring against judging criteria
| Criterion | How VoiceForm scores |
|---|---|
| Technical Implementation | Real Qualcomm AI Hub cloud-device profiling benchmark (named device, latency/tokens-per-sec vs CPU) shown before any feature work; GBNF-constrained JSON output proves real engineering, not a lucky demo |
| Application Use Case & Innovation | Accessibility/GovTech angle proven to win in the closest analog, currently unclaimed here; named real form (NSP) makes the use case checkable, not vague |
| Deployment & Accessibility | Single-screen, oversized mic button, large Devanagari-capable typography, no login/setup friction — installable and usable by the stated low-literacy user, not just a developer |
| Presentation & Documentation | README explicitly states what's real vs. simulated (per Decision #13), demo video follows the confirmed 90-second structure (human → benchmark → task complete) |
