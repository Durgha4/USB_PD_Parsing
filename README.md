USB Power Delivery Specification PDF Parser

📌 Overview
This project is a **Python-based parser** for extracting structured information from the **USB Power Delivery Specification PDF**.  
It processes:
- **Table of Contents (ToC)** into JSONL  
- **General sections** (content) into JSONL  
- **Excel-based validation report** showing schema compliance

The parser uses **regex-based extraction**, **JSON Schema validation**, and **Excel reporting** for clean, reusable, and standards-compliant data output.

🚀 Features

- **PDF Text Extraction** using [`pdfplumber`](https://github.com/jsvine/pdfplumber)
- **Flexible Table of Contents Parsing**  
- **Section Content Parsing** with hierarchical `section_id` support
- **JSON Schema Validation** for both ToC and sections
- **Validation Report** exported to both **console** and **Excel (`.xlsx`)**
- **Customizable page range** for ToC scanning
- **JSONL Output** for easy downstream processing


📂 Project Structure

usb_pd_parser/
│
├── data/
│ ├── input.pdf # Your USB PD spec PDF
│ ├── toc.jsonl # Parsed Table of Contents
│ ├── sections.jsonl # Parsed section data
│ ├── validation_report.xlsx # Excel validation report
│
├── schemas/
│ ├── toc_schema.json # ToC JSON Schema
│ ├── section_schema.json # Section JSON Schema
│
├── utils/
│ ├── pdf_utils.py # PDF text extraction
│ ├── parsing_utils.py # Regex parsing logic
│ ├── io_utils.py # Save/validate helpers
│
├── main.py # Entry point for execution
├── requirements.txt # Python dependencies
└── README.md # Documentation


