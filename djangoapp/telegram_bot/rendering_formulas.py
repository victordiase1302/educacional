import io
import re

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["text.usetex"] = True
matplotlib.rcParams["text.latex.preamble"] = (
    r"\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{lmodern}\usepackage{amsmath}"
)


def prepare_text_for_latex(text):
    # Substitui cabeçalhos markdown por comandos LaTeX
    text = text.replace("### ", "\\textbf{")  # Transforma markdown headers em negrito
    # Fecha o negrito no fim de cada linha iniciada por '###'
    return text


def replace_unicode_with_latex(text):
    """
    Substitui caracteres Unicode comuns por seus equivalentes LaTeX.
    """
    replacements = {
        "µ": r"\\mu",
        "σ": r"\\sigma",
        "°": r"^\\circ",
        "²": r"^2",
        "³": r"^3",
        "α": r"\\alpha",
        "β": r"\\beta",
        "γ": r"\\gamma",
        "Δ": r"\\Delta",
        "δ": r"\\delta",
        "ε": r"\\epsilon",
        "θ": r"\\theta",
        "λ": r"\\lambda",
        "π": r"\\pi",
        "φ": r"\\phi",
        "ω": r"\\omega",
        "Ω": r"\\Omega",
        "∑": r"\\sum",
        "∫": r"\\int",
        "√": r"\\sqrt",
        "∞": r"\\infty",
        "≈": r"\\approx",
        "≠": r"\\neq",
        "≤": r"\\leq",
        "≥": r"\\geq",
        "×": r"\\times",
        "÷": r"\\div",
        "±": r"\\pm",
        "→": r"\\rightarrow",
        "←": r"\\leftarrow",
        "⇔": r"\\Leftrightarrow",
        "∈": r"\\in",
        "∉": r"\\notin",
        "⊂": r"\\subset",
        "⊃": r"\\supset",
        "∪": r"\\cup",
        "∩": r"\\cap",
        "∀": r"\\forall",
        "∃": r"\\exists",
        "∧": r"\\land",
        "∨": r"\\lor",
        "¬": r"\\neg",
        "ρ": r"\\rho",
        "τ": r"\\tau",
        "κ": r"\\kappa",
        "Φ": r"\\Phi",
        "Ψ": r"\\Psi",
        "Σ": r"\\Sigma",
        "½": r"\\frac{1}{2}",
        "⅓": r"\\frac{1}{3}",
        "¼": r"\\frac{1}{4}",
        "⅛": r"\\frac{1}{8}",
        "∂": r"\\partial",
        "∆": r"\\Delta",
        "ℵ": r"\\aleph",
        "ℓ": r"\\ell",
        "ℜ": r"\\Re",
        "ℑ": r"\\Im",
    }

    for unicode_char, latex_char in replacements.items():
        text = re.sub(rf"\b{unicode_char}\b", rf"${latex_char}$", text)

    return text


def add_line_breaks(text, max_line_length=70):
    # Adiciona uma quebra de linha após cada ponto final, a menos que já haja uma quebra de linha
    new_text = ""
    current_line = ""
    for part in text.split(" "):
        if len(current_line) + len(part) + 1 > max_line_length:
            # Se a linha atual mais a próxima palavra ultrapassarem o limite, quebra a linha
            new_text += current_line.strip() + "\n"
            current_line = part + " "  # A palavra vai para a nova linha
        else:
            current_line += part + " "  # Adiciona a palavra à linha atual

        # Quebra a linha após o ponto final
        if part.endswith(".") and len(current_line.strip()) > 0:
            new_text += current_line.strip() + "\n"
            current_line = ""

    # Adiciona o que sobrar no `current_line`
    if current_line.strip():
        new_text += current_line.strip()

    return new_text.strip()


def calculate_figsize(text):
    lines = text.split("\n")  # Contar quebras de linha para estimar o número de linhas
    max_line_length = max(len(line) for line in lines)
    width = max(5, min(max_line_length * 0.1, 15))
    height = max(3, len(lines) * 0.6)  # Ajustar a altura com base no número de linhas
    return (width, height)


def create_image_with_text_and_formulas(text, formulas, name_path):
    text = add_line_breaks(text)
    text = replace_unicode_with_latex(text)
    figsize = calculate_figsize(text)
    fig, ax = plt.subplots(figsize=figsize)
    ax.axis("off")  # Desativar os eixos
    formatted_text = prepare_text_for_latex(text)

    for i, formula in enumerate(formulas):
        formula = formula.replace("\\dots", "\dots")
        formula = formula.replace("\a", "\\a")
        formula = formula.replace("&", "\\&")
        formula = formula.replace("\t", "\\t")
        # formula = formula.replace("\\\\", "\\")

        placeholder = f"(formula_{i})"
        formatted_text = formatted_text.replace(
            placeholder,
            f" ${formula.strip()}$ ",
        )

    # for i, line in enumerate(formatted_text.split("\n")):
    #     ax.text(
    #         0,
    #         1 - (i * 0.5),
    #         line,
    #         fontsize=48,
    #         ha="left",
    #         va="top",
    #         wrap=True,
    #     )
    ax.text(
        0,
        1.5,
        formatted_text,
        fontsize=48,
        va="top",
        ha="left",
        wrap=False,
    )
    buffer = io.BytesIO()
    plt.savefig(
        name_path,
        bbox_inches="tight",
        pad_inches=0.7,
    )
    plt.savefig(
        buffer,
        format="png",
        bbox_inches="tight",
        pad_inches=0.7,
    )
    buffer.seek(0)
    plt.close(fig)
    return buffer


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


def main(api_text, msg_id):
    raw_text = rf"""{api_text}"""
    # print(raw_text)
    texto_simples, formulas = extrair_formulas_e_texto(raw_text)
    resp_img = None
    resp_txt = None
    # print("Formulas:\n", formulas)
    if formulas:
        name_path = f"./images/{msg_id}.png"
        resp_img = create_image_with_text_and_formulas(
            texto_simples,
            formulas,
            name_path,
        )
    else:
        resp_txt = api_text
    return resp_img, resp_txt
