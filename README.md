# USB Power Delivery Specification PDF Parser

## 📌 Overview
🔍 **Python-based Parser** designed to extract and structure content from the **USB Power Delivery Specification PDF**.

📄 **Focus Outputs**:
- 📑 **Table of Contents (ToC)** – identifies each section with its **ID**, **title**, **page number**, and **hierarchy**  
- 📚 **General Sections** – captures **full section titles**, **hierarchy**, **starting/ending pages**, and **content text**  

🛡 **The extracted data is**:  
- ✅ **Validated** against predefined **JSON Schemas** for correctness  
- 💾 **Saved** in newline-delimited JSON (**JSONL**) files for easy processing  
- 📊 **Reported** in a detailed **Excel validation report**, showing ✅ valid and ❌ failed entries for both ToC and sections  

⚙️ **Core Capabilities**:  
- 📜 **PDF text extraction** (`pdfplumber`)  
- 🔍 **Pattern-based parsing** with **regex**  
- 🧪 **Data integrity validation** (`jsonschema`)  
- 📢 **Error reporting** and summaries  
- 📈 **Excel report generation** (`openpyxl`) for review  

🎯 **Primary Goal**:  
Turn an **unstructured**, complex **USB PD specification PDF** into **clean**, **validated**, and **structured data** 💎 — ready for 🔎 search, 📊 analysis, or 🔗 integration into other systems.

---

## 🚀 Features
- Extracts text directly from PDF  
- Parses hierarchical Table of Contents  
- Captures full section content with metadata  
- Validates against JSON Schemas  
- Saves outputs in JSONL format plus Excel report  
- Easy to customise regex and page ranges

---

## 🔧 Requirements
- **Python** `>=3.7`
- **pip** to install packages

Dependencies:

pdfplumber
jsonschema
tqdm
openpyxl

text

Install all dependencies:

pip install -r requirements.txt

text

---

## 🚀 Execution

1. **Install dependencies**

pip install -r requirements.txt

text
*(Requires Python 3.7+)*

2. **Place your PDF** in the `data/` folder as `input.pdf`  
*(Or update `pdf_path` in `main.py` if your file name/location is different)*

3. **Run the parser**

python main.py

text

4. **Check the outputs** in `data/`:
- `toc.jsonl` → Parsed Table of Contents  
- `sections.jsonl` → Parsed sections with content  
- `validation_report.xlsx` → Excel validation report of schema checks  

---

## 📊 Validation Report
- **Summary** sheet → Numbers of valid vs error entries for both ToC and Sections  
- **TOC Errors** sheet → Each failing Table of Contents entry with error message  
- **Section Errors** sheet → Each failing section with error details  

---

## 📄 License
This project is provided for educational and parsing use. You may adapt it as needed.

---

## 🔍 Keywords
`USB Power Delivery` `PDF parser` `JSON Schema` `Table of Contents extraction`  
`Python PDF processing` `USB PD spec` `pdfplumber` `jsonschema`  
`Excel report` `openpyxl` `JSONL output` `regex parsing`
