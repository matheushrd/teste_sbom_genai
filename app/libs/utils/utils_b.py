# app/libs/utils/utils_b.py

def add_prefix(text: str, prefix: str = "PROCESSED:") -> str:
    """Adiciona um prefixo a uma string."""
    return f"{prefix} {text}"