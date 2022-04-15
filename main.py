# Snakes and Ladders Game
def main():
    import  random  #importing random module

    ladder={4:25,13:46,33:49,42:63,50:69,62:81,74:92} #ladder coordinates or positions using dictionary
    snake={41:3,25:5,43:18,54:31,99:41,66:45,89:53,76:58} #snake coordinates or positions using dictionary
    position1=0  #Initializing PLAYER1 Position
    position2=0  #Initializing PLAYER1 Position

 #PLease Enter Names OF Both Players.......

    a=(input("Please Enter NAME of Player 1: "))
    b=(input("Please Enter NAME of Player 2: "))

    def move(pos):
        dice=random.randint(1,6) #Generating Random number between 1 to 6
        print(f"Dice:{dice}")
        pos=pos+dice
        if pos in snake:
            print("OOPS You BITTEN BY A SNAKE")
            pos=snake[pos]
            print(f"Position:{pos}")
        elif pos in ladder:
            print(" You Climbed A Ladder")
            pos = ladder[pos]
            print(f"Position:{pos}")
        else:
            print(f"Position:{pos}")
        print("\n")
        return  pos
    while True:

        A=input( f"{a} Please Enter \"D\" to throw dice:")
        position1=move(position1)
        if position1 >=100:
            print("Game Over!!")
            print(f"{a} You Win!!!!!!!")
            break

        B=input( f"{b} Please  Enter \"D\" to throw dice:")
        position2 =move(position2)
        if position2 >= 100:
            print("Game Over!!!")
            print(f"{b} You Win!!!")
            break
    print("Type [yes] to continue or [no] to exit")
    contd=input("Do You Want To Play the Game Again: ")

    if contd=="yes":
        main()
    else:
        exit()
main()

