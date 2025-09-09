def format_numbers(query_dict):
    digit = ''
    cell_phone = ''

    for chave, valor in query_dict.items():
        if chave.startswith('digit-'):
            digit += valor

        elif chave == 'cell_phone':
            cell_phone = valor

    return digit, cell_phone
