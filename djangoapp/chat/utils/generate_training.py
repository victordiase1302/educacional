# Exporta o dataset de treinamento para um arquivo JSONL.
import json

from chat.models import Training


def generate_training_data(filename='chatbot_training.jsonl'):
    with open(filename, 'w') as f:
        for entry in Training.objects.all():
            record = {"prompt": entry.prompt, "completion": entry.completion}
            f.write(json.dumps(record) + '\n')
