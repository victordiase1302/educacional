import boto3
from django.conf import settings

from .creat_finetune import train_model
from .generate_training import generate_training_data


def upload_to_s3(file_name, bucket_name, object_name=None):
    """
    Faz o upload de um arquivo para o bucket S3 e retorna a URI do objeto.

    :param file_name: Nome do arquivo local a ser carregado
    :param bucket_name: Nome do bucket S3
    :param object_name: Nome do objeto S3 (se diferente do file_name)
    :return: URI do objeto S3 carregado
    """
    # Se o S3 object_name não foi fornecido, use o file_name
    if object_name is None:
        object_name = file_name

    # Cria uma sessão S3
    session = boto3.session.Session(
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    s3_client = session.client('s3')

    try:
        # Faz o upload do arquivo
        s3_client.upload_file(file_name, bucket_name, object_name)
    except Exception as e:
        print(f"Alguma coisa deu errado: {e}")
        return None

    # Retorna a URI do arquivo no S3
    return f"s3://{bucket_name}/{object_name}"

def generate_and_upload_jsonl():
    file_name = 'chatbot_training.jsonl'
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    # Aqui chamamos a função de geração do arquivo que você implementará
    generate_training_data(file_name)

    s3_uri = upload_to_s3(file_name, bucket_name)

    response = train_model(s3_uri)
    fine_tune_id = response.id
    print(">>>>>>", response, fine_tune_id, sep='\n')

    if s3_uri:
        print(f"Arquivo enviado com sucesso. URI do S3: {s3_uri}")
        return s3_uri
    else:
        print("Falha ao enviar o arquivo para o S3.")
        return None
