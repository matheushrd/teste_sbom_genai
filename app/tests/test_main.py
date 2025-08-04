# app/tests/tests.py
import pytest
import sys
import os

# Adiciona o diretório raiz 'app' ao path para que os imports funcionem
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from libs.utils.utils_a import to_uppercase
from libs.utils.utils_b import add_prefix
# from libs.aws_connector.aws_connector import S3Connector
from main import process_data

# Testes para utils_a.py
def test_to_uppercase_success():
    """Testa a conversão para maiúsculas."""
    assert to_uppercase("hello world") == "HELLO WORLD"

def test_to_uppercase_with_empty_string():
    """Testa com uma string vazia."""
    assert to_uppercase("") == ""

def test_to_uppercase_raises_error():
    """Testa se um erro é lançado para input não-string."""
    with pytest.raises(TypeError):
        to_uppercase(123)

# Testes para utils_b.py
def test_add_prefix_default():
    """Testa o prefixo padrão."""
    assert add_prefix("data") == "PROCESSED: data"

def test_add_prefix_custom():
    """Testa um prefixo customizado."""
    assert add_prefix("data", prefix="CUSTOM:") == "CUSTOM: data"

# Teste para o conector AWS
# def test_s3_connector_upload():
#     """Testa a resposta simulada do upload S3."""
#     connector = S3Connector()
#     response = connector.upload_to_s3("bucket", "content", "object")
#     assert response['ResponseMetadata']['HTTPStatusCode'] == 200
#     assert 'ETag' in response

# Teste de integração para a função principal de processamento
def test_process_data():
    """Testa o fluxo de processamento completo."""
    result = process_data("meus dados")
    assert result == "PROCESSED: MEUS DADOS"