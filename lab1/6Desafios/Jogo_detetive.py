'''
Jogo de detetive 
'''

# impotando as bibliotecas 

import os
import time

# cores do jogo 

class Cor:
    RESET   = "\033[0m"
    VERDE   = "\033[92m"
    AMARELO = "\033[93m"
    VERMELHO= "\033[91m"
    CIANO   = "\033[96m"
    NEGRITO = "\033[1m"
    DIM     = "\033[2m"


# Definindo funções necessarias para apoio

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def digitar(texto, velocidade=0.025):
    """Imprime o texto letra por letra, como máquina de escrever."""
    for letra in texto:
        print(letra, end="", flush=True)  # flush=True exibe imediatamente
        time.sleep(velocidade)
    print()  # quebra de linha ao final

def pausa(): #espera o jogador apertar Enter
    input(f"\n{Cor.DIM} Precione enter para continuar...{Cor.RESET}\n")

def titulo(texto, cor=Cor.CIANO): # formatação visual com cores ANSI
    print(f"\n{cor}{Cor.NEGRITO}{texto}{Cor.RESET}\n")

def separador(): # formatação visual com cores ANSI
    print("─" * 54)


# Casos do jogo

CASOS = [

    # ── CASO 1 ──────────────────────────────────────
    {
        "id": 1,
        "titulo": "O Roubo na Biblioteca",
        "dificuldade": "Fácil ⭐",
        "regra": "Modus Ponens",
        "explicacao_regra": (
            "MODUS PONENS\n"
            "  Se (P → Q) e P é verdadeiro → Q é verdadeiro.\n"
            "  Ex: 'Se usou a chave → pegou o livro' + 'Usou a chave' → 'Pegou o livro'."
        ),
        "narrativa": (
            "Um livro raro sumiu da biblioteca na sexta à noite.\n"
            "Três estudantes estavam no local: ANA, BRUNO e CARLOS.\n"
            "Use as pistas para descobrir quem pegou o livro."
        ),
        "suspeitos": ["Ana", "Bruno", "Carlos"],
        "pistas": [
            {
                "tipo": "Condicional (P → Q)",
                "texto": "SE alguém usou a chave reserva → ESSA pessoa pegou o livro.",
            },
            {
                "tipo": "Fato (P é verdadeiro)",
                "texto": "O registro eletrônico mostra: ANA usou a chave reserva às 21h07.",
            },
            {
                "tipo": "Álibi",
                "texto": "Bruno e Carlos estavam na cantina das 20h às 22h — confirmado.",
            },
        ],
        "resposta": "Ana",
        "explicacao": (
            "  P = 'Alguém usou a chave reserva'\n"
            "  Q = 'Essa pessoa pegou o livro'\n\n"
            "  Pista 1: P → Q\n"
            "  Pista 2: P é verdadeiro para ANA\n"
            "  ∴ Modus Ponens: Q é verdadeiro → ANA pegou o livro.\n"
            "  Pista 3 elimina Bruno e Carlos por álibi."
        ),
    },

    # ── CASO 2 ──────────────────────────────────────
    {
        "id": 2,
        "titulo": "O Envenenamento no Jantar",
        "dificuldade": "Médio ⭐⭐",
        "regra": "Modus Tollens",
        "explicacao_regra": (
            "MODUS TOLLENS\n"
            "  Se (P → Q) e Q é FALSO → P é FALSO.\n"
            "  Ex: 'Se preparou o prato → estava na cozinha' + 'Não estava' → 'Não preparou'."
        ),
        "narrativa": (
            "Uma taça foi envenenada durante o jantar da família Silveira.\n"
            "O veneno exige acesso à cozinha antes das 20h.\n"
            "Suspeitos: DIANA, EDUARDO e FERNANDA."
        ),
        "suspeitos": ["Diana", "Eduardo", "Fernanda"],
        "pistas": [
            {
                "tipo": "Condicional (P → Q)",
                "texto": "SE o culpado colocou o veneno → ESTAVA na cozinha antes das 20h.",
            },
            {
                "tipo": "¬Q para Eduardo",
                "texto": "Câmeras: Eduardo chegou à mansão às 20h35 — não estava antes das 20h.",
            },
            {
                "tipo": "¬Q para Diana",
                "texto": "GPS: Diana estava a 120 km até 19h50 — impossível chegar antes das 20h.",
            },
            {
                "tipo": "Confirmação",
                "texto": "Mordomo testemunha: Fernanda estava sozinha na cozinha das 19h30 às 19h55.",
            },
        ],
        "resposta": "Fernanda",
        "explicacao": (
            "  P = 'O culpado colocou o veneno antes das 20h'\n"
            "  Q = 'O culpado estava na cozinha antes das 20h'\n\n"
            "  Pista 1: P → Q\n"
            "  Pista 2: ¬Q para Eduardo → Modus Tollens: ¬P (Eduardo inocente)\n"
            "  Pista 3: ¬Q para Diana   → Modus Tollens: ¬P (Diana inocente)\n"
            "  Sobra FERNANDA — confirmada pela pista 4."
        ),
    },

    # ── CASO 3 ──────────────────────────────────────
    {
        "id": 3,
        "titulo": "O Sabotador do Torneio",
        "dificuldade": "Difícil ⭐⭐⭐",
        "regra": "Silogismo Hipotético",
        "explicacao_regra": (
            "SILOGISMO HIPOTÉTICO\n"
            "  Se (P → Q) e (Q → R) → (P → R).\n"
            "  Você encadeia duas condicionais para chegar a uma conclusão mais distante."
        ),
        "narrativa": (
            "O servidor do torneio de programação foi invadido horas antes da final.\n"
            "Três competidores tinham credenciais: GABRIEL, HELENA e IGOR.\n"
            "Este caso exige encadear múltiplas inferências."
        ),
        "suspeitos": ["Gabriel", "Helena", "Igor"],
        "pistas": [
            {
                "tipo": "Condicional (P → Q)",
                "texto": "SE conhecia a vulnerabilidade → USOU a VPN interna da universidade.",
            },
            {
                "tipo": "Condicional (Q → R)",
                "texto": "SE usou a VPN interna → O ACESSO partiu de dentro do campus.",
            },
            {
                "tipo": "Conclusão (P → R)",
                "texto": "Encadeando: quem conhecia a vulnerabilidade acessou de dentro do campus.",
            },
            {
                "tipo": "Eliminações",
                "texto": (
                    "Gabriel: cartão de embarque comprova que estava em São Paulo.\n"
                    "  Igor: usou VPN *externa* — rastreada ao IP da casa dele."
                ),
            },
            {
                "tipo": "Confirmação",
                "texto": (
                    "Helena participou da equipe que descobriu a vulnerabilidade (satisfaz P).\n"
                    "  Registro de entrada: ela estava no campus no horário (satisfaz R)."
                ),
            },
        ],
        "resposta": "Helena",
        "explicacao": (
            "  P = 'Conhecia a vulnerabilidade'\n"
            "  Q = 'Usou a VPN interna'\n"
            "  R = 'Acessou de dentro do campus'\n\n"
            "  Pistas 1+2: P → Q → R  ∴ Silogismo Hipotético: P → R\n"
            "  Gabriel: estava fora da cidade (¬R) → inocente\n"
            "  Igor: usou VPN externa (¬Q) → inocente\n"
            "  HELENA satisfaz P e R → culpada."
        ),
    },
]

