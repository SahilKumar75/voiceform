# VoiceForm

An on device voice assistant that fills the NSP Post-Matric Scholarship form for a low literacy Hindi speaker, with a spoken confirm and correct loop. Built for the Snapdragon® AI Lab Build & Present Challenge (Qualcomm, 2026).

**Status: AI Hub NPU benchmark obtained, schema locked, placeholder UI built (no ASR/LLM wired up yet).**

## What's real vs. simulated
_To be filled in as the build progresses, see docs/build plan.md Decision on live demo vs. benchmark honesty. This section must state plainly what ran on the builder's own machine versus what came from Qualcomm AI Hub's cloud device profiling, before submission._

## Problem
See [docs/idea spec.md](docs/idea spec.md).

## How it works
See architecture diagram in [docs/build plan.md](docs/build plan.md).

## Benchmark
Real Qualcomm AI Hub cloud device profiling job, Whisper tiny (float, ONNX runtime), device: Snapdragon X Elite CRD.

| Component | Estimated inference time | Ops on NPU | Peak memory |
|---|---|---|---|
| Encoder | 26.0 ms | 294 / 294 (100%) | 33 MB |
| Decoder (per step) | 2.0 ms | 509 / 509 (100%) | 83 MB |

Job details: [encoder profile](https://workbench.aihub.qualcomm.com/jobs/jp0mrr7ng/), [decoder profile](https://workbench.aihub.qualcomm.com/jobs/j568134yg/).

This confirms the model compiles and runs entirely on the Hexagon NPU (0 ops fell back to CPU or GPU) on a real cloud hosted Snapdragon X Elite device, obtained without owning physical hardware, via Qualcomm AI Hub's device farm.

## Install & run
_TBD._

## Demo video
_TBD._
