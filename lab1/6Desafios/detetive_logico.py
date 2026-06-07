"""
╔══════════════════════════════════════════════════════╗
║           🔍  DETETIVE LÓGICO  🔍                    ║
║      Um jogo de dedução e raciocínio formal          ║
╚══════════════════════════════════════════════════════╝

Disciplina: Universo Computacional / Introdução à Programação
Desenvolvido com Python 3 — sem dependências externas
"""

import os
import sys
import time


# ─────────────────────────────────────────────
#  CORES (ANSI — funcionam no Linux, macOS e
#  no Windows 10+ com terminal moderno)
# ─────────────────────────────────────────────
class Cor:
    RESET     = "\033[0m"
    VERMELHO  = "\033[91m"
    VERDE     = "\033[92m"
    AMARELO   = "\033[93m"
    AZUL      = "\033[94m"
    MAGENTA   = "\033[95m"
    CIANO     = "\033[96m"
    BRANCO    = "\033[97m"
    NEGRITO   = "\033[1m"
    DIM       = "\033[2m"


# ─────────────────────────────────────────────
#  UTILITÁRIOS DE EXIBIÇÃO
# ─────────────────────────────────────────────
def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def digitar(texto, delay=0.025):
    """Efeito de máquina de escrever."""
    for char in texto:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def pausar(msg="Pressione Enter para continuar..."):
    input(f"\n{Cor.DIM}{msg}{Cor.RESET}")


def linha(char="═", largura=56):
    return char * largura


def cabecalho_caso(caso, total):
    cor = {1: Cor.VERDE, 2: Cor.AMARELO, 3: Cor.VERMELHO}.get(caso["id"], Cor.CIANO)
    print(f"\n{cor}{Cor.NEGRITO}{linha()}")
    print(f"  CASO {caso['id']}/{total}: {caso['titulo'].upper()}")
    print(f"  Dificuldade: {caso['dificuldade']}  |  Regra: {caso['regra']}")
    print(f"{linha()}{Cor.RESET}\n")


