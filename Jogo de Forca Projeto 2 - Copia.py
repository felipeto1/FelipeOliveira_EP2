# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:54:21 2015

@author: Felipe
"""

import turtle
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

lista=[SÃ£o Paulo, SÃ£o Bernardo do Campo, Baleia Azul, leÃ£o marinho, wikipedia, videojogo, equinÃ³cio, EstÃ´nia, cenozÃ³ico, tardÃ­grado, covalente]

for k in range():   
    erros=0

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