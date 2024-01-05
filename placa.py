import random

abe ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
total =4



for i in range(total):
    letra1= random.choice(abe)
    letra2= random.choice(abe)
    letra3= random.choice(abe)
    
    
    num1= random.choice(num)
    num2= random.choice(num)
    num3= random.choice(num)
    print("{}{}{} - {}{}{}". format(letra1,letra2,letra3, num1, num2, num3,))    



    