# ─────────────────────────────────────────────
#  BANCO DE CASOS
# ─────────────────────────────────────────────
CASOS = [
    # ── CASO 1 ──────────────────────────────
    {
        "id": 1,
        "titulo": "O Roubo na Biblioteca",
        "dificuldade": "Fácil ⭐",
        "regra": "Modus Ponens",
        "intro_regra": (
            "MODUS PONENS: Se (P → Q) e P é verdadeiro, então Q é verdadeiro.\n"
            "  Exemplo: 'Se usou a chave → entrou na sala' + 'Usou a chave' → 'Entrou na sala'."
        ),
        "narrativa": [
            "Um livro raro desapareceu da biblioteca da universidade na noite de sexta-feira.",
            "Você é o Detetive Lógico — seu trabalho é descobrir o culpado usando",
            "puras deduções, sem achismos.",
            "",
            "Três estudantes estavam no local na hora do crime:",
            "  → ANA, BRUNO e CARLOS.",
        ],
        "suspeitos": ["Ana", "Bruno", "Carlos"],
        "pistas": [
            {
                "n": 1,
                "tipo": "Condicional  (P → Q)",
                "texto": (
                    "A câmera de segurança registrou:\n"
                    "  'SE alguém usou a chave reserva,\n"
                    "   ENTÃO essa pessoa pegou o livro.'"
                ),
            },
            {
                "n": 2,
                "tipo": "Fato  (P é verdadeiro)",
                "texto": (
                    "O registro de acesso eletrônico mostra:\n"
                    "  ANA usou a chave reserva às 21h07."
                ),
            },
            {
                "n": 3,
                "tipo": "Eliminação por álibi",
                "texto": (
                    "O funcionário da cantina confirma:\n"
                    "  Bruno e Carlos estavam na cantina das 20h às 22h."
                ),
            },
        ],
        "resposta": "Ana",
        "explicacao": [
            "  P   = 'Alguém usou a chave reserva'",
            "  Q   = 'Essa pessoa pegou o livro'",
            "",
            "  Pista 1: P → Q  (se usou a chave, pegou o livro)",
            "  Pista 2: P é verdadeiro para ANA  (ela usou a chave)",
            "  ∴ Por MODUS PONENS: Q é verdadeiro → ANA pegou o livro.",
            "  Pista 3 elimina Bruno e Carlos por álibi — confirmação.",
        ],
    },

    # ── CASO 2 ──────────────────────────────
    {
        "id": 2,
        "titulo": "O Envenenamento no Jantar",
        "dificuldade": "Médio ⭐⭐",
        "regra": "Modus Tollens",
        "intro_regra": (
            "MODUS TOLLENS: Se (P → Q) e Q é FALSO, então P é FALSO.\n"
            "  Exemplo: 'Se preparou o prato → estava na cozinha' + 'Não estava na cozinha'\n"
            "           → 'Não preparou o prato'."
        ),
        "narrativa": [
            "Uma taça de vinho foi envenenada durante o jantar da família Silveira.",
            "O veneno exige acesso à cozinha antes das 20h para ser preparado.",
            "",
            "Três parentes estavam na mansão:",
            "  → DIANA, EDUARDO e FERNANDA.",
            "",
            "Desta vez você precisa raciocinar ao contrário: descarte quem",
            "NÃO pôde ser o culpado até sobrar um único suspeito.",
        ],
        "suspeitos": ["Diana", "Eduardo", "Fernanda"],
        "pistas": [
            {
                "n": 1,
                "tipo": "Condicional  (P → Q)",
                "texto": (
                    "O toxicologista afirma:\n"
                    "  'SE o veneno foi colocado antes das 20h,\n"
                    "   ENTÃO o culpado estava na cozinha antes das 20h.'"
                ),
            },
            {
                "n": 2,
                "tipo": "Negação do consequente  (¬Q para Eduardo)",
                "texto": (
                    "As câmeras registram:\n"
                    "  Eduardo chegou à mansão às 20h35.\n"
                    "  Logo, ele NÃO estava na cozinha antes das 20h."
                ),
            },
            {
                "n": 3,
                "tipo": "Negação do consequente  (¬Q para Diana)",
                "texto": (
                    "O GPS do carro de Diana mostra que ela estava\n"
                    "  a 120 km da mansão até às 19h50 — impossível chegar antes das 20h."
                ),
            },
            {
                "n": 4,
                "tipo": "Confirmação positiva",
                "texto": (
                    "O mordomo testemunha:\n"
                    "  Fernanda estava sozinha na cozinha das 19h30 às 19h55."
                ),
            },
        ],
        "resposta": "Fernanda",
        "explicacao": [
            "  P   = 'O culpado colocou o veneno antes das 20h'",
            "  Q   = 'O culpado estava na cozinha antes das 20h'",
            "",
            "  Pista 1: P → Q",
            "  Pista 2: ¬Q para Eduardo  →  Por MODUS TOLLENS: ¬P (Eduardo não é culpado).",
            "  Pista 3: ¬Q para Diana    →  Por MODUS TOLLENS: ¬P (Diana não é culpada).",
            "  Sobra apenas Fernanda — e a pista 4 confirma sua presença na cozinha.",
        ],
    },

    # ── CASO 3 ──────────────────────────────
    {
        "id": 3,
        "titulo": "O Sabotador do Torneio",
        "dificuldade": "Difícil ⭐⭐⭐",
        "regra": "Silogismo Hipotético",
        "intro_regra": (
            "SILOGISMO HIPOTÉTICO: Se (P → Q) e (Q → R), então (P → R).\n"
            "  Você encadeia duas condicionais para chegar a uma conclusão mais distante."
        ),
        "narrativa": [
            "O servidor do torneio universitário de programação foi invadido",
            "horas antes da final, e os dados foram corrompidos.",
            "",
            "Três competidores tinham credenciais de acesso ao servidor:",
            "  → GABRIEL, HELENA e IGOR.",
            "",
            "Este caso exige encadear múltiplas inferências —",
            "cada pista é uma peça de um silogismo maior.",
        ],
        "suspeitos": ["Gabriel", "Helena", "Igor"],
        "pistas": [
            {
                "n": 1,
                "tipo": "Condicional  (P → Q)",
                "texto": (
                    "O perito forense digital afirma:\n"
                    "  'SE o invasor conhecia a vulnerabilidade do servidor,\n"
                    "   ENTÃO ele usou a VPN interna da universidade para agir.'"
                ),
            },
            {
                "n": 2,
                "tipo": "Condicional  (Q → R)",
                "texto": (
                    "Os logs de rede mostram:\n"
                    "  'SE alguém usou a VPN interna da universidade,\n"
                    "   ENTÃO o acesso partiu de dentro do campus.'"
                ),
            },
            {
                "n": 3,
                "tipo": "Silogismo Hipotético  (P → R)",
                "texto": (
                    "Encadeando as pistas 1 e 2:\n"
                    "  'Quem conhecia a vulnerabilidade, acessou de dentro do campus.'\n"
                    "  (Essa é a conclusão do Silogismo — use-a para filtrar os suspeitos!)"
                ),
            },
            {
                "n": 4,
                "tipo": "Eliminações",
                "texto": (
                    "• Gabriel embarcou para uma conferência em São Paulo na manhã do ataque\n"
                    "  — comprovado por cartão de embarque.\n"
                    "• Igor usou uma VPN *externa* rastreada ao endereço IP da casa dele."
                ),
            },
            {
                "n": 5,
                "tipo": "Confirmação final  (P ∧ R verdadeiros)",
                "texto": (
                    "A coordenadora do laboratório confirma:\n"
                    "  Helena participou da equipe que descobriu a vulnerabilidade.\n"
                    "  E o registro de entrada mostra que ela estava no campus no horário."
                ),
            },
        ],
        "resposta": "Helena",
        "explicacao": [
            "  P   = 'Conhecia a vulnerabilidade do servidor'",
            "  Q   = 'Usou a VPN interna da universidade'",
            "  R   = 'Acessou de dentro do campus'",
            "",
            "  Pista 1: P → Q",
            "  Pista 2: Q → R",
            "  ∴ Por SILOGISMO HIPOTÉTICO: P → R",
            "",
            "  Pista 4: Gabriel estava fora da cidade (¬R) → não pôde agir.",
            "           Igor usou VPN externa (¬Q) → não satisfaz a cadeia.",
            "  Pista 5: Helena satisfaz P (conhecia a vulnerabilidade) e R (estava no campus).",
            "  ∴ HELENA é a sabotadora.",
        ],
    },
]


