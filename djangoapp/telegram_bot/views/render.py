import re

import matplotlib.pyplot as plt


def create_image_with_text_and_formulas(text, formulas):
    # Criar uma figura com fundo branco
    fig, ax = plt.subplots(figsize=(200, 180))  # Tamanho da figura em polegadas
    ax.axis("off")  # Desativar os eixos

    # Adicionar texto e fórmulas na imagem
    ax.text(0.05, 0.95, text, fontsize=12, ha="left", va="top", wrap=True)

    # Posições iniciais para as fórmulas
    formula_y = 0.8
    for formula in formulas:
        ax.text(0.05, formula_y, f"${formula}$", fontsize=14, ha="left", va="top")
        formula_y -= 0.15  # Ajustar o espaçamento vertical para a próxima fórmula

    plt.savefig("full_message3.png")
    plt.close(fig)


text = "O modelo ARIMA, que significa AutoRegressive Integrated Moving Average, é uma ferramenta estatística usada para análise e previsão de séries temporais. O modelo ARIMA é descrito por três parâmetros: (p, d, q)."



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
    formula_pattern = r"(\$\$.*?\$\$|\$.*?\$|\\\[.*?\\\]|\\\(.*?\\\))"
    formulas = re.findall(formula_pattern, text, flags=re.DOTALL)
    clean_text = re.sub(formula_pattern, "", text, flags=re.DOTALL)
    # print(clean_text,' - ' *30 ,formulas, sep="\n")
    return clean_text, formulas


def clean_formula(formula):
    # Remover os delimitadores LaTeX
    formula = re.sub(r"\\[()\\[\]]", "", formula).strip()
    return formula


def convert_formulas(formulas):
    descriptions = {
        "p": "p: \\text{Ordem do componente autoregressivo (AR)}.",
        "d": "d: \\text{Grau de diferenciação necessário para tornar a série estacionária}.",
        "q": "q: \\text{Ordem do componente de médias móveis (MA)}.",
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
create_image_with_text_and_formulas(clean_text, converted_formulas)
[
    "p: \\text{Ordem do componente autoregressivo (AR)}.",
    "d: \\text{Grau de diferenciação necessário para tornar a série estacionária}.",
    "q: \\text{Ordem do componente de médias móveis (MA)}.",
    "d: \\text{Grau de diferenciação necessário para tornar a série estacionária}.",
    "Y_t",
    "d: \\text{Grau de diferenciação necessário para tornar a série estacionária}.",
    "Y'_t",
    "abla",
    "abla Y_t = Y_t - Y_{t-1}",
    "Y'_t",
    "Y'_t = c + \\phi_1 Y'_{t-1} + \\phi_2 Y'_{t-2} + \\dots + \\phi_p Y'_{t-p} + \theta_1 \\epsilon_{t-1} + \theta_2 \\epsilon_{t-2} + \\dots + \theta_q \\epsilon_{t-q} + \\epsilon_t",
    "c",
    "\\phi_1, \\phi_2, \\dots, \\phi_p",
    "heta_1, \theta_2, \\dots, \theta_q",
    "\\epsilon_t",
    "t",
]
formulas = [
    "p: \\text{Ordem do componente autoregressivo (AR)}.",
    "d: \\text{Grau de diferenciação necessário para tornar a série estacionária}.",
    "q: \\text{Ordem do componente de médias móveis (MA)}.",
    "\\nabla Y_t = Y_t - Y_{t-1}",
    "Y'_t = c + \\phi_1 Y'_{t-1} + \\phi_2 Y'_{t-2} + \\dots + \\phi_p Y'_{t-p} + \\theta_1 \\epsilon_{t-1} + \\theta_2 \\epsilon_{t-2} + \\dots + \\theta_q \\epsilon_{t-q} + \\epsilon_t",
]
