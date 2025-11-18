import bleach

def sanitize_text(text: str) -> str:
    # Strip all HTML tags & script-like content
    return bleach.clean(text, tags=[], attributes={}, strip=True)
