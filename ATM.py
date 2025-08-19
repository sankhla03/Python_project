pasword = 1234
balance = 100000000000

print("plz enter your card")

print("Select your Language")
print("1 : Hindi")
print("2: English")
a =int(input())

if(a==1):
    print("hindi")
elif(a==2):
    print("English")



pin = int(input("enter your pin: "))

if(pin == pasword):
    if( pin == pasword ):
        flag =0
        print("1: saving")
        print("2: curent")
        v = int(input("select account type "))

        if(v==1):
         print("saving")
        elif(v==2):
         print("Current")
     
        print("1: withdraw")
        print("2: check balance")
        u = int(input())
        a = 000
        if(u==1):
         a = int(input("enter amount: "))
         print(a,"Withdraw is processing ")
         print("remaining amount is : ", balance-a)

        elif(u==2):
         print("Current amount is ", balance -a)

else:
    print("You enter Wrong password, plz try again") 

    repass =  int(input("Re-enter password: ")) 

    if(pasword == repass):
       if(pasword == repass or pin == pasword ):
        flag =0
        print("1: saving")
        print("2: curent")
        v = int(input("select account type "))

        if(v==1):
         print("saving")
        elif(v==2):
         print("Current")
     
        print("1: withdraw")
        print("2: check balance")
        u = int(input())
        a = 000
        if(u==1):
         a = int(input("enter amount: "))
         print(a,"Withdraw is processing ")
         print("remaining amount is : ", balance-a)

        elif(u==2):
         print("Current amount is ", balance -a)

    else:
      print("invalid password, Plz try again")

      o = int(input("Re-enter password: "))

      if(pasword == o):
         print("1: saving")
         print("2: curent")
         v = int(input("select account type "))

         if(v==1):
          print("saving")
         elif(v==2):
          print("Current")
     
         print("1: withdraw")
         print("2: check balance")
         u = int(input())
         a = 000
         if(u==1):
          a = int(input("enter amount: "))
          print(a,"Withdraw is processing ")
          print("remaining amount is : ", balance-a)

         elif(u==2):
          print("Current amount is ", balance -a)

      else:
        print("Your card has been block")
          
   

       