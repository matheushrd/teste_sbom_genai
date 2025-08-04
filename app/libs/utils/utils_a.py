# app/libs/utils/utils_a.py

def to_uppercase(text: str) -> str:
    """Converte uma string para maiúsculas."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.upper()