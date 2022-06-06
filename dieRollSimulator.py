import random
print("This is a simple Die Roll Simulator \n")
condition = "y"
while(condition=="y"):
  die_number = random.randint(1,6)
  if(die_number==1):
    print("-----------")
    print("|         |")
    print("|    o    |")
    print("|         |")
    print("-----------")
  if(die_number==2):
    print("-----------")
    print("|         |")
    print("|  o   o  |")
    print("|         |")
    print("-----------")
  if(die_number==3):
    print("-----------")
    print("|  o      |")
    print("|    o    |")
    print("|      o  |")
    print("-----------")
  if(die_number==4):
    print("-----------")
    print("|  o   o  |")
    print("|         |")
    print("|  o   o  |")
    print("-----------")
  if(die_number==5):
    print("-----------")
    print("|  o   o  |")
    print("|    o    |")
    print("|  o   o  |")
    print("-----------")
  if(die_number==6):
    print("-----------")
    print("|  o   o  |")
    print("|  o   o  |")
    print("|  o   o  |")
    print("-----------")
  condition = input("Press y if you want to continue \n")
print("Thank you for playing.")
