# Natural Language Processing

โปรเจกต์ตัวอย่างสำหรับเรียนรู้และเปรียบเทียบการประมวลผลภาษาธรรมชาติ (NLP) ด้วย 3 ไลบรารีหลัก ได้แก่ **NLTK**, **spaCy** (สำหรับภาษาอังกฤษ) และ **PyThaiNLP** (สำหรับภาษาไทย) ในที่เดียว

## เหมาะกับใคร

โปรเจกต์นี้เหมาะสำหรับผู้ที่สนใจเริ่มต้นศึกษา NLP โดยเฉพาะ:

- ผู้ที่อยากเห็นตัวอย่างการทำ **Tokenization, POS Tagging, Named Entity Recognition (NER), Dependency Parsing และ Stopword Removal** แบบเปรียบเทียบระหว่างไลบรารี ในโค้ดชุดเดียวกัน
- ผู้ที่อยากรู้ความแตกต่างของการตัดคำภาษาไทย (Thai word segmentation) ระหว่าง engine ต่าง ๆ ของ PyThaiNLP (`newmm`, `longest`, `mm`) เพราะภาษาไทยไม่มีช่องว่างคั่นคำ การเลือก engine มีผลต่อผลลัพธ์โดยตรง
- นักศึกษา/ผู้เริ่มต้นที่ต้องการโครงสร้างโปรเจกต์ Python ที่แยก logic เป็นโมดูล (`Process/`, `Util/`) พร้อมไฟล์ config แยกต่างหาก เพื่อเป็นแนวทางจัดโครงสร้างโปรเจกต์ NLP ของตัวเอง

## Features

| โมดูล | ไลบรารี | งานที่ทำ |
| --- | --- | --- |
| `Process/Nltk_Process.py` | NLTK | Tokenize, Sentence Tokenize, POS Tagging, Named Entity Chunking, Stopwords (EN) |
| `Process/Spacy_Process.py` | spaCy (`en_core_web_sm`) | Tokenize, POS Tagging, Dependency Parsing |
| `Process/Py_Thai_NLP.py` | PyThaiNLP | ตัดคำภาษาไทย (multi-engine), POS Tagging, Stopwords (TH) |
| `Util/load_utils.py` | PyYAML | โหลดค่าตั้งต้นจาก `config.yaml` |

## โครงสร้างโปรเจกต์

```text
Natural-Language-Processing/
├── main.py                 # จุดเริ่มรันโปรแกรม เรียกใช้ทั้ง 3 โปรเซสเซอร์
├── config.yaml              # ข้อความตัวอย่างภาษาอังกฤษ/ไทยที่ใช้ประมวลผล
├── requirements.txt          # รายการไลบรารีที่ต้องติดตั้ง
├── Process/
│   ├── Nltk_Process.py       # NLTK wrapper
│   ├── Spacy_Process.py      # spaCy wrapper
│   └── Py_Thai_NLP.py        # PyThaiNLP wrapper
└── Util/
    └── load_utils.py         # ฟังก์ชันโหลด config.yaml
```

## การติดตั้ง

1. สร้างและเปิดใช้งาน virtual environment (แนะนำ conda หรือ venv)

   ```bash
   conda create -n text_cls python=3.11
   conda activate text_cls
   ```

2. ติดตั้งไลบรารีที่จำเป็น

   ```bash
   pip install -r requirements.txt
   ```

3. ดาวน์โหลดโมเดลภาษาอังกฤษของ spaCy (ต้องทำครั้งเดียว)

   ```bash
   python -m spacy download en_core_web_sm
   ```

   ส่วนข้อมูลของ NLTK (`punkt`, `averaged_perceptron_tagger`, `stopwords`, `maxent_ne_chunker`, `words` ฯลฯ) และข้อมูลของ PyThaiNLP จะถูกดาวน์โหลดอัตโนมัติเมื่อรันโปรแกรมครั้งแรก (ต้องต่ออินเทอร์เน็ต)

## การตั้งค่า (`config.yaml`)

กำหนดข้อความที่จะนำไปประมวลผลได้ที่ `config.yaml`:

```yaml
text : "This is a sample text for NLP processing. It contains multiple sentences."
th_text : "นักเรียนชาติจีนเรียนภาษาไทยกับอาจารย์"
```

- `text` — ข้อความภาษาอังกฤษ ใช้กับ NLTK และ spaCy
- `th_text` — ข้อความภาษาไทย ใช้กับ PyThaiNLP

## วิธีใช้งาน

```bash
python main.py
```

โปรแกรมจะประมวลผลตามลำดับและพิมพ์ผลลัพธ์ของ:

1. **NLTK** — Sentence tokens, POS tags, Named Entities, Tokens/Cleaned tokens (ตัด stopwords)
2. **spaCy** — Tokens, POS, Dependency relation, Head word
3. **PyThaiNLP** — Thai tokens, Cleaned Thai tokens, Thai POS tags และผลเปรียบเทียบการตัดคำภาษาไทยด้วย engine `newmm`, `longest`, `mm`

### หมายเหตุ: การแสดงผลภาษาไทยบน Windows Terminal

ถ้ารันบน Command Prompt/PowerShell แล้วเจอ `UnicodeEncodeError` ตอนพิมพ์ข้อความไทย ให้ตั้งค่า encoding เป็น UTF-8 ก่อนรัน:

```bash
set PYTHONIOENCODING=utf-8
python main.py
```

หรือใช้ Windows Terminal ที่ตั้ง code page เป็น UTF-8 (`chcp 65001`)

## License

โปรเจกต์นี้จัดทำเพื่อการศึกษา (รายวิชา 1323404 NLP)
