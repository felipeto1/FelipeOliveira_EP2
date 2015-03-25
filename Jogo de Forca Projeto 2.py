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
sup=0
while sup<=11: #definindo 11 rodadas
    erros=0
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
    while (h<=tamanho or erros!=7): #criando o loop principal
        letra=window.textinput('letra','escolha uma letra') #janela deescrever a letra
        if letra in escolha:
            if letra==escolha[0]: #condições para posicionamento das letras
                turtle.penup()
                turtle.setpos(-135.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[1]:
                turtle.penup()
                turtle.setpos(-115.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[2]:
                turtle.penup()
                turtle.setpos(-95.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[3]:
                turtle.penup()
                turtle.setpos(-75.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[4]:
                turtle.penup()
                turtle.setpos(-55.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[5]:
                turtle.penup()
                turtle.setpos(-35.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[6]:
                turtle.penup()
                turtle.setpos(-15.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[7]:
                turtle.penup()
                turtle.setpos(5.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[8]:
                turtle.penup()
                turtle.setpos(15.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[9]:
                turtle.penup()
                turtle.setpos(35.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[10]:
                turtle.penup()
                turtle.setpos(55.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[11]:
                turtle.penup()
                turtle.setpos(75.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[12]:
                turtle.penup()
                turtle.setpos(95.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[13]:
                turtle.penup()
                turtle.setpos(115.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[14]:
                turtle.penup()
                turtle.setpos(135.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[15]:
                turtle.penup()
                turtle.setpos(155.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[16]:
                turtle.penup()
                turtle.setpos(175.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[17]:
                turtle.penup()
                turtle.setpos(195.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[18]:
                turtle.penup()
                turtle.setpos(215.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[19]:
                turtle.penup()
                turtle.setpos(235.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
            if letra==escolha[20]:
                turtle.penup()
                turtle.setpos(255.00,20.00)
                turtle.pendown()
                turtle.write(letra)
                h+=1
        else:
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
            turtle.right(180)

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
            
        if h==tamanho:
            turtle.penup()
            turtle.setpos(00.00,100.00)
            turtle.pendown()
            turtle.write('GANHOU!') #imprimindo notificação de vitória
            
        turtle.penup()
        turtle.setpos(-145.00,15.00)
        turtle.pendown()
    sup+=1
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
window.exitonclick()