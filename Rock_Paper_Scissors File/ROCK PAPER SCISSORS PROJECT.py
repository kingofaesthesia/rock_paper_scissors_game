import random

print('''Welcome to Rock, Paper, Scissors v1.
How to play;
To play, you have to choose either Rock(R),Paper(P) or Scissors(S) to continue each gameplay.
Enter 'Quit' or a wrong value to END the game.\n''')

def game_playrec():
 '''Writing a function that returns to the gameplay's menu'''
 Rock_list = ['R', 'Rock']
 Paper_list = ['P', 'Paper']
 Scissors_list = ['S', 'Scissors']
 Answers = [Rock_list, Paper_list, Scissors_list]
 C = ['C','Computer']
 F = ['F','Friend']
 score = 0
 score2 = 0
 Trial = -1
 Mode = input(f'\nPick a Game-Play option;\n'
              f"Play versus Computer or versus A Friend? (C/F)\n"
              f"Enter 'Q' to quit the game.; ").title()
 if Mode in C:
   while True:
    Trial = Trial + 1
    item = input(f"\nReady,Set,\n"
                 f"Pick an item; ").title()
    py_item = random.choice(random.choices(Answers, weights=map(len, Answers))[0])
    # py_item = random.choice(Answers) in random.choice
    if item in Rock_list or Paper_list or Scissors_list and item in py_item:

#      '''-------------------------------------Writing the Draws-------------------------------------------'''

     if py_item in Rock_list and item in Rock_list:
      print("That's a tie.\n"
            f"No change in scores.\n"
            f"I swear i picked Rock too.\n")
     elif py_item in Scissors_list and item in Scissors_list:
      print("It's a tie.\n"
            f"Still no change in scores.\n"
            f"I picked Scissors too.\n")
     elif py_item in Paper_list and item in Paper_list:
      print(f"Haha,That's a tie.\n"
            f"No change in scores.\n"
            f"I also picked Paper.(sus!).\n")

#    '''-------------------------------End of Draws-------------------------------------'''

     elif py_item in Scissors_list and item in Rock_list:
      print("Hurray,You won this round.\n"
            f'I picked Scissors.\n'
            f"'Rock' crushes 'Scissors'")
      score = score + 10
      print(f'Your score: {score}')
      print(f'My score: {score2}\n')

     elif py_item in Scissors_list and item in Paper_list:
      print(f"I Won.\n"
            f"I picked Scissors.\n"
            f"'Scissors' cuts 'Paper'")
      score2 = score2 + 10
      print(f'Your score: {score}')
      print(f'My score: {score2}\n')

     elif py_item in Paper_list and item in Rock_list:
      print("Hehe...I won!!!\n"
            f"I picked Paper.\n"
            f"'Paper' covers 'Rock'(wham)")
      score2 = score2 + 10
      print(f'Your score: {score}')
      print(f'My score: {score2}\n')

     elif py_item in Paper_list and item in Scissors_list:
      print("Congrats,You Won!!!\n"
            f'I picked Paper.\n'
            f"'Scissors' cuts 'Paper'")
      score = score + 10
      print(f'Your score: {score}')
      print(f'My score: {score2}\n')

     elif py_item in Rock_list and item in Paper_list:
      print("You won this time.\n"
            f'I picked Rock.\n'
            f"'Paper' covers 'Rock'")
      score = score + 10
      print(f'Your score: {score}')
      print(f'My score: {score2}\n')

     elif py_item in Rock_list and item in Scissors_list:
      print("Yess,I won.\n"
            f'I picked Rock.\n'
            f"'Rock' smashesss 'Scissors'")
      score2 = score2 + 10
      print(f'Your score: {score}')
      print(f'My score: {score2}\n')

     else:
      print('You quit the game')
      print(f'I scored {score2}, and you scored {score} after {Trial} Trials\n')
      if score > score2:
       print('Congrats,You Won!!!')
       replay = input("Press P to play again; \n"
                      "Press Q to Quit.\n"
                      "Select an Option; ").title()
       if replay == 'P':
        game_playrec()
       elif replay == 'Q':
        print("Quitting the game...")
        break
       else:
        print("Uh-OH,You picked a wrong option.(Try entering 'P' to play or 'Q' to quit the game.)")
        game_playrec()
      elif score < score2:
       print('Finally, I won you!!!\n'
             'Hehe...Better luck next time.\n')
       replay = input("Press P to get bumped again xD; \n"
                      "Press Q to Quit.(ha).\n"
                      "Select an Option; ").title()
       if replay == 'P':
        game_playrec()
       elif replay == 'Q':
        print("Quitting the game...")
        break
       else:
        print("Uh-OH,You picked a wrong option.(Try entering 'P' to play or 'Q' to quit the game.)")
        game_playrec()
      elif score == score2:
       print("That's a tie.")
       replay = input("Press P to play again; \n"
                      "Press Q to Quit.\n"
                      "Select an Option; ").title()
       if replay == 'P':
        game_playrec()
       elif replay == 'Q':
        print("Quitting the game...")
        break
       else:
        print("Uh-OH,You picked a wrong option.(Try entering 'P' to play or 'Q' to quit the game.)")
        game_playrec()
      break



 elif Mode in F:
  Rock_list = ['R', 'Rock']
  Paper_list = ['P', 'Paper']
  Scissors_list = ['S', 'Scissors']
  score = 0
  score2 = 0
  Trial = -1
  P1_name = input('Player 1\'s name: ').title()
  P2_name = input('Player 2\'s name: ').title()
  while True:
   Trial = Trial + 1
   P1 = input(f'\n{P1_name}\'s turn ').title()
   P2 = input(f'{P2_name}\'s turn ').title()
   if P1 in Rock_list or Paper_list or Scissors_list and P2 in Rock_list or Paper_list or Scissors_list:

