'''A , B , C
Se 2 tiverem certeza, implementa. 
Senão, não implementa. 
Qual n vão escrever uma solução ? 
n linhas contem 3 votos , onde 1 é sim 
0 é nao'''

problemascompeticao=  int(input(""))
problemasenviados=0
for i in range (problemascompeticao):

    a= int(input(""))
    b= int(input ("")) #ativ. descobrir uma forma de resumir essas três perguntas pra ser rápido 
    c= int(input (""))  

    if a + b + c >= 2 :
        problemasenviados+=1  
print(problemasenviados)