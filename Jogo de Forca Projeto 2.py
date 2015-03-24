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
    turtle.position()
    (0.00,0.00)
    turtle.right(90)
    turtle.forward(-100)
    turtle.position()
    (0.00,100.00)
    turtle.right(90)
    turtle.forward(-75)
    turtle.position()
    (75.00,100.00)
    turtle.right(90)
    turtle.forward(-30)
    turtle.position()
    (75.00,70.00)    
    
window.exitonclick()