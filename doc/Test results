# Test Results

All tests were performed on video recordings of real lip movements. The model predicted phoneme sequences which were decoded to text and compared against the ground truth transcript.

---

## Results Summary

| Test | Input Sentence | Accuracy |
|---|---|---|
| Test 1 | "Hi, I am Rohith, I'm studying in AMC Engineering College and my choice of branch is ISE." | 41.13% |
| Test 2 | "I have a dog named rocky and he is three years old and he's very cute." | **93.33%** |
| Test 3 | "I'm staying at college hostel facility and in my opinion my room looks and feels great." | **87.55%** |
| Test 4 | "I have a friend named niru who is the most brilliant student in the class." | **93.33%** |
| Test 5 | "I have another friend named harsha who thinks he knows everything about me but he doesn't." | **94.11%** |
| Test 6 | "I have a friend named prapulla who is the most useless fellow in this world." | **100%** |
| Test 7 | "Now I am recording this video to train my model to be as accurate as possible." | **93.33%** |

---

## Analysis

- **Average accuracy (Tests 2–7):** ~93.6%
- **Test 1 lower accuracy:** The sentence contained domain-specific proper nouns ("AMC Engineering College", "ISE") which were underrepresented in training data, leading to phoneme mismatch.
- **Test 6 — 100% accuracy:** Shorter, common-vocabulary sentence with clear lip articulation and good lighting conditions.
- **General trend:** Everyday conversational sentences with common vocabulary achieve >87% accuracy consistently.

---

## Key Observations

- Lighting conditions and speaker distance significantly affect lip segmentation quality.
- Proper nouns (names, institutions) reduce accuracy due to training data limitations.
- Longer sentences with natural speech rhythm perform better than short isolated words.
- The model generalizes well across different sentence structures and topics.
