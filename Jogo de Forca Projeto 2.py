# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:54:21 2015

@author: Felipe
"""
from random import choice
import turtle
f = open("entrada.txt", encoding="utf-8") #Puxando as palavras do arquivo
palavra=f.readlines()
listapalavras=[]
listapalavras.append(palavra)
window = turtle.Screen()    #criando a janela
window.bgcolor("gray")
window.title("Jogo da Forca")

d=0
v=0
repetiçoes=0
mamona=1
while repetiçoes<11: #definindo rodadas
    if mamona==1:
        turtle.reset()
        turtle.setpos(320.00,0.00) #criando a forca
        turtle.setpos(-275.00,0.00)
        turtle.setpos(-275.00,200.00)
        turtle.setpos(-160.00,200.00)
        turtle.setpos(-160.00,180.00)
        turtle.penup()
        turtle.setpos(-195.00,10.00)
        turtle.pendown()
        turtle.hideturtle()
        erros=0 
        h=0
        escolha=choice(palavra) #o sistema escolhe uma palavra aleatória da lista
        palavra.remove(escolha) #o sistema deleta a palavra escolhida da lista
        escolha=escolha.strip()
        tamanho=len(escolha)
        o=escolha.count(" ")
        lista=[]
        if escolha!=" ":
            for u in escolha: #criando as linhas debaixo das letras
                if u!= ' ':
                    turtle.forward(20)
                if u==' ':
                    turtle.penup()
                    turtle.forward(20)
                    turtle.pendown()
                turtle.penup()
                turtle.forward(5)
                turtle.pendown()
            while (h<tamanho-o and erros<6): #criando o loop principal
                letra=window.textinput('letra','escolha uma letra') #janela de escrever a letra
                if len(letra)==1 and letra not in lista:
                    n=escolha.count(letra)
                    j=0
                    x=-1
                    aaa=escolha.find('ã') #condições para acentos e maiúsculas
                    aaaa=escolha.find('â')
                    eee=escolha.find('é')
                    eeee=escolha.find('ê')
                    iii=escolha.find('í')
                    ooo=escolha.find('ó')
                    oooo=escolha.find('ô')
                    sss=escolha.find('S')
                    bbb=escolha.find('B')
                    ccc=escolha.find('C')
                    aa=escolha.find('A')
                    ee=escolha.find('E')
                    ppp=escolha.find('P')
                    while j<n:
                        x=escolha.index(letra,x+1) #colocando as letras nos lugares
                        j+=1
                        if letra in escolha:
                            turtle.penup()
                            turtle.setpos(-190.00+(25*x),10.00)
                            turtle.pendown()
                            turtle.write(letra)
                            h+=1
                    if letra == "a" and escolha[aaa] == "ã" : #aplicando acentos
                        turtle.penup()
                        turtle.setpos(-190.00+(25*aaa),10.00)
                        turtle.pendown()
                        turtle.write('ã')
                        h+=1
            
                    if letra == "a" and escolha[aaaa]=="â" :
                        turtle.penup()
                        turtle.setpos(-190.00+(25*aaaa),10.00)
                        turtle.pendown()
                        turtle.write('â')
                        h+=1
                       
                    if letra == "e" and escolha[eee] == 'é':
                        turtle.penup()
                        turtle.setpos(-190.00+(25*eee),10.00)
                        turtle.pendown()
                        turtle.write('é')
                        h+=1
                       
                    if letra == "e" and escolha[eeee] == "ê":
                        turtle.penup()
                        turtle.setpos(-190.00+(25*eeee),10.00)
                        turtle.pendown()
                        turtle.write('ê')
                        h+=1
                      
                    if letra == 'o' and escolha[ooo] == 'ó':
                        turtle.penup()
                        turtle.setpos(-190.00+(25*ooo),10.00)
                        turtle.pendown()
                        turtle.write('ó')
                        h+=1
                     
                    if letra == "o" and escolha[oooo] == "ô":
                        turtle.penup()
                        turtle.setpos(-190.00+(25*oooo),10.00)
                        turtle.pendown()
                        turtle.write('ô')
                        h+=1
                        erros-=1
                    if letra == 'i' and escolha[iii] == 'í':
                        turtle.penup()
                        turtle.setpos(-190.00+(25*iii),10.00)
                        turtle.pendown()
                        turtle.write('í') 
                        h+=1
                        erros-=1
                    if letra == "s" and escolha[sss] == "S": # aplicando maiúsculas
                        turtle.penup()
                        turtle.setpos(-190.00+(25*sss),10.00)
                        turtle.pendown()
                        turtle.write('S')
                        h+=1
                        erros-=1
                    if letra == 'e' and escolha[ee] == 'E':
                        turtle.penup()
                        turtle.setpos(-190.00+(25*ee),10.00)
                        turtle.pendown()
                        turtle.write('E')
                        h+=1
                        erros-=1
                    if letra == "b" and escolha[bbb] == "B":
                        turtle.penup()
                        turtle.setpos(-190.00+(25*bbb),10.00)
                        turtle.pendown()
                        turtle.write('B')
                        h+=1
                        erros-=1
                    if letra == 'c' and escolha[ccc] == 'C':
                        turtle.penup()
                        turtle.setpos(-190.00+(25*ccc),10.00)
                        turtle.pendown()
                        turtle.write('C') 
                        h+=1
                        erros-=1
                    if letra == "a" and escolha[aa] == "A":
                        turtle.penup()
                        turtle.setpos(-190.00+(25*aa),10.00)
                        turtle.pendown()
                        turtle.write('A')
                        h+=1
                        erros-=1
                    if letra == 'p' and escolha[ppp] == 'P':
                        turtle.penup()
                        turtle.setpos(-190.00+(25*ppp),10.00)
                        turtle.pendown()
                        turtle.write('P')
                        h+=1
                        erros-=1
                   
                    elif letra not in escolha:
                        erros+=1
                        if erros==1: #criando a cabeça
                            turtle.st()
                            turtle.penup()
                            turtle.setpos(-160.00,180.00)
                            turtle.pendown()
                            n=100
                            dist = -1
                            angulo =180-((n-2)*180)/n
                            for i in range(n):
                                turtle.left(angulo)
                                turtle.forward(dist)
                        if erros==2: #criando o corpo
                            turtle.st()
                            turtle.penup()
                            turtle.setpos(-160.00,148.00)
                            turtle.pendown()
                            turtle.setpos(-160.00,80.00) 
                        if erros==3: #criando o braço esquerdo
                            turtle.st()
                            turtle.penup()
                            turtle.setpos(-160.00,148.00)
                            turtle.pendown()
                            turtle.setpos(-160.00,140.00)
                            turtle.setpos(-140.00,110.00)
                        if erros==4: #criando o braço direito
                            turtle.st()
                            turtle.penup()
                            turtle.setpos(-160.00,148.00)
                            turtle.pendown()
                            turtle.setpos(-160.00,140.00)
                            turtle.setpos(-180.00,110.00)    
                        if erros==5: #criando o perna esquerda
                            turtle.st()
                            turtle.penup()
                            turtle.setpos(-160.00,148.00)
                            turtle.pendown()
                            turtle.setpos(-160.00,140.00)
                            turtle.setpos(-160.00,80.00)
                            turtle.setpos(-150.00,40.00)
                        if erros==6: #criando a perna esquerda
                            turtle.st()
                            turtle.penup()
                            turtle.setpos(-160.00,148.00)
                            turtle.pendown()
                            turtle.setpos(-160.00,80.00)
                            turtle.setpos(-170.00,40.00)
                            turtle.penup()
                            turtle.setpos(00.00,100.00)
                            turtle.pendown()
                            turtle.write('PERDEU!') #Imprimindo notificação de perda
                            turtle.penup()
                            turtle.setpos(00.00,70.00)
                            turtle.pendown()
                            d+=1
                    
                    if h==tamanho-o:
                        turtle.penup()
                        turtle.setpos(00.00,120.00)
                        turtle.pendown()
                        turtle.write('GANHOU!') #imprimindo notificação de vitória
                        turtle.penup()
                        turtle.setpos(00.00,100.00)
                        turtle.pendown()
                        turtle.write('Sua média de chutes por acertos foi: ')
                        scoref=(h+erros)/(tamanho-o)
                        turtle.penup()
                        turtle.setpos(200.00,100.00)
                        turtle.pendown()
                        turtle.write(scoref)
                        v+=1
                elif len(letra)!=1:
                    turtle.penup()
                    turtle.setpos(00.00,200.00)
                    turtle.pendown()
                    turtle.write('Você só pode escolher uma letra por vez')
                else:
                    turtle.penup()
                    turtle.setpos(65.00,40.00)
                    turtle.pendown()
                    turtle.write('Você já escolheu essa letra')
                lista.append(letra)
                
            turtle.penup()
            turtle.setpos(-100.00,-100.00)
            turtle.pendown()
            turtle.write('Seu score é: ')
            turtle.penup()
            turtle.setpos(-100.00,-110.00)
            turtle.pendown()
            turtle.write(v)
            turtle.penup() 
            turtle.setpos(-100.00,-120.00)
            turtle.pendown()
            turtle.write('O score do PC é: ')
            turtle.penup()
            turtle.setpos(-100.00,-130.00)
            turtle.pendown()
            turtle.write(d)
            repetiçoes+=1
            jd=window.textinput('Restart','Deseja jogar denovo?')
            if jd=='não':
                mamona=3
                turtle.bye()
            elif (jd!='sim' and jd!='não'): 
                turtle.penup()
                turtle.setpos(-50.00,-50.00)
                turtle.pendown()
                turtle.write("Não existe essa opção. Digite sim ou não")
                jd=window.textinput('Restart','Deseja jogar denovo?')
      
turtle.reset()
turtle.penup()
turtle.setpos(-2.0,0.0)
turtle.pendown()
turtle.write('FIM DO JOGO')
window.exitonclick()