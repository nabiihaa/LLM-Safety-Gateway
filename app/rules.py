import re

# Very simple first rule — you can expand this later
INJECTION_PATTERNS = [
    r"ignore (all )?previous instructions",
    r"disregard above",
    r"pretend to be",
    r"you are now",
]

def is_prompt_injection(prompt: str) -> bool:
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, prompt, re.I):
            return True
    return False
