import pdfplumber

def extract_text_from_pdf(pdf_path, pages=None):
    """Extract text from given PDF. Pages can be None or list of page numbers."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if pages:
                text = "\n".join(pdf.page[i].extract_text() for i in pages if i < len(pdf.pages))
            else:
                text = "\n".join(page.extract_text() for page in pdf.pages)
        return text
    except Exception as e:
        raise RuntimeError(f"Error extracting PDF text: {e}")

def extract_pages(pdf_path):
    """Return list of page texts."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            return [page.extract_text() for page in pdf.pages]
    except Exception as e:
        raise RuntimeError(f"Unable to extract pages: {e}")
