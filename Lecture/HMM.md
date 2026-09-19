---
tags:
  - NLP
  - Machine-Learning
  - HMM
  - Viterbi
date: 2026-09-19
---

# การคำนวณ Hidden Markov Model (HMM) สำหรับ POS Tagging
> [!abstract] บริบทของประโยค
> ตัวอย่างการคำนวณแบบ Step-by-Step สำหรับประโยค: **"I am a Demon who destroy world"** โดยใช้กลไกการคำนวณของ **HMM ร่วมกับ Viterbi Algorithm** ในกรณีที่บางคำสามารถแตกกิ่งได้หลาย Tag (คำว่า *destroy* และ *world*)

---
## 📊 1. คลังสถิติความน่าจะเป็น (Probability Tables)

### Tag Transition Table — $P(t_i \mid t_{i-1})$
*(โอกาสการเปลี่ยนจาก Tag แนวตั้ง ไปยัง Tag แนวนอน)*

| Tag ก่อนหน้า ($t_{i-1}$) | PRON | VERB | DET | NOUN |
| :--- | :--- | :--- | :--- | :--- |
| **Start (เริ่มประโยค)** | **0.6** | 0.1 | 0.2 | 0.1 |
| **PRON** | 0.1 | **0.7** | 0.1 | 0.1 |
| **VERB** | 0.2 | 0.05 | **0.5** | **0.25** |
| **DET** | 0.05 | 0.05 | 0.05 | **0.85** |
| **NOUN** | **0.4** | 0.3 | 0.05 | 0.25 |

### Emission Table — $P(w_i \mid t_i)$
*(โอกาสที่แต่ละ Tag จะแสดงออกมาเป็นคำศัพท์นั้น ๆ)*

| Word ($w_i$) / Tag ($t_i$) | PRON | VERB | DET | NOUN |
| :--- | :--- | :--- | :--- | :--- |
| **I** | **0.5** | 0.0 | 0.0 | 0.0 |
| **am** | 0.0 | **0.6** | 0.0 | 0.0 |
| **a** | 0.0 | 0.0 | **0.9** | 0.0 |
| **Demon** | 0.0 | 0.0 | 0.0 | **0.02** |
| **who** | **0.4** | 0.0 | 0.0 | 0.0 |
| **destroy** | 0.0 | **0.1** | 0.0 | **0.05** |
| **world** | 0.0 | **0.02** | 0.0 | **0.08** |

---
## 🚶‍♂️ 2. ขั้นตอนการคำนวณคำต่อคำ (Step-by-Step)

สูตรพื้นฐานของ Viterbi ในแต่ละจุด:
$$\text{Score} = \max(\text{Previous Score} \times \text{Transition}) \times \text{Emission}$$

### 🔹 คำที่ 1: "I"
* **PRON**: $\text{Start} \times P(\text{PRON} \mid \text{Start}) \times P(\text{"I"} \mid \text{PRON}) = 1.0 \times 0.6 \times 0.5 = \mathbf{0.3}$
* *สถานะตัวประมวลผล*: `[PRON: 0.3, VERB: 0, DET: 0, NOUN: 0]`

### 🔹 คำที่ 2: "am"
* **VERB**: $\text{เดิม}(PRON) \times P(\text{VERB} \mid \text{PRON}) \times P(\text{"am"} \mid \text{VERB}) = 0.3 \times 0.7 \times 0.6 = \mathbf{0.126}$
* *สถานะตัวประมวลผล*: `[PRON: 0, VERB: 0.126, DET: 0, NOUN: 0]`

### 🔹 คำที่ 3: "a"
* **DET**: $\text{เดิม}(VERB) \times P(\text{DET} \mid \text{VERB}) \times P(\text{"a"} \mid \text{DET}) = 0.126 \times 0.5 \times 0.9 = \mathbf{0.0567}$
* *สถานะตัวประมวลผล*: `[PRON: 0, VERB: 0, DET: 0.0567, NOUN: 0]`