#   '''-------------------------------Writing the Draws-------------------------------------------'''

    if P1 in Rock_list and P2 in Rock_list:
     print("That's a tie")
     print('No change in scores.\n')

    elif P1 in Scissors_list and P2 in Scissors_list:
     print(f"It's a tie\n"
           f"Still no change in scores\n")

    elif P1 in Paper_list and P2 in Paper_list:
     print("\nThat's a tie")
     print('No change in scores.\n')

#     '''------------------------------------End of Draws----------------------------------------------'''

    elif P1 in Scissors_list and P2 in Rock_list:
     print(f'\n{P2_name} won!!!')
     print(f"We'ld advise you to get a heavier Scissors {P1_name}.")
     score2 = score2 + 10
     print(f'{P1_name}: {score} points')
     print(f'{P2_name}: {score2} points\n')

    elif P1 in Scissors_list and P2 in Paper_list:
     print(f'\n{P1_name} won this round!!!')
     print(f"{P2_name} got shaped...(sigh)")
     score = score + 10
     print(f'{P1_name}: {score} points')
     print(f'{P2_name}: {score2} points\n')

    elif P1 in Paper_list and P2 in Rock_list:
     print(f'\n{P1_name} won.')
     print(f"Uh-OH,Seems {P2_name} got covered.")
     score = score + 10
     print(f'{P1_name}: {score} points')
     print(f'{P2_name}: {score2} points\n')

    elif P1 in Paper_list and P2 in Scissors_list:
     print(f'\n{P2_name} won this round!!!')
     print(f"{P1_name} got shaped...(sigh).")
     score2 = score2 + 10
     print(f'{P1_name}: {score}')
     print(f'{P2_name}: {score2}\n')

    elif P1 in Rock_list and P2 in Paper_list:
     print(f'\n{P2_name} won.')
     print(f"Uh-OH,Seems {P1_name} got covered.")
     score2 = score2 + 10
     print(f'{P1_name}: {score} points')
     print(f'{P2_name}: {score2} points\n')

    elif P1 in Rock_list and P2 in Scissors_list:
     print(f'\nAh,tough,{P1_name} won this round.')
     print(f"{P2_name} got smashed by {P1_name}'s mighty Rockk!!...(brutal).")
     score = score + 10
     print(f'{P1_name}: {score}')
     print(f'{P2_name}: {score2}\n')

    else:
     print('\nYou quit the game.')
     print(f'{P1_name} scored {score}, and {P2_name} scored {score2} after {Trial} play(s).')

     if score > score2:
      print(f'Yesss,{P1_name} won!!!,Congrats.')
      replay = input("Press P to play again; \n"
                      "Press Q to Quit.\n"
                      "Select an Option; ").title()
      if replay == 'P':
         game_playrec()
      elif replay == 'Q':
         print("\nQuitting the game...")
         break
      else:
        print("Uh-OH,You picked a wrong option.(Try entering 'P' to play or 'Q' to quit the game.)")
        game_playrec()
     elif score < score2:
      print(f'Hurray, {P2_name} won!!!')
      replay2 = input("Press P to play again; \n"
                      "Press Q to Quit.\n"
                      "Select an Option; ").title()
      if replay2 == 'P':
        game_playrec()
      elif replay2 == 'Q':
        print("\nQuitting the game...\n")
        break
      else:
        print("Uh-OH,You picked a wrong option.(Try entering 'P' to play or 'Q' to quit the game.)")
        game_playrec()
      
     elif score == score2:
      print("It's a tie.")
      replay1 = input("Press P to play again; \n"
                      "Press Q to Quit.\n"
                      "Select an Option; ").title()
      if replay1 == 'P':
         game_playrec()
      elif replay1 == 'Q':
        print("\nQuitting the game...")
        break
      else:
        print("Uh-OH,You picked a wrong option.(Try entering 'P' to play or 'Q' to quit the game.)")
        game_playrec()
     break
   elif P1 not in Rock_list or Paper_list or Scissors_list and P2 not in Rock_list or Paper_list or Scissors_list:
       print("Uh-Oh,Someone picked a wrong item and the game has to restart.\n")
       game_playrec()
 elif Mode == "Q":
     print("\nQuitting game...")
     quit()
 else:
  print("Uh-Oh,You picked a wrong option\n"
        "Try again.")
  quit_option = input("Enter Quit to quit the game.").title()
  if quit_option == 'Q':
      print("\nQuitting game...")
      quit()
  else:
      game_playrec()

game_playrec()