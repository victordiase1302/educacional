from django.conf import settings
from openai import OpenAI


def train_model(training_file):
    client = OpenAI(api_key=settings.OPENAI_KEY)
    response = client.files.create(
        file=open("chatbot_training.jsonl", "rb"),
        purpose="fine-tune"
    )
    print(response)
    return response

def list_models():
    client = OpenAI(api_key=settings.OPENAI_KEY)
    response = client.fine_tunes.list()
    print('response>>>>', response, sep='\n')
    for modelo in response.data:
        print(modelo)
    return response

# def train_model(training_file):
#     client = OpenAI(api_key=settings.OPENAI_KEY)
#     response = client.fine_tuning.jobs.create(
#         training_file=training_file, # URL do seu arquivo JSONL
#         model="gpt-3.5-turbo-1106", # Modelo base a ser finetuned. Substitua se necessário.
#         # Você pode definir outros parâmetros aqui conforme necessário.
#     )
#     return response

# Substitua 'path_to_your_jsonl_file' pelo caminho do seu arquivo de treinamento
# training_file_url = "s3://path_to_your_bucket/path_to_your_jsonl_file.jsonl"
# response = train_model(training_file_url)
# print(response)


# fine_tune_id = response["id"]  # Adquira o ID do processo de finetuning da resposta

# Verificar o status do finetuning:
# status_response = openai.FineTune.retrieve(id=fine_tune_id)
# print(status_response)
