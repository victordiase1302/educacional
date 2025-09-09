import re

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["text.usetex"] = True
matplotlib.rcParams["text.latex.preamble"] = (
    r"\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{amsmath}"
)

api_text = r"""
    Para analisar o impacto de desastres naturais na quantidade de transações PIX, você pode usar um modelo de estudo de eventos com diferenças em diferenças (DiD). Este modelo permite comparar a evolução das transações PIX em áreas afetadas por desastres naturais com áreas que não foram afetadas, antes e depois do evento. Aqui está uma proposta de modelo econométrico para essa análise:

### Modelo Econométrico

Considere a seguinte equação de regressão para o modelo DiD:

\[ Y_{it} = \beta_0 + \beta_1 Post_t + \beta_2 Treated_i + \beta_3 (Post_t \times Treated_i) + \gamma X_{it} + \delta_t + \mu_i + \epsilon_{it} \]

onde:
- \( Y_{it} \) é a quantidade de transações PIX na região \( i \) no tempo \( t \).
- \( Post_t \) é uma variável dummy que assume valor 1 para todos os períodos após o desastre e 0 antes.
- \( Treated_i \) é uma variável dummy que assume valor 1 para regiões afetadas pelo desastre (tratadas) e 0 para regiões não afetadas (controle).
- \( Post_t \times Treated_i \) é o termo de interação entre o pós-evento e as regiões tratadas, capturando o efeito diferencial do desastre sobre as transações PIX nas regiões afetadas em comparação com as não afetadas.
- \( X_{it} \) é um vetor de covariáveis que podem incluir outras variáveis que influenciam as transações PIX, como atividade econômica local, população da região, infraestrutura de internet, etc.
- \( \delta_t \) são efeitos fixos de tempo que capturam fatores macroeconômicos e outras tendências temporais que afetam todas as regiões igualmente.
- \( \mu_i \) são efeitos fixos de região que capturam características não observadas das regiões que não variam no tempo.
- \( \epsilon_{it} \) é o termo de erro.

### Considerações Adicionais

1. **Seleção de Período**: É crucial definir adequadamente o período de estudo, incluindo um período suficiente antes e depois do desastre para capturar as tendências pré e pós-evento.

2. **Robustez dos Resultados**: Verifique a robustez dos resultados usando diferentes especificações do modelo, como variando o período de controle ou incluindo interações adicionais.

3. **Verificação de Hipóteses**: Certifique-se de que as hipóteses-chave do modelo DiD sejam satisfeitas, incluindo a hipótese de que as tendências pré-evento nas regiões tratadas e não tratadas seriam paralelas na ausência do desastre.

4. **Análise de Sensibilidade**: Realize testes de sensibilidade, como excluir regiões específicas ou alterar a definição de regiões tratadas e controle.

5. **Controle de Variáveis Confundidoras**: Inclua variáveis de controle que possam afetar tanto a probabilidade de um desastre quanto o volume de transações PIX.

Este modelo proporcionará insights valiosos sobre como os desastres naturais afetam a atividade econômica medida através das transações PIX, controlando por outros fatores que podem influenciar essas transações.
"""


def prepare_text_for_latex(text):
    # Substitui cabeçalhos markdown por comandos LaTeX
    text = text.replace("### ", "\\textbf{")  # Transforma markdown headers em negrito
    # Fecha o negrito no fim de cada linha iniciada por '###'
    return text


def add_line_breaks(text):
    # Adiciona uma quebra de linha após cada ponto final, a menos que já haja uma quebra de linha
    new_text = ""
    for part in text.split("."):
        if part:
            # Evita adicionar uma quebra de linha extra se já termina com uma
            if part[-1] != "\n":
                new_text += part.strip() + ".\n"
            else:
                new_text += part.strip() + "."
        else:
            new_text += part
    return new_text.strip()


def calculate_figsize(text):
    lines = text.split("\n")  # Contar quebras de linha para estimar o número de linhas
    max_line_length = max(len(line) for line in lines)
    width = max(
        27, min(max_line_length * 0.1, 20)
    )  # Ajustar a largura com base no comprimento da linha mais longa
    height = max(9, len(lines) * 0.6)  # Ajustar a altura com base no número de linhas
    return (width, height)


def create_image_with_text_and_formulas(text, formulas):
    # Criar uma figura com fundo branco
    text = add_line_breaks(text)
    figsize = calculate_figsize(text)
    fig, ax = plt.subplots(figsize=figsize)  # Tamanho da figura em polegadas
    ax.axis("off")  # Desativar os eixos
    formatted_text = prepare_text_for_latex(text)

    for i, formula in enumerate(formulas):
        formula = formula.replace("\\dots", "\dots")
        formula = formula.replace("\a", "\\a")
        formula = formula.replace("\t", "\\t")
        formula = formula.replace("\\\\", "\\")

        placeholder = f"(formula_{i})"
        formatted_text = formatted_text.replace(
            placeholder,
            f" ${formula.strip()}$ ",
        )

    ax.text(
        -0.10,
        0.85,
        formatted_text,
        fontsize=22,
        ha="left",
        va="top",
        wrap=False,
    )

    # Calcular posição inicial para as fórmulas baseada na extensão do texto
    # renderer = fig.canvas.get_renderer()
    # bbox = text_obj.get_window_extent(renderer=renderer)
    # formula_y = bbox.y0 / fig.dpi / fig.get_size_inches()[1] - 0.01
    # formula_y = 0.85
    # Adicionar fórmulas na imagem
    # for formula in formulas:
    #     formula = formula.replace("\\dots", "\dots")
    #     formula = formula.replace("abla", "\\nabla")
    #     formula = formula.replace("\t", "\\t")
    #     formula = formula.replace("\\\\", "\\")
    #     ax.text(
    #         0.05,
    #         formula_y,
    #         f" $ {formula.strip()} $ ",
    #         fontsize=14,
    #         ha="left",
    #         va="top",
    #     )
    #     formula_y -= 0.02
    # Ajustar o espaçamento vertical para a próxima fórmula

    plt.savefig("full_message6.png")
    plt.close(fig)


def extrair_formulas_e_texto(texto):
    # Expressão regular para capturar fórmulas LaTeX corretamente
    padrao_formula = r"\\\[\s*.*?\s*\\\]|\s*\\\(\s*.*?\s*\\\)\s*"

    # Encontrar todas as fórmulas usando a regex
    formulas = re.findall(padrao_formula, texto, re.DOTALL)

    # Limpar as fórmulas removendo os delimitadores LaTeX
    formulas_limpa = [f.strip()[2:-2] for f in formulas]

    # Substituir as fórmulas por marcadores placeholders e criar um mapeamento
    def substituicao_por_marcador(match):
        # Crie um marcador baseado no índice da fórmula capturada
        index = formulas.index(match.group(0))
        return f" (formula_{index}) "

    # Realiza a substituição no texto original usando a função de substituição
    texto_limpo = re.sub(padrao_formula, substituicao_por_marcador, texto)

    return texto_limpo.strip(), formulas_limpa


texto_simples, formulas = extrair_formulas_e_texto(api_text)
# print("Texto Simples:\n", texto_simples)
print("Formulas:\n", formulas)
create_image_with_text_and_formulas(texto_simples, formulas)
