# app/main.py
from libs.utils.utils_a import to_uppercase
from libs.utils.utils_b import add_prefix
from libs.aws_connector.aws_connector import S3Connector
import pandas as pd

def process_data(input_data: str) -> str:
    """
    Processa os dados aplicando transformações das bibliotecas de utils.
    """
    upper_data = to_uppercase(input_data)
    processed_data = add_prefix(upper_data)
    return processed_data

def main():
    """Função principal do aplicativo."""
    # Exemplo de uso do pandas
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    print("DataFrame criado com pandas:")
    print(df.head())
    print("-" * 20)

    # Processa os dados
    my_data = "dados para teste"
    final_result = process_data(my_data)
    print(f"Resultado do processamento: {final_result}")
    print("-" * 20)

    # # Usa o conector S3
    # s3_conn = S3Connector()
    # upload_response = s3_conn.upload_to_s3(
    #     bucket_name="meu-bucket-de-teste",
    #     file_content=final_result,
    #     object_name="resultado.txt"
    # )

    # if upload_response['ResponseMetadata']['HTTPStatusCode'] == 200:
    #     print("Upload para S3 simulado com sucesso!")
    # else:
    #     print("Falha no upload para o S3.")

if __name__ == "__main__":
    main()