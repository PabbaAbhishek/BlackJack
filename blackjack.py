import random
from os import system
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
print('''
                                      .------.
                   .------.           |A .   |
                   |A_  _ |    .------; / \  |
                   |( \/ )|-----. _   |(_,_) |
                   | \  / | /\  |( )  |  I  A|
                   |  \/ A|/  \ |_x_) |------'
                   `-----+'\  / | Y  A|
                         |  \/ A|-----'   
                         `------''')
print('''88          88                       88                                 88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P''')
print("Let's start the game of BlackJack :)")
should_continue=False
while not should_continue:
  player_first=cards[random.randint(0,12)]
  player_second=cards[random.randint(0,12)]
  player_third=cards[random.randint(0,12)]
  computer_first=cards[random.randint(1,12)]
  computer_second=cards[random.randint(0,12)]
  computer_third=cards[random.randint(0,12)]
  total_player_2=player_first+player_second
  total_computer_2=computer_first+computer_second
  if player_first==11 or player_second==11:
    if total_player_2>20:
      total_player_2-=10
      if player_first==11:
        player_first=1
      elif player_second==11:
        player_second=1
  elif computer_first==11 or computer_second==11:
    if total_computer_2>20:
      total_computer_2-=10
      if computer_first==11:
        computer_first=1
      elif computer_second==11:
        computer_second=1
  total_player_3=player_first+player_second+player_third
  total_computer_3=computer_first+computer_second+computer_third
  print(f"Your first two cards are:[{player_first},{player_second}]. Your current total is '{total_player_2}'")
  print(f"Computer's first card is:[{computer_first}]")
  take_card= input("Do you want to pick another card?\n(Type 'y' for yes and 'n' for no)\n").lower()
  if take_card=="n":
    print(f"Your cards are [{player_first},{player_second}]. Your total is {total_player_2}")
    if total_player_2>21:
      print("Your score is greater than 21.\nYou lose...")
    else:
      print(f"Computer's second card is {computer_second}")
      print(f"Computer's cards are [{computer_first},{computer_second}]. Computer total is {total_computer_2}")
      if total_computer_2>21:
        print("You win")
      else:
        if total_computer_2>total_player_2:
          print("You lose")
        elif total_computer_2<total_player_2:
          print("You Win")
        else:
          print("It is a draw")
  elif take_card=="y":
    print(f"Your third card is: {player_third}")
    print(f"Your final cards are [{player_first},{player_second},{player_third}]. Your total is {total_player_3}")
    if total_player_3>21:
      print("You lose")
    else:
      print(f"Computer's second card is '{computer_second}'")
      print(f"Computer's two cards are [{computer_first},{computer_second}]. Computer's current total is '{total_computer_2}'")
      if total_computer_2>21:
        print("You win")
      else:
        if total_computer_2>total_player_3 and total_computer_2>17:
          print("You lose")
        elif total_computer_2<17:
          print("As computer's current score is <17, computer picks another card.")
          print(f"Computer's third card is '{computer_third}'. Computer's final total is '{total_computer_3}'")
          if total_computer_3>21:
            print("You win")
          else:
            if total_computer_3<total_player_3:
              print("You Win")
            elif total_computer_3>total_player_3:
              print("You lose")
            else:
              print("It is a draw")
          if total_computer_2<total_player_3 and total_computer_2>17:
            print(f"Computer's third card is '{computer_third}'. Computer's final total is '{total_computer_3}'")
            if total_computer_3>21:
              print("You win")
            else:
              if total_computer_3<total_player_3:
                print("You Win")
              elif total_computer_3>total_player_3:
                print("You lose")
              else:
                print("It is a draw")
  quit=input("Want to ontinue (press 'y') or take a break (press any other key)").lower()
  if quit=="y":
    system('cls')
  else:
    system('cls')
    should_continue=True