import boto3
from core.models import EbookDownload
from django.conf import settings
from django.http import StreamingHttpResponse


def download_file(request, *args, **kwargs):
    # Cria o cliente do S3
    file_key = "GUIA_DE_ATIVIDADES_[INSPIRARPROFESSORES].pdf"
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION_NAME,
    )

    # Pega o arquivo do S3
    file_obj = s3_client.get_object(
        Bucket="econometriafacil",
        Key=file_key,
    )

    EbookDownload.objects.create(
        title=file_key,
        ip_address=request.META.get("REMOTE_ADDR"),
        user_agent=request.META.get("HTTP_USER_AGENT"),
    )

    # Retorna como resposta de streaming para o download
    response = StreamingHttpResponse(file_obj["Body"].iter_chunks())
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename={file_key.split("/")[-1]}'

    return response
