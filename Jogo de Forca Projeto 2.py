# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:54:21 2015

@author: Felipe
"""
from random import choice
import turtle
f = open("entrada.txt", encoding="utf-8")
palavra=f.readlines()
window = turtle.Screen()    
window.bgcolor("gray")
window.title("Jogo da Forca")

q=int(input('Aperte zero para começar - '))
if q==0:
    turtle.setpos(320.00,0.00)
    turtle.setpos(-275.00,0.00)
    turtle.setpos(-275.00,200.00)
    turtle.setpos(-160.00,200.00)
    turtle.setpos(-160.00,180.00)
    turtle.penup()
    turtle.setpos(-130.00,15.00)
    turtle.pendown()
sup=0
while sup<=11:   
    erros=0

    escolha=choice(palavra)
    palavra.remove(escolha)

    tamanho=len(escolha)

    for u in escolha:
        if u!= ' ':
            turtle.forward(20)
        else:
            turtle.penup()
            turtle.forward(20)
            turtle.pendown()
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
    letra=window.textinput('letra','escolha uma letra')
    
    if letra in escolha:
        print(letra)
    else:
        erros+=1
    
    if erros>=1:
        n=100
        dist = -1
        angulo =180-((n-2)*180)/n
        for i in range(n+50):
            turtle.left(angulo)
            turtle.forward(dist)

    if erros>=2:
        turtle.setpos(-160.00,80.00)
    
    if erros>=3:
        turtle.setpos(-160.00,140.00)
        turtle.setpos(-140.00,110.00)

    if erros>=4:
        turtle.setpos(-160.00,140.00)
        turtle.setpos(-180.00,110.00)
    
    if erros>=5:
        turtle.setpos(-160.00,140.00)
        turtle.setpos(-160.00,80.00)
        turtle.setpos(-150.00,40.00)

    if erros>=6:
        turtle.setpos(-160.00,80.00)
        turtle.setpos(-170.00,40.00)
    
    turtle.penup()
    turtle.setpos(-130.00,15.00)

    
window.exitonclick()