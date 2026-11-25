## Getting started

print("Hello world!")
a=(input("What is your name?"))
print(a,", That's a nice name!")
b=int(input("Ok then, what is your age?"))
print(b,", Nice!")

## Operations/Standard mathmatic equations

print("Welcome to the standard calculator!")
num1=int(input("Please enter a number: "))
num2=int(input("Please enter a second number: "))
op=(input("Please enter a mathmatical operation (+ Or - Or * Or /): "))

if op=="+":
    print(num1+num2," Is the answer!")
elif op=="-":
    print(num1-num2," Is the answer!")
elif op=="*":
    print(num1*num2," Is the answer!")
else:
    print(num1/num2," Is the answer!")

## Conditional statements

inpu=int(input("Hello, please enter your grade to see if you passed or failed: "))

if inpu<0:
    print("Sorry, but it seems like you entered the wrong grade.")
elif inpu<=50:
    print("You failed, better luck next time!")
elif inpu<=70:
    print("You barely! Just Barely! passed. Try harder next time")
elif inpu<=85:
    print("Standard, try to get a 90 next time!")
elif inpu<=95:
    print("Wow! You are brilliant!")
else:
    print("Error, you entered the wrong grade.")

## Loops

i=40

for i in range(i):
    print("Your number is ",i)

while i<=40:
    print("Your number is ",i)
    i+=1

## Functions

def greet(name):
    print("Greetings! "+name)

greet("Mehdiya")

## Lists

Fruits=["Banna","Orange","Apple"]

for f in Fruits:
    print(Fruits[1])

## OOP

class Cars:
    vehicle="Car"
    def __init__(self,type,brand):
        self.type=type
        self.brand=brand
car1=Cars("Sedan","Toyota Camry")
car2=Cars("SUV","Hyundai Elantra")

print("Car type: ",car1.type)
print("Car Brand: ",car1.brand)
print("Car type: ",car2.type)
print("Car Brand: ",car2.brand)

# Game screen/pygame

import pygame

pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT=800, 800

display_surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Practice.")

background_img=pygame.transform.scale(pygame.image.load("wave.jpg"))