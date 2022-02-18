print("Welcome to the maze")
side = input("You just entered the home which has treasure hidden in it and youre supposed to find it, where do you want to go Left or Right?")
side = side.lower()

if side == "left":
    door = input("You are now a step ahead and hence you got a mashal in your hand, now you encounter 3 Doors Red, Green and Blue which door you would want to go?")
    door = door.lower()

    if door=="green":
        treasure = input("You entered the room, and now you see a drawer and a wardrobe, what to open Drawer or Wardrobe?")
        treasure = treasure.lower()
        if treasure == "drawer":
            print("Congratulations you found the treasure")
        else:
            ("You did not reach till the treasure")
    else:
        print("Ghosts found you, Game Over!")
else:
    print("You entered the wrong place, Game Over!")
