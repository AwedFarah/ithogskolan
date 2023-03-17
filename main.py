import random
print("Välkommen till Sten-sax-påse")

point = int(input("Hur många poäng vill du köra till?: "))

my_scour = 0

computer_scour = 0

while True:

    if point == my_scour:
      print ("Du vann")
      break

    elif point == computer_scour:
        print("Du förlorade")
        break

    my_choice = input("Välj sten, sax eller påse: ")
    computer_choice = random.choice(["sten", "sax", "påse"])
    print(computer_choice)

    if my_choice == "påse" and computer_choice == "sten":
        my_scour += 1
    elif my_choice == "sax" and computer_choice == "påse":
        my_scour += 1
    elif my_choice == "sten" and computer_choice == "sax":
        my_scour += 1
    elif my_choice == computer_choice:
        pass
    else:
        computer_scour +=1


