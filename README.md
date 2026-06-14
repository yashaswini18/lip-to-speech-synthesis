# lip-to-speech-synthesis
 Multimodal AI system that converts lip movements to speech using CNN + LSTM + gTTS — VTU Internship Project 2023-24
# 🗣️ Lip-to-Speech Synthesis using Machine Learning

> **Internship Project** — 3rd Year B.E. (Electronics & Communication Engineering)  
> **Conducted at:** Compsoft Technologies, Bengaluru  
> **College:** AMC Engineering College, VTU Belagavi | 2023–24  
> **Intern:** Yashaswini R (1AM21EC101)

---

## 📌 Project Overview

**Lip-to-Speech Synthesis** is a multimodal AI system that converts **silent lip movements** from video into coherent speech — without any audio input. This project implements the system using **Python**, **Computer Vision (OpenCV)**, and **Deep Learning (CNN + RNN)**, with real-time performance.

The system can be used for:
- 🤫 Silent communication interfaces
- ♿ Assistive technology for people with speech impairments
- 🎮 Immersive gaming & multimedia experiences
- 🌍 Cross-language and cross-cultural communication

---

## 🧠 How It Works

```
Video Input (lip movement)
        │
        ▼
  Frame Extraction & Preprocessing
  (lip region segmentation, normalization)
        │
        ▼
  CNN — Visual Feature Extraction
  (spatial lip articulation features)
        │
        ▼
  RNN — Temporal Modelling
  (audio spectrogram + temporal dependencies)
        │
        ▼
  Multimodal Fusion
  (attention mechanisms / concatenation)
        │
        ▼
  Text-to-Speech Engine (gTTS)
        │
        ▼
  🔊 Synthesized Speech Output
```

---

## 📊 Test Results

| Test | Input Sentence | Accuracy |
|---|---|---|
| Test 1 | "Hi, I am Rohith, I'm studying in AMC Engineering College..." | 41.13% |
| Test 2 | "I have a dog named rocky and he is three years old..." | **93.33%** |
| Test 3 | "I'm staying at college hostel facility and my room looks great..." | **87.55%** |
| Test 4 | "I have a friend named niru who is the most brilliant student..." | **93.33%** |
| Test 5 | "I have another friend named harsha who thinks he knows everything..." | **94.11%** |
| Test 6 | "I have a friend named prapulla who is the most useless fellow..." | **100%** |
| Test 7 | "Now I am recording this video to train my model to be accurate..." | **93.33%** |

> 📈 Average accuracy across Tests 2–7: **~93.6%**  
> Test 1 had lower accuracy due to domain-specific vocabulary (college/branch names).

---

## 🔧 Tech Stack

| Category | Tool / Library |
|---|---|
| Language | Python 3.12 |
| IDE | Visual Studio Code |
| Computer Vision | OpenCV |
| Deep Learning | CNN (visual) + RNN (temporal) |
| Data Handling | NumPy, Pandas |
| ML Framework | TensorFlow / PyTorch |
| Speech Output | gTTS (Google Text-to-Speech) |
| ML Utilities | Scikit-learn |

---

## 📁 Repository Structure

```
lip-to-speech-synthesis/
├── README.md
├── src/
│   ├── preprocess.py           # Frame extraction & lip segmentation
│   ├── feature_extraction.py   # CNN visual + RNN audio feature pipeline
│   ├── fusion.py               # Multimodal fusion (attention mechanism)
│   ├── tts_output.py           # Text-to-speech synthesis using gTTS
│   └── main.py                 # End-to-end pipeline runner
├── model/
│   └── model_architecture.md   # CNN + RNN model design overview
├── docs/
│   ├── system_design.md        # Design & analysis documentation
│   └── requirements.md         # Hardware & software requirements
└── results/
    └── test_results.md         # All 7 test case results with accuracy
```

---

## ⚙️ Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/lip-to-speech-synthesis.git
cd lip-to-speech-synthesis
```

### 2. Install Dependencies
```bash
pip install opencv-python numpy pandas scikit-learn tensorflow gTTS
```

### 3. Run the Pipeline
```bash
python src/main.py --video path/to/lip_video.mp4
```

---

## 💻 Hardware Requirements

| Component | Minimum | Recommended |
|---|---|---|
| Processor | 1 GHz | 2 GHz or more |
| RAM | 1 GB | 4 GB or above |
| Storage | 32 GB | 64 GB or more |
| Network | LAN / Wi-Fi | — |

**Software:** Windows 7+, Python 3.12, Visual Studio Code

---

## 🔬 Existing Systems Compared

| System | Approach | Notes |
|---|---|---|
| LipNet | Deep learning end-to-end | Lip reading to text |
| Lip2AudSpec | CNN + Audio Spectrogram | Visual to audio spectrogram |
| LipGAN | Generative Adversarial Network | Lip sync and speech |
| HMM/GMM based | Statistical models | Captures temporal lip dynamics |
| **This Project** | CNN + RNN + Multimodal Fusion + gTTS | Real-time, Python-based |

---

## 🔮 Future Enhancements

- Train on larger and more diverse datasets for improved generalization
- Add multi-language and multi-dialect support
- Integrate with ESP32 / edge devices for embedded deployment
- Build a web interface using Flask for browser-based real-time demo
- Explore Transformer-based architectures (LipFormer, AV-HuBERT)

---

## 📚 References

1. Afouras T., Chung J.S., Zisserman A. — *"The Conversation: Deep Audio-Visual Speech Enhancement"* arXiv:1804.04
2. B. Prof, Akash P., Dhanush S., et al. — *"Lip-to-Speech Synthesis Using Machine Learning"*, IJARCCE, 2023
3. Akbari H. et al. — *"Lip2AudSpec: Speech Reconstruction from Silent Lip Movements Video"*, ICASSP 2018
4. Hegde S. et al. — *"Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild"*, 2022
5. Kim M. et al. — *"CroMM-VSR: Cross-Modal Memory Augmented Visual Speech Recognition"*, IEEE Transactions on Multimedia, 2022
6. Vougioukas K. et al. — *"Video-Driven Speech Reconstruction using Generative Adversarial Networks"*, arXiv:1906.06301, 2019

---

## 🏢 About the Internship

**Organization:** Compsoft Technologies, Bengaluru  
Compsoft Technologies is a software development company specializing in Python, web development, Android apps, ERP solutions, and software training. The internship provided hands-on exposure to machine learning workflows, computer vision, and real-world model development.

---

*Internship completed at Compsoft Technologies, Bengaluru | AMC Engineering College, VTU | 2023–24*
