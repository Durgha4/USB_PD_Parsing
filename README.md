🔍 Python-based Parser designed to extract and structure content from the USB Power Delivery Specification PDF.

📄 Focus Outputs:

    📑 Table of Contents (ToC) – identifies each section with its ID, title, page number, and hierarchy

    📚 General Sections – captures full section titles, hierarchy, starting/ending pages, and content text

🛡 The extracted data is:

    ✅ Validated against predefined JSON Schemas for correctness

    💾 Saved in newline-delimited JSON (JSONL) files for easy processing

    📊 Reported in a detailed Excel validation report, showing ✅ valid and ❌ failed entries for both ToC and sections

⚙️ Core Capabilities:

    📜 PDF text extraction (pdfplumber)

    🔍 Pattern-based parsing with regex

    🧪 Data integrity validation (jsonschema)

    📢 Error reporting and summaries

    📈 Excel report generation (openpyxl) for review

🎯 Primary Goal:
Turn an unstructured, complex USB PD specification PDF into clean, validated, and structured data 💎 — ready for 🔎 search, 📊 analysis, or 🔗 integration into other systems.