###############
#Tela inicial
##############

def tela_inicial():
    limpar_tela()
    print(f"""{Cor.CIANO}{Cor.NEGRITO}
  ╔══════════════════════════════════════════════════╗
  ║         🔍  DETETIVE LÓGICO  🔍                 ║
  ║    Um jogo de dedução e raciocínio formal        ║
  ╚══════════════════════════════════════════════════╝
{Cor.RESET}""")

def como_jogar():
    tela_inicial()
    titulo("📖  Como Jogar", Cor.CIANO)

    regras = [
        ("Modus Ponens",        "P → Q  e  P  →  Q"),
        ("Modus Tollens",       "P → Q  e  ¬Q →  ¬P"),
        ("Silogismo Hipotético","P → Q  e  Q → R  →  P → R"),
    ]

    for nome, formula in regras:
        print(f"  {Cor.AMARELO}{Cor.NEGRITO}{nome}{Cor.RESET}")
        print(f"    {formula}\n")

    pausa()


#Jogar os casos

def jogar_caso(caso):
    # ── Regra do caso ────────────────────────────────
    tela_inicial()
    titulo(f"CASO {caso['id']}: {caso['titulo'].upper()}", Cor.AMARELO)
    print(f"  Dificuldade : {caso['dificuldade']}")
    print(f"  Regra usada : {caso['regra']}\n")
    separador()
    print(f"\n{Cor.DIM}{caso['explicacao_regra']}{Cor.RESET}")
    pausa()

    # ── Narrativa ────────────────────────────────────
    tela_inicial()
    titulo(f"CASO {caso['id']}: {caso['titulo'].upper()}", Cor.AMARELO)
    titulo("📜 Narrativa", Cor.CIANO)
    digitar(caso["narrativa"])

    print(f"\n{Cor.NEGRITO}Suspeitos:{Cor.RESET}")
    for i, nome in enumerate(caso["suspeitos"], 1):
        print(f"  {i}. {nome}")
    pausa()

    # ── Pistas ───────────────────────────────────────
    total_pistas = len(caso["pistas"])
    for i, pista in enumerate(caso["pistas"], 1):
        tela_inicial()
        titulo(f"CASO {caso['id']}: {caso['titulo'].upper()}", Cor.AMARELO)
        titulo(f"🔎 Pista {i} de {total_pistas}", Cor.CIANO)
        print(f"  {Cor.DIM}[{pista['tipo']}]{Cor.RESET}\n")
        digitar(f"  {pista['texto']}")
        pausa()

    # ── Pergunta ─────────────────────────────────────
    tela_inicial()
    titulo(f"CASO {caso['id']}: {caso['titulo'].upper()}", Cor.AMARELO)
    print(f"{Cor.NEGRITO}Com base nas pistas, quem é o culpado?{Cor.RESET}\n")

    for i, nome in enumerate(caso["suspeitos"], 1):
        print(f"  {Cor.AMARELO}[{i}]{Cor.RESET}  {nome}")

    # Valida a entrada — só aceita 1, 2 ou 3
    while True:
        escolha = input("\n  Sua resposta (1, 2 ou 3): ").strip()
        if escolha in ("1", "2", "3"):
            break
        print(f"  {Cor.VERMELHO}Digite 1, 2 ou 3.{Cor.RESET}")

    escolhido = caso["suspeitos"][int(escolha) - 1]
    acertou = escolhido == caso["resposta"]

    # ── Resultado ────────────────────────────────────
    separador()
    if acertou:
        print(f"\n{Cor.VERDE}{Cor.NEGRITO}  ✅  Correto! {escolhido} é o culpado!{Cor.RESET}")
    else:
        print(f"\n{Cor.VERMELHO}{Cor.NEGRITO}  ❌  Errado. O culpado era {caso['resposta']}.{Cor.RESET}")

    titulo(f"📐 Explicação — {caso['regra']}", Cor.CIANO)
    print(caso["explicacao"])
    pausa()

    return acertou


