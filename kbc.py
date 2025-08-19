
questions =[["in these which isnot the part of python data typr",
            "arr", "none","string","int", 0],
            ["what isnot required in love?",
              "trust","care", "understanding","ego", 3],
            ["my last name is ?" ,
               "gupta", "sarma","sankhla", "singaniya", 2],
            ["what is my first name ?",
               "vikas", "aditya","ravi","uv", 1],
            ["my Father's last name is ?" ,
               "gupta", "sarma","sankhla", "singaniya", 2],
            ["my mother's last name is ?" ,
              "gupta", "sarma","Gahlot", "singaniya", 2],
            ["what is father's first name ?",
               "vikas", "aditya","LaduRam","uv", 2],
            ["what ismother's first name ?",
              "vikas", "aditya","ravi","rukma", 3]
             ]

levels =[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money =0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"question for Rs. {levels[i]}")
    print(f"a.{question[1]}        b.{question[2]}")
    print(f"c.{question[3]}        d.{question[4]}")
    reply = int(input("Enter the answer(1-4) "))
    if(reply-1 == question[-1]):
        print(f"carret answer, you won Rs. {levels[i]}")
        if(i==3):
            money = 10000
        elif(i==6):
            money = 320000
        elif(i==7):
            money = 1000000
    else:
        print("Incorret answer ")
        break
print(f"you take money home after finising Game Rs. {money}")
          