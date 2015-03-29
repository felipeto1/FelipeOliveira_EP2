# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:54:21 2015

@author: Felipe
"""
from random import choice
import turtle
f = open("entrada.txt", encoding="utf-8") #Puxando as palavras do arquivo
palavra=f.readlines()
window = turtle.Screen()    #criando a janela
window.bgcolor("gray")
window.title("Jogo da Forca")

turtle.setpos(320.00,0.00) #criando a forca
turtle.setpos(-275.00,0.00)
turtle.setpos(-275.00,200.00)
turtle.setpos(-160.00,200.00)
turtle.setpos(-160.00,180.00)
turtle.penup()
turtle.setpos(-145.00,15.00)
turtle.pendown()
turtle.hideturtle()
repetiçoes=0
while repetiçoes<11: #definindo 11 rodadas
    erros=0
    d=0
    v=0
    h=0
    escolha=choice(palavra) #o sistema escolhe uma palavra aleatória da lista
    palavra.remove(escolha) #o sistema deleta a palavra escolhida da lista
    tamanho=len(escolha)
    for u in escolha: #criando as linhas debaixo das letras
        if u!= ' ':
            turtle.forward(20)
        else:
            turtle.penup()
            turtle.forward(20)
            turtle.pendown()
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
    while (h<tamanho and erros<6): #criando o loop principal
        letra=window.textinput('letra','escolha uma letra') #janela de escrever a letra
        if len(letra)==1:
            n=escolha.count(letra)
            j=0
            x=0
            while j<n:
                x=escolha.index(letra,x+1) #colocando as letras nos lugares
                j+=1
                if letra in escolha:
                    turtle.penup()
                    turtle.setpos(-140.00+(25*x),15.00)
                    turtle.pendown()
                    turtle.write(letra)
            
            if letra not in escolha:
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
            
            if h==tamanho:
                turtle.penup()
                turtle.setpos(00.00,100.00)
                turtle.pendown()
                turtle.write('GANHOU!') #imprimindo notificação de vitória
                turtle.write('Sua média de chutes por acertos foi: ')
                turtle.write(h+erros/tamanho)
                v+=1
        else:
            turtle.penup()
            turtle.setpos(00.00,200.00)
            turtle.pendown()
            turtle.write('Você só pode escolher uma letra por vez')
    jd=window.textinput('Restart','Deseja jogar denovo?')
    for s in jd:
        repetiçoes+=1
    for n in jd:
        repetiçoes+=20
    turtle.reset() #resetando
    turtle.setpos(320.00,0.00) #recriando a forca
    turtle.setpos(-275.00,0.00)
    turtle.setpos(-275.00,200.00)
    turtle.setpos(-160.00,200.00)
    turtle.setpos(-160.00,180.00)
    turtle.penup()
    turtle.setpos(-145.00,15.00)
    turtle.pendown()
    turtle.hideturtle()
    
turtle.penup() #Criando o Score
turtle.setpos(100.00,60.00)
turtle.pendown()
turtle.write('Seu score foi:', v)
turtle.write('O score do PC foi:', d)
window.exitonclick()