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