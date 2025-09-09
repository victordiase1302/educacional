import json
import os
from datetime import datetime

FILE_NAME = "user_data.json"


# Função para criar um arquivo JSON vazio se não existir
def create_file_if_not_exists(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump({}, file)


# Função para ler dados do arquivo JSON
def read_json(file_name):
    with open(file_name, "r") as file:
        return json.load(file)


# Função para escrever dados no arquivo JSON
def write_json(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


# Função para atualizar ou adicionar um novo usuário
def update_or_add_user(file_name, user_id, user_name, thread_id):
    data = read_json(file_name)
    if user_id in data:
        return data[user_id]["thread_id"]
    else:
        data[user_id] = {"user_name": user_name, "thread_id": thread_id}
        write_json(file_name, data)
        return thread_id


def operation_in_file(client):
    # create_file_if_not_exists(FILE_NAME)
    # data = read_json(FILE_NAME)
    # if str(user_id) in data:
    #     thread_id = data[str(user_id)]['thread_id']
    # else:
    #     # Criar nova thread
    #     thread = client.beta.threads.create()
    #     thread_id = thread.id

    #     # Adicionar novo usuário ao JSON
    #     data[str(user_id)] = {
    #         'user_name': name,
    #         'thread_id': thread_id,
    #         'date': msg_date.isoformat(),
    #         'type': message_type,
    #     }
    #     write_json(FILE_NAME, data)
    thread = client.beta.threads.create()
    thread_id = thread.id
    return thread_id
