import random

num = random.randint(1,100)

while True:
     
     guess=int(input("Enter your guess number : "))

     if guess < 1 or guess > 100:
       print("Please enter the number between 1 and 100")
       continue
     
     if guess < num:
         print("lower number")
         print("computer number",num)

     elif guess > num:
         print("higher number")
         print("computer number",num)
         
     else:
         print("guess number is correct")
         break