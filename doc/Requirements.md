# Requirements Specification

## Hardware Requirements

| Component | Minimum | Recommended |
|---|---|---|
| Processor | 1 GHz | 2 GHz or more |
| RAM | 1 GB | 4 GB or above |
| Storage | 32 GB | 64 GB or more |
| Network | LAN / Wi-Fi adapter | — |
| Webcam | Any (for live input) | HD 1080p |

---

## Software Requirements

| Software | Version |
|---|---|
| Operating System | Windows 7 or newer / Ubuntu 20.04+ |
| Python | 3.12 |
| IDE | Visual Studio Code |

---

## Python Dependencies

Install all dependencies with:

```bash
pip install opencv-python numpy pandas scikit-learn tensorflow gTTS librosa
```

| Package | Version | Purpose |
|---|---|---|
| `opencv-python` | ≥4.8 | Video capture & face/lip detection |
| `numpy` | ≥1.24 | Numerical array operations |
| `pandas` | ≥2.0 | Data loading and CSV handling |
| `scikit-learn` | ≥1.3 | ML utilities, metrics |
| `tensorflow` | ≥2.13 | CNN & RNN model building |
| `librosa` | ≥0.10 | Audio loading & Mel spectrogram |
| `gTTS` | ≥2.4 | Google Text-to-Speech output |
