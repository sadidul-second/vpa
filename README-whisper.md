---
datasets:
- mozilla-foundation/common_voice_13_0
language:
- bn
metrics:
- wer
pipeline_tag: automatic-speech-recognition
tags:
- audio
- automatic-speech-recognition
- hf-asr-leaderboard
---

## Model Details


## Usage

```shell
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch

r = sr.Recognizer()
device = "cuda:0" if torch.cuda.is_available() else "cpu"
# load model and processor
processor = WhisperProcessor.from_pretrained(WHISPER_MODEL_OUTPUT, language=WHISPER_MODEL_LANGUAGE)
model = WhisperForConditionalGeneration.from_pretrained(WHISPER_MODEL_OUTPUT).to(device)
model.config.forced_decoder_ids = None
```