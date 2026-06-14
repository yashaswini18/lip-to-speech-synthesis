# Model Architecture — Lip-to-Speech Synthesis

## Overview

The model uses two parallel branches (CNN + RNN) whose outputs are merged via a multimodal fusion layer, followed by a decoder that produces text or phoneme predictions.

---

## Full Architecture

```
Input: Video Frames (lip region crops)
         │
         ▼
┌─────────────────────────────┐
│      CNN Visual Branch      │
│                             │
│  Conv2D(32, 3x3) + ReLU    │
│  MaxPool(2x2)               │
│  Conv2D(64, 3x3) + ReLU    │
│  MaxPool(2x2)               │
│  Conv2D(128, 3x3) + ReLU   │
│  MaxPool(2x2)               │
│  Flatten                    │
│  Dense(256) + ReLU          │
└─────────────┬───────────────┘
              │
              │  Visual Features (256-d)
              │
              ▼
     ┌────────────────┐       ┌─────────────────────────────┐
     │ Attention /    │◄──────│     RNN Audio Branch        │
     │ Concatenation  │       │                             │
     │   Fusion       │       │  Input: Mel Spectrogram     │
     └────────┬───────┘       │  LSTM(128, return_seq=True) │
              │               │  LSTM(64)                   │
              │               │  Dense(128) + ReLU          │
              │               └─────────────────────────────┘
              ▼
     Fused Feature Vector
              │
              ▼
     ┌─────────────────┐
     │  Seq2Seq        │
     │  Decoder        │
     │  (CTC / LSTM)   │
     └────────┬────────┘
              │
              ▼
     Phoneme / Text Prediction
              │
              ▼
        gTTS Engine
              │
              ▼
       🔊 Audio Output (.mp3)
```

---

## Key Design Choices

| Choice | Reason |
|---|---|
| CNN for visual features | Captures spatial lip shape and articulation per frame |
| RNN (LSTM) for audio | Captures temporal dependencies in speech over time |
| Attention fusion | Learns to weight visual vs audio importance dynamically |
| gTTS for output | Simple, reliable, and language-agnostic TTS for synthesis |

---

## Training Data Format

The model is trained on synchronized audiovisual recordings:
- **Video:** lip movement clips at ~25 fps, cropped to 64×64
- **Audio:** 16kHz .wav, converted to 80-band Mel spectrograms
- **Labels:** Phoneme or word-level transcriptions

---

## Evaluation Metrics

| Metric | What it Measures |
|---|---|
| Accuracy (%) | Word/phoneme match between prediction and ground truth |
| Intelligibility | Human-rated clarity of synthesized speech |
| Naturalness | Similarity to natural human speech (prosody, fluency) |
| Lip Sync Score | Alignment between lip movement timing and synthesized audio |
