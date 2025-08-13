import json
from utils.pdf_utils import extract_pages
from utils.parsing_utils import parse_toc_line, parse_sections
from utils.io_utils import save_jsonl, validate_json


def main():
    pdf_path = "data/input.pdf"
    doc_title = "USB Power Delivery Specification"

    print("Extracting pages...")
    pages = extract_pages(pdf_path)

    # ===================== TOC Extraction =====================
    with open("schemas/toc_schema.json") as f:
        toc_schema = json.load(f)

    toc_entries = []
    print("Parsing Table of Contents...")

    # Try first 3 pages for ToC — change [:3] if your ToC is longer
    for page_num, page_text in enumerate(pages[:3], start=1):
        if not page_text:
            continue
        for line in page_text.splitlines():
            record = parse_toc_line(line, doc_title)
            if record:
                try:
                    validate_json(record, toc_schema)
                    toc_entries.append(record)
                except Exception as e:
                    print(f"Validation error for line: {line} — {e}")

    if not toc_entries:
        print("[WARNING] No Table of Contents entries found. Check your regex or page range.")
    else:
        save_jsonl(toc_entries, "data/toc.jsonl")
        print(f"✅ Saved TOC entries: {len(toc_entries)}")

    # ===================== Section Extraction =====================
    with open("schemas/section_schema.json") as f:
        sec_schema = json.load(f)

    print("Parsing sections...")
    sections = parse_sections(pages, doc_title)
    for sec in sections:
        try:
            validate_json(sec, sec_schema)
        except Exception as e:
            print(f"Validation error in section {sec.get('section_id')}: {e}")

    save_jsonl(sections, "data/sections.jsonl")
    print(f"✅ Saved Sections: {len(sections)}")


if __name__ == "__main__":
    main()