# ─────────────────────────────────────────────
#  TELA INICIAL
# ─────────────────────────────────────────────
def tela_inicial():
    limpar()
    print(f"""
{Cor.CIANO}{Cor.NEGRITO}
  ╔══════════════════════════════════════════════════════╗
  ║           🔍  DETETIVE LÓGICO  🔍                    ║
  ║      Um jogo de dedução e raciocínio formal          ║
  ╚══════════════════════════════════════════════════════╝
{Cor.RESET}""")


# ─────────────────────────────────────────────
#  COMO JOGAR
# ─────────────────────────────────────────────
def como_jogar():
    limpar()
    tela_inicial()
    print(f"{Cor.CIANO}{Cor.NEGRITO}📖  REGRAS DE INFERÊNCIA DO JOGO{Cor.RESET}\n")

    regras = [
        (
            "1. Modus Ponens",
            "Se (P → Q) e P é verdadeiro → Q é verdadeiro.",
            "Se estuda → passa.  + Está estudando.  → Vai passar.",
        ),
        (
            "2. Modus Tollens",
            "Se (P → Q) e Q é falso → P é falso.",
            "Se estuda → passa.  + Não passou.  → Não estudou.",
        ),
        (
            "3. Silogismo Hipotético",
            "Se (P → Q) e (Q → R) → (P → R).",
            "Se estuda → passa.  + Se passa → se forma.  → Se estuda → se forma.",
        ),
    ]

    for nome, regra, exemplo in regras:
        print(f"  {Cor.AMARELO}{Cor.NEGRITO}{nome}{Cor.RESET}")
        print(f"    {regra}")
        print(f"    {Cor.VERDE}Ex: {exemplo}{Cor.RESET}\n")

    print(f"  {Cor.DIM}Em cada caso você receberá pistas na forma de proposições.")
    print(f"  Aplique a regra correta e deduza o culpado!{Cor.RESET}")
    pausar()


# ─────────────────────────────────────────────
#  JOGO DE UM CASO
# ─────────────────────────────────────────────
def jogar_caso(caso, total) -> bool:
    limpar()
    tela_inicial()
    cabecalho_caso(caso, total)

    # Regra do caso
    print(f"{Cor.DIM}Regra em uso neste caso:{Cor.RESET}")
    for ln in caso["intro_regra"].splitlines():
        print(f"  {Cor.DIM}{ln}{Cor.RESET}")

    pausar("Pressione Enter para ler a narrativa...")

    # Narrativa
    limpar()
    tela_inicial()
    cabecalho_caso(caso, total)
    print(f"{Cor.CIANO}{Cor.NEGRITO}📜  NARRATIVA:{Cor.RESET}\n")
    for linha_texto in caso["narrativa"]:
        digitar(f"  {linha_texto}", delay=0.022)
        if linha_texto == "":
            time.sleep(0.15)

    print(f"\n{Cor.AMARELO}{Cor.NEGRITO}🕵️  SUSPEITOS:{Cor.RESET}")
    for i, s in enumerate(caso["suspeitos"], 1):
        print(f"  {i}. {s}")

    pausar("Pressione Enter para investigar as pistas...")

    # Pistas — uma por vez
    for pista in caso["pistas"]:
        limpar()
        tela_inicial()
        cabecalho_caso(caso, total)
        print(f"{Cor.CIANO}{Cor.NEGRITO}🔎  PISTA {pista['n']} de {len(caso['pistas'])}:{Cor.RESET}")
        print(f"    {Cor.AMARELO}[{pista['tipo']}]{Cor.RESET}\n")
        for ln in pista["texto"].splitlines():
            digitar(f"  {ln}", delay=0.022)
        pausar()

    # Decisão
    limpar()
    tela_inicial()
    cabecalho_caso(caso, total)
    print(f"{Cor.NEGRITO}Com base nas pistas e na lógica formal — quem é o culpado?\n{Cor.RESET}")
    for i, s in enumerate(caso["suspeitos"], 1):
        print(f"  {Cor.AMARELO}[{i}]{Cor.RESET}  {s}")

    while True:
        escolha = input("\n  Sua dedução (1, 2 ou 3): ").strip()
        if escolha in ("1", "2", "3"):
            escolhido = caso["suspeitos"][int(escolha) - 1]
            break
        print(f"  {Cor.VERMELHO}Digite apenas 1, 2 ou 3.{Cor.RESET}")

    # Resultado
    print(f"\n{linha('─')}")
    acertou = escolhido == caso["resposta"]

    if acertou:
        print(f"\n{Cor.VERDE}{Cor.NEGRITO}  ✅  CORRETO! {escolhido} é o culpado!{Cor.RESET}")
    else:
        print(f"\n{Cor.VERMELHO}{Cor.NEGRITO}  ❌  Incorreto. O culpado era {caso['resposta']}.{Cor.RESET}")

    print(f"\n{Cor.CIANO}📐  EXPLICAÇÃO — {caso['regra']}:{Cor.RESET}")
    for ln in caso["explicacao"]:
        print(f"{ln}")

    pausar()
    return acertou


