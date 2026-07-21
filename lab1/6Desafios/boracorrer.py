## PROJETO: BORACORRER - PLANEJAMENTO DE TREINOS DE CORRIDA
## INTEGRANTES: LAURA , LUIZ , KEMYLLY .

import turtle
import tkinter as tk
from tkinter import simpledialog, messagebox

## CONFIGURAÇÃO DA INTERFACE GRÁFICA
def perguntar(titulo, pergunta, opcoes=None):
   resposta = None
   def on_select():
      nonlocal resposta
      resposta = var.get()
      win.destroy()

   if opcoes:
      win = tk.Tk()
      win.title(titulo)
      tk.Label(win, text=pergunta, font=("Arial", 12)).pack(padx=20, pady=10)
      var = tk.StringVar(win)
      var.set(opcoes[0])
      option = tk.OptionMenu(win, var, *opcoes)
      option.config(font=("Arial", 12))
      option.pack(pady=5)
      tk.Button(win, text="OK", command=on_select, font=("Arial", 12)).pack(pady=10)
      win.mainloop()
      return resposta
   else:
      root = tk.Tk()
      root.withdraw()
      resposta = simpledialog.askstring(titulo, pergunta)
      root.destroy()
      return resposta

## ENTRADA DE DADOS
experiencia = perguntar("Experiência", "Qual seu nível de experiência?", ["Iniciante", "Intermediário", "Experiente"])
objetivo = perguntar("Objetivo", "Qual seu objetivo?", ["Diminuir o pace", "Concluir uma prova específica", "Melhorar condicionamento"])
prazo = perguntar("Prazo", "Qual prazo para o seu objetivo ?")
dias = perguntar("Dias de treino", "Quantos dias por semana você pode treinar?")

planilha = []
if experiencia == "Iniciante":
   planilha.append("- 2 a 3 treinos por semana, priorizando resistência e adaptação.")
elif experiencia == "Intermediário":
   planilha.append("- 3 a 4 treinos por semana, incluindo tiros e fortalecimento.")
elif experiencia == "Experiente":
   planilha.append("- 4 a 6 treinos por semana, com foco em performance e variação de estímulos.")
else:
   planilha.append("- Nível não reconhecido, personalize sua rotina com orientação profissional.")

if objetivo and "pace" in objetivo.lower():
   planilha.append("- Inclua treinos intervalados (tiros) e de ritmo.")
elif objetivo and "prova" in objetivo.lower():
   planilha.append("- Simule a distância da prova em treinos longos.")
elif objetivo and "condicionamento" in objetivo.lower():
   planilha.append("- Varie intensidade e inclua fortalecimento.")
else:
   planilha.append("- Defina um objetivo claro para melhores resultados.")

planilha.append("- Reserve pelo menos 1 dia para descanso.")
planilha.append("- Monitore seu pace e frequência cardíaca.")

## SUGESTÃO DE TREINO PARA O CORREDOR (BASEADA NAS RESPOSTAS FORNECIDAS)
mensagem = "\n".join([
   "Olá, corredor! Aqui está sua sugestão de treino:",
   f"Experiência: {experiencia}",
   f"Objetivo: {objetivo}",
   f"Prazo: {prazo}",
   f"Dias disponíveis: {dias}",
   "",
   "Sugestões:",
   *planilha,
   "",
   "Bons treinos! Lembre-se: Um passo por vez. O topo te espera!"
])
## MENSAGEM FINAL CONFIGURAÇÃO
def mostrar_turtle(texto):
   t = turtle.Turtle()
   t.hideturtle()
   turtle.title("BoraCorrer")
   turtle.setup(width=700, height=500)
   turtle.bgcolor("#f0f8ff")
   t.penup()
   t.goto(-320, 200)
   t.pendown()
   for linha in texto.split("\n"):
      t.write(linha, font=("Arial", 14, "normal"))
      t.penup()
      t.sety(t.ycor() - 30)
      t.pendown()
   turtle.done()

mostrar_turtle(mensagem)