import ascii

print(ascii.treasure_box)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

lake = 0
door_color = 0

door = input("on this islend you find a mistirious castel, There are two front doors for some reason you cannot undestend, which door do you choose?\n").lower()

if door == "right":
  print(ascii.portal)
  print(" you enter the right door, there is a HUGE portal that starts sokeing you in - game over ")
elif door == "left":
  print(ascii.water)
  lake = input("You enter the left door, there is a huge lake infront of you, you thinking about swimming to the other side of it, but then you notice a boat on the horizen, maybe you can wait for it to arive so you can cross the lake, but you have no idea how long you can wait for the boat.. what do you do? swim or wait?\n").lower()
else:
  print(ascii.grifin)
  print("you didnt choose any of the doors, a magical gripin is flaying so fast towards you, you can barly see it, he grabs you with his mighty claws and take you away from the Treasure island!! Game over!")

if lake == "swim":
  print(ascii.octopus)
  print("You decide you wont wait for god knows how long, and you start swimming. the water feels cold, but you soon get used to it. suddenly, something touches your foot! you start swim faster, but the water monster gets you! Game over!")
elif lake == "wait":
  print(ascii.boat)
  door_color = input("you decide that swimming is rather a dengarous option, and you wait for the boat. finally after probably more than a couple of days, the boat arrived and you hop in. you realize that there is no one on this boat and it's moving with some kind of magical forxes.. you are starting to re-think if swimming was a better option.. \nFinally, you arive at the other side, where you are faced with yet another decition between 3 doors.\nRed door, Yellow door, and Blue door, which one will you choose?\n").lower()
else:
  print("This is not a valid option! a huge tentical monster is trying to get you, and you run out of the door you came from! Game over!")

if door_color == "red":
  print(ascii.fire)
  print("you enter the room, but there is nothing but fire, Game Over!")
elif door_color == "yellow":
  print(ascii.canadian_dollar)
  print("You enter the room and see a Canadian Dolor coin! This one called a loonie! how awesomw is that!! you found the tresure! But of course we all know that it's all about the path we take, enjoying the jorney, and not the end goal! :D")
elif door_color == "blue":
  print(ascii.angry_troll)
  print("you enter the room, and you see this thing staring at you, your only thought is 'NOPE!', Game Over!")