### 🔹 คำที่ 4: "Demon"
* **NOUN**: $\text{เดิม}(DET) \times P(\text{NOUN} \mid \text{DET}) \times P(\text{"Demon"} \mid \text{NOUN}) = 0.0567 \times 0.85 \times 0.02 = \mathbf{0.0009639}$
* *สถานะตัวประมวลผล*: `[PRON: 0, VERB: 0, DET: 0, NOUN: 0.0009639]`

### 🔹 คำที่ 5: "who"
* **PRON**: $\text{เดิม}(NOUN) \times P(\text{PRON} \mid \text{NOUN}) \times P(\text{"who"} \mid \text{PRON}) = 0.0009639 \times 0.4 \times 0.4 = \mathbf{0.000154224}$
* *สถานะตัวประมวลผล*: `[PRON: 0.000154224, VERB: 0, DET: 0, NOUN: 0]`

---
## ⚡ 3. จุดแตกกิ่งและความซับซ้อน (Multiple Tags)

### 🔹 คำที่ 6: "destroy" (เป็นไปได้ทั้ง VERB และ NOUN)

> [!note] การคำนวณแยก 2 กิ่ง
> * **กรณีเป็น VERB**: วิ่งมาจาก PRON (who)
>   $$0.000154224 \times P(\text{VERB} \mid \text{PRON}) \times P(\text{"destroy"} \mid \text{VERB}) = 0.000154224 \times 0.7 \times 0.1 = \mathbf{0.00001079568}$$
> * **กรณีเป็น NOUN**: วิ่งมาจาก PRON (who)
>   $$0.000154224 \times P(\text{NOUN} \mid \text{PRON}) \times P(\text{"destroy"} \mid \text{NOUN}) = 0.000154224 \times 0.1 \times 0.05 = \mathbf{0.00000077112}$$

*สถานะตัวประมวลผล*: `[PRON: 0, VERB: 0.00001079568, DET: 0, NOUN: 0.00000077112]`

---

### 🔹 คำที่ 7: "world" (จุดคำนวณไขว้หาเส้นทางสูงสุด)

#### ทางเลือก ก) คิดกรณี "world" เป็น VERB
1. วิ่งมาจาก destroyที่เป็น VERB: $0.00001079568 \times 0.05 \times 0.02 = \mathbf{1.079568 \times 10^{-8}}$  *(เลือกค่านี้เนื่องจากชนะข้อ 2)*
2. วิ่งมาจาก destroyที่เป็น NOUN: $0.00000077112 \times 0.3 \times 0.02 = 4.62672 \times 10^{-9}$

#### ทางเลือก ข) คิดกรณี "world" เป็น NOUN
1. วิ่งมาจาก destroyที่เป็น VERB: $0.00001079568 \times 0.25 \times 0.08 = \mathbf{2.159136 \times 10^{-7}}$ *(เลือกค่านี้เนื่องจากชนะข้อ 2)*
2. วิ่งมาจาก destroyที่เป็น NOUN: $0.00000077112 \times 0.25 \times 0.08 = 1.54224 \times 10^{-8}$

---
## 🏁 4. การตัดสินใจเลือกเส้นทาง (Backtracking)

คะแนนสะสมสุทธิที่ปลายทาง:
* `[world เป็น VERB]` = $1.079568 \times 10^{-8}$
* `[world เป็น NOUN]` = $\mathbf{2.159136 \times 10^{-7}}$  ✨ **(ชนะ)**

เมื่อย้อนรอย (Backtrack) กลับไปจากค่าที่ชนะ ระบบจะเลือกทางเดินที่เป็น **VERB ของคำว่า destroy** ส่งผลให้ได้ลำดับ Tag ที่ถูกต้องที่สุดคือ:

$$\mathbf{I [PRON] \rightarrow am [VERB] \rightarrow a [DET] \rightarrow Demon [NOUN] \rightarrow who [PRON] \rightarrow destroy [VERB] \rightarrow world [NOUN]}$$

---
## 🔗 ลิงก์ที่เกี่ยวข้องภายในคลัง Obsidian
* [[WordPiece Tokenization]]
* [[BiLSTM คืออะไร]]
* [[Viterbi Algorithm Deep Dive]]