# ─────────────────────────────────────────────────────
#  MENU PRINCIPAL
#
#  Loop while True — o jogo só termina na opção [4].
#  Pontos são acumulados ao jogar todos os casos.
# ─────────────────────────────────────────────────────

def menu():
    while True:
        tela_inicial()
        print(f"  {Cor.NEGRITO}Bem-vindo, Detetive!{Cor.RESET}\n")
        print(f"  {Cor.AMARELO}[1]{Cor.RESET}  Jogar todos os casos")
        print(f"  {Cor.AMARELO}[2]{Cor.RESET}  Escolher um caso")
        print(f"  {Cor.AMARELO}[3]{Cor.RESET}  Como jogar")
        print(f"  {Cor.AMARELO}[4]{Cor.RESET}  Sair\n")

        opcao = input("  Escolha: ").strip()

        # ── Jogar tudo ───────────────────────────────
        if opcao == "1":
            pontos = 0
            for caso in CASOS:
                if jogar_caso(caso):
                    pontos += 1  # True == 1 em Python

            tela_inicial()
            titulo("🏁 Resultado Final", Cor.CIANO)
            print(f"  Acertos: {Cor.VERDE}{pontos}{Cor.RESET} / {len(CASOS)}\n")

            if pontos == len(CASOS):
                print(f"  {Cor.VERDE}🏆 Perfeito! Você domina lógica formal!{Cor.RESET}")
            elif pontos >= 2:
                print(f"  {Cor.AMARELO}🔍 Bom trabalho! Revise o que errou.{Cor.RESET}")
            else:
                print(f"  {Cor.VERMELHO}📚 Releia as regras e tente de novo!{Cor.RESET}")

            pausa()

        # ── Escolher caso ────────────────────────────
        elif opcao == "2":
            tela_inicial()
            titulo("Escolha um caso:", Cor.CIANO)
            for c in CASOS:
                print(f"  [{c['id']}]  {c['titulo']}  —  {c['dificuldade']}")

            escolha = input("\n  Número: ").strip()

            # Dict lookup por ID — mais direto que um for
            casos_por_id = {str(c["id"]): c for c in CASOS}
            if escolha in casos_por_id:
                jogar_caso(casos_por_id[escolha])
            else:
                print(f"\n  {Cor.VERMELHO}Caso inválido.{Cor.RESET}")
                time.sleep(1)

        # ── Como jogar ───────────────────────────────
        elif opcao == "3":
            como_jogar()

        # ── Sair ─────────────────────────────────────
        elif opcao == "4":
            limpar_tela()
            print(f"\n  {Cor.CIANO}Até logo, Detetive! 🔍\n{Cor.RESET}")
            break  # sai do while True (mais limpo que sys.exit)

        else:
            print(f"\n  {Cor.VERMELHO}Opção inválida.{Cor.RESET}")
            time.sleep(1)


# ─────────────────────────────────────────────────────
#  PONTO DE ENTRADA
#
#  Só executa quando rodado diretamente:
#    python detetive_logico.py
#  Se outro arquivo importar este módulo, menu() não é chamado.
# ─────────────────────────────────────────────────────

if __name__ == "__main__":
    if os.name == "nt":
        os.system("color")  # ativa cores ANSI no Windows
    menu()

