# Pitch Plan — VoiceForm

This is an **async, submission-only** challenge — no live pitch stage exists (see [[rules-and-judging]] and [[timeline]]). The demo video and README ARE the pitch. No Q&A will save a confusing moment, so every second must be self-explanatory.

## Story arc
1. **The human problem** (silent/visible, ~10s): a person struggling to fill a government form — can't read it confidently, or it's in a script/language mismatch with their comfort.
2. **The fix, live** (~50-60s): the same person speaks their details in Hindi; fields fill on screen; one field is deliberately mis-heard; they say a correction; it re-fills; form completes.
3. **The proof** (~8-10s): a clean benchmark table — real Qualcomm AI Hub cloud-device profiling numbers (latency/tokens-per-sec, named Snapdragon device, vs. CPU baseline).
4. **Close** (~5-10s): the same person, task done, on screen. No architecture diagram, no logo slide.

Total: under 90 seconds, per [[verdict]] Decision #14.

## Slide-by-slide outline (for README/submission form, not a live deck)
1. **Problem** — one sentence, one number: name the user and the specific failure mode (e.g. "First-gen scholarship applicants lose renewals to form errors they can't catch by reading.")
2. **Solution** — one sentence: "VoiceForm fills the real NSP Post-Matric Scholarship form by voice, entirely on-device."
3. **How it works** — the mermaid architecture diagram from [[build-plan]], with the live-demo-path vs. AI-Hub-benchmark-path distinction clearly labeled (this is not optional — see Decision #13).
4. **Benchmark** — the real numbers, named device, CPU comparison.
5. **What's real vs. simulated** — explicit statement: the app runs on [your dev machine]; the NPU numbers come from a genuine Qualcomm AI Hub cloud-hosted device profiling job, not the same machine running the live demo.
6. **What's next** — one line only: mention the "reusable voice-to-structured-data" idea as future work, don't oversell it (per the cut line — never build an SDK for this submission).

## Demo script (2-3 minutes as spoken instructions to yourself while recording, video itself under 90s)
1. Open on a static shot or your own hands, not the IDE. Say/show the problem in one sentence (text overlay in Hindi + English, or spoken).
2. Press the mic button. Speak: name, DOB, annual income, caste category, bank IFSC — naturally, not overly clean.
3. Let one field come out wrong (real ASR error, or deliberately mumble a number).
4. Say the correction phrase ("नहीं, बदलो" / "no, change it") — show the field re-filling correctly.
5. Show the completed form.
6. Cut to the benchmark table (8-10 seconds, no more).
7. Return to the completed form / the same "person" shot. End.

## Backup video plan
Record this exact script and save it by Day 11 of [[build-plan]], well before the deadline — per Session A's fallback-plan requirement, given the single-submission/no-edit rule and a fragile solo toolchain. If the live re-recording on submission day has any hiccup, the Day-11 backup is the one that gets submitted.

## The number/proof point that anchors the pitch
The Qualcomm AI Hub cloud-device profiling benchmark: a specific latency number (e.g. "Xms inference on Snapdragon X Elite Hexagon NPU vs Yms on CPU") on a named device. This is the single artifact a skeptical internal Qualcomm judge cannot dismiss as "just a nice idea" — it's the one number every advisor across both council sessions named as non-negotiable.

## Likely judge questions, with answers
| Question | Answer |
|---|---|
| "Is this actually running on a Snapdragon NPU, or is that just a claim?" | "The app demo ran on my own machine for recording purposes; the benchmark numbers shown are from a real Qualcomm AI Hub cloud-hosted device profiling job against [named device] — I didn't have physical access to a Snapdragon X-series HP PC, and I've stated that explicitly rather than blur the two." |
| "Why the NSP scholarship form specifically, not a generic assistant?" | "Because a generic assistant is what everyone else with the same AI tools defaults to. This is a real, findable government form with a defined schema, so the claim is checkable — not a vague accessibility pitch." |
| "What happens if the ASR mishears something important, like a bank account number?" | "That's exactly what the confirm-and-correct loop is for — every field is read back before being accepted, and low-confidence or rejected fields get re-prompted by voice, not silently accepted." |
| "Did you train any models?" | "No — deliberately not, given the time budget. Whisper and the small LLM are both pre-built, pre-quantized models pulled from Qualcomm AI Hub's model zoo; the engineering is in the pipeline (ASR → constrained JSON extraction → correction loop), not in model training." |
| "Why Hindi only, why not more languages?" | "Scoping discipline — one language done reliably beats three done shallowly, especially solo in under 40 hours. The architecture doesn't change to add a language later; only the ASR language setting and prompt would." |
