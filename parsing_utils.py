import re


def parse_toc_line(line, doc_title):
    """
    Parses a Table of Contents line into JSON-structured dict.
    Flexible to match formats like: "2.1   Protocol Layer    17"
    """

    # Allow tabs or spaces, flexible title capture, page number at the end
    toc_pattern = re.compile(
        r"^(\d+(?:\.\d+)*)(?:\s+|\t+)(.+?)(?:\s+|\t+)(\d+)$"
    )

    line_clean = line.strip()
    match = toc_pattern.match(line_clean)
    if not match:
        return None

    section_id, title, page = match.groups()
    title = title.strip().rstrip('.')  # remove trailing dots if any

    level = section_id.count('.') + 1
    parent_id = ".".join(section_id.split('.')[:-1]) if '.' in section_id else None
    full_path = f"{section_id} {title}"

    return {
        "section_id": section_id,
        "title": title,
        "page": int(page),
        "level": level,
        "parent_id": parent_id,
        "full_path": full_path,
        "doc_title": doc_title,
        "tags": []
    }


def parse_sections(pages, doc_title):
    """
    Parses general sections from all pages.
    """

    sections = []
    # Matches start of a section line: number(s) + title
    section_pattern = re.compile(r"^(\d+(?:\.\d+)*)(?:\s+|\t+)(.+)$")

    current_section = None
    for idx, text in enumerate(pages, start=1):
        if not text:
            continue
        for line in text.splitlines():
            match = section_pattern.match(line.strip())
            if match:
                if current_section:  # Close previous section
                    current_section["page_end"] = idx - 1
                    sections.append(current_section)

                section_id, title = match.groups()
                current_section = {
                    "section_id": section_id,
                    "title": title.strip(),
                    "content": "",
                    "page_start": idx,
                    "page_end": idx,
                    "level": section_id.count('.') + 1,
                    "parent_id": ".".join(section_id.split('.')[:-1]) if '.' in section_id else None,
                    "full_path": f"{section_id} {title.strip()}",
                    "doc_title": doc_title,
                    "tags": []
                }
            elif current_section:
                current_section["content"] += line + "\n"

    # Append last section
    if current_section:
        sections.append(current_section)

    return sections