# ─────────────────────────────────────────────
#  MENU PRINCIPAL
# ─────────────────────────────────────────────
def menu():
    total = len(CASOS)

    while True:
        tela_inicial()
        print(f"  {Cor.NEGRITO}Bem-vindo, Detetive!{Cor.RESET}")
        print(
            "\n  Cada caso testa uma regra de inferência diferente.\n"
            "  Leia as pistas com atenção e use a lógica para resolver o mistério.\n"
        )
        print(f"  {Cor.AMARELO}[1]{Cor.RESET}  Jogar todos os casos (sequência completa)")
        print(f"  {Cor.AMARELO}[2]{Cor.RESET}  Escolher um caso específico")
        print(f"  {Cor.AMARELO}[3]{Cor.RESET}  Como jogar / Regras de inferência")
        print(f"  {Cor.AMARELO}[4]{Cor.RESET}  Sair\n")

        opcao = input("  Sua escolha: ").strip()

        # ── Jogar todos ─────────────────────
        if opcao == "1":
            pontos = 0
            for caso in CASOS:
                if jogar_caso(caso, total):
                    pontos += 1

            limpar()
            tela_inicial()
            print(f"\n  {Cor.NEGRITO}🏁  RESULTADO FINAL{Cor.RESET}\n")
            print(f"  Casos resolvidos corretamente: "
                  f"{Cor.VERDE}{pontos}{Cor.RESET} / {total}\n")

            if pontos == total:
                print(f"  {Cor.VERDE}{Cor.NEGRITO}  🏆  Perfeito! Você domina o raciocínio lógico!{Cor.RESET}")
            elif pontos >= 2:
                print(f"  {Cor.AMARELO}  🔍  Bom trabalho! Revise os casos que errou.{Cor.RESET}")
            else:
                print(f"  {Cor.VERMELHO}  📚  Releia as regras de inferência e tente de novo!{Cor.RESET}")

            pausar("Pressione Enter para voltar ao menu...")

        # ── Escolher caso ────────────────────
        elif opcao == "2":
            limpar()
            tela_inicial()
            print(f"  {Cor.CIANO}Escolha um caso:{Cor.RESET}\n")
            for c in CASOS:
                print(f"  [{c['id']}]  {c['titulo']}  —  {c['dificuldade']}  ({c['regra']})")

            escolha = input("\n  Número do caso: ").strip()
            encontrado = False
            for c in CASOS:
                if str(c["id"]) == escolha:
                    jogar_caso(c, total)
                    encontrado = True
                    break
            if not encontrado:
                print(f"\n  {Cor.VERMELHO}Caso inválido.{Cor.RESET}")
                time.sleep(1.2)

        # ── Como jogar ───────────────────────
        elif opcao == "3":
            como_jogar()

        # ── Sair ─────────────────────────────
        elif opcao == "4":
            limpar()
            print(f"\n  {Cor.CIANO}Até logo, Detetive! Continue raciocinando. 🔍\n{Cor.RESET}")
            sys.exit(0)

        else:
            print(f"\n  {Cor.VERMELHO}Opção inválida. Tente novamente.{Cor.RESET}")
            time.sleep(1)


# ─────────────────────────────────────────────
#  PONTO DE ENTRADA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Habilita cores ANSI no Windows (necessário em algumas versões)
    if os.name == "nt":
        os.system("color")
    menu()