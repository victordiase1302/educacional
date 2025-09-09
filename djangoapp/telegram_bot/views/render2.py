import re

import matplotlib.pyplot as plt

# Exemplo de texto da API, com correções para qualquer caracter problemático
api_text = """
O modelo ARIMA, que significa AutoRegressive Integrated Moving Average, é uma ferramenta estatística usada para análise e previsão de séries temporais. O modelo ARIMA é descrito por três parâmetros: (p, d, q). Aqui está uma explicação de cada um desses parâmetros:

- \( p \): Ordem do componente autoregressivo (AR).
- \( d \): Grau de diferenciação necessário para tornar a série estacionária.
- \( q \): Ordem do componente de médias móveis (MA).

A fórmula genérica para um modelo ARIMA(p, d, q) pode ser expressa da seguinte maneira:

1. **Diferenciação**: Primeiro, se \( d \) é maior que zero, a série original \( Y_t \) é diferenciada \( d \) vezes para obter uma nova série \( Y'_t \) que é estacionária. Isso é feito usando o operador de diferenciação \( \nabla \), onde:

   \[
   \nabla Y_t = Y_t - Y_{t-1}
   \]

2. **Modelo ARIMA**: Após a diferenciação, aplicamos o modelo ARIMA à série diferenciada \( Y'_t \). A equação do modelo ARIMA é:

   \[
   Y'_t = c + \phi_1 Y'_{t-1} + \phi_2 Y'_{t-2} + \dots + \phi_p Y'_{t-p} + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \dots + \theta_q \epsilon_{t-q} + \epsilon_t
   \]

   onde:
   - \( c \) é uma constante.
   - \( \phi_1, \phi_2, \dots, \phi_p \) são os coeficientes para o componente autoregressivo.
   - \( \theta_1, \theta_2, \dots, \theta_q \) são os coeficientes para o componente de médias móveis.
   - \( \epsilon_t \) é o termo de erro no tempo \( t \).
"""

def extract_formulas(text):
    # Regex para encontrar fórmulas LaTeX
    formula_pattern = r'(\$\$.*?\$\$|\$.*?\$|\\\[.*?\\\]|\\\(.*?\\\))'
    formulas = re.findall(formula_pattern, text, flags=re.DOTALL)
    clean_text = re.sub(formula_pattern, "___FORMULA___", text, flags=re.DOTALL)
    # print(clean_text,' - ' *30 ,formulas, sep="\n")
    return clean_text, formulas

def render_image(text, formulas):
    # plt.rc('text', usetex=False)
    # plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

    fig, ax = plt.subplots(figsize=(12, 10))
    ax.axis('off')

    y_pos = 0.95
    formula_index = 0

    # Iterar por cada linha e verificar se contém marcador de fórmula
    for line in text.split('\n'):
        if "___FORMULA___" in line:
            while "___FORMULA___" in line:
                before, _, after = line.partition("___FORMULA___")
                ax.text(0.05, y_pos, before, fontsize=12, ha='left', va='top', wrap=True)
                line = after
                if formula_index < len(formulas):
                    ax.text(0.05, y_pos, formulas[formula_index], fontsize=12, color='blue', ha='left', va='top')
                    formula_index += 1
                y_pos -= 0.05
        ax.text(0.05, y_pos, line, fontsize=12, ha='left', va='top', wrap=True)
        y_pos -= 0.05 * len(line.split()) / 10  # Ajustar espaço baseado no número de palavras

    plt.savefig('full_message_image.png')
    plt.close(fig)

def clean_formula(formula):
    # Remover os delimitadores LaTeX
    formula = re.sub(r'\\[()\\[\]]', '', formula).strip()
    return formula

def convert_formulas(formulas):
    descriptions = {
        'p': 'p: \\text{Ordem do componente autoregressivo (AR)}.',
        'd': 'd: \\text{Grau de diferenciação necessário para tornar a série estacionária}.',
        'q': 'q: \\text{Ordem do componente de médias móveis (MA)}.',
    }
    converted = []
    for formula in formulas:
        cleaned = clean_formula(formula)
        # print(cleaned)
        if cleaned in descriptions:
            converted.append(descriptions[cleaned])
        else:
            converted.append(cleaned)
    return converted

clean_text, extracted_formulas = extract_formulas(api_text)
converted_formulas = convert_formulas(extracted_formulas)
print(converted_formulas)
render_image(clean_text, converted_formulas)
