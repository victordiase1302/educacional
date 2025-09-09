# exports.py
import json

import boto3
import openai
from chat.models import Training


def export_training_data_to_jsonl(filepath):
    with open(filepath, 'w') as f:
        for item in Training.objects.all():
            jsonl_content = json.dumps({"prompt": item.prompt, "completion": item.completion})
            f.write(jsonl_content + '\n')


def upload_to_s3(filepath, bucket, object_name):
    s3_client = boto3.client('s3')
    s3_client.upload_file(filepath, bucket, object_name)


def start_finetuning(training_file_url):
    openai.api_key = "your-openai-api-key"

    response = openai.FineTune.create(
        training_file=training_file_url,
        model="gpt-3.5-turbo", # Pode mudar dependendo do modelo disponível
        # Outros parâmetros como n_epochs podem ser definidos aqui
    )
    return response.id


def get_finetuning_status(finetune_id):
    openai.api_key = "your-openai-api-key"
    finetune = openai.FineTune.retrieve(id=finetune_id)
    return finetune.status
