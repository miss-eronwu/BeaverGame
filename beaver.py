#Create your own video game
#Run code in any python console to play 

print('''                                 
888                                             
888                                             
88888b.  .d88b.  8888b. 888  888 .d88b. 888d888 
888 "88bd8P  Y8b    "88b888  888d8P  Y8b888P"   
888  88888888888.d888888Y88  88P88888888888     
888 d88PY8b.    888  888 Y8bd8P Y8b.    888     
88888P"  "Y8888 "Y888888  Y88P   "Y8888 888    
''')

first_turn = input("Welcome to the beaver adventure game! Lead the lost beaver back to his dam."
      "\nThe beaver went to get more wood for his dam but wandered in the woods for a long time and now he is lost. "
       "\nHe managed to find the river but he does not know if he should go upstream or downstream."
        "\nWhich route do you want to take? Left or Right?").lower()

if first_turn == "right":
    print('''The beaver turns right, he goes upstream and ends up at a river fork:"

        ___
           .="   "=._.---.
         ."         c ' Y'`p
        /   ,       `.  w_/
    jgs |   '-.   /     /
  _,..._|      )_-\ \_=.\
 `-....-'`------)))`=-'"`'"
                  ''')

    second_turn = input("Which side of the river do you want to explore? Left or Right?").lower()
    if second_turn == "left":
        print('''The beaver has made it further down the river. It has even found extra wood for its dam"
              "     |    :|
                   |     |
                   |    .|
               ____|    .|
             .' .  ).   ,'
           .' c   '7 ) (
       _.-"       |.'   `.
     .'           "8E   :|
     |          _}""    :|
     |         (   |     |
    .'         )   |    :|
.odCG8o_.---.__8E  |    .|    
`Y8MMP""       ""  `-...-'   cgmm
''')
    else:
      print("The beaver took the right and was chased by a grizzly bear hunting salmon\nGame Over")
    third_turn = input("The beaver made it to the final river fork, which path do you take this like, left or right?").lower()
    if third_turn == "right":
        print("Congrats! You finally made it to your dam.\n"
              '''
 \
  \
   \         ___
 \  \       ('+'`)_------_   ######
  ><          W           -##########
 }  { ejm 96    /|/----\|\  #######
 }  {          " "      " "

''')
    else:
        print("Sorry, this way leads to a lake, a dead end.")
else:
    print("The current is too strong and the beaver ends up being pushed further downstream. "
          "Game Over")
