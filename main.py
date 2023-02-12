
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

lake = 0
door_color = 0

door = input("on this islend you find a mistirious castel, There are two front doors for some reason you cannot undestend, which door do you choose?\n").lower()

if door == "right":
  print('''
  XXXXXX      ~.                            .                       -                              .~    XXXXXXXXXXXX
XXXXXXXXXX'         ~.                           \                     /                             .~       `XXXXXXXXXX
XXXXXXXXX'            ~.                          -                   .                            .~          `XXXXXXXXX
  `XXX' T               ~.                         \                 /                           .~             T `XXX'
  ,XXX. |                 ~.                        .               -                          .~               | ,XXX.
XXX` 'XXX                   ~.                       \             /                         .~                 XXX` 'XXX
XXX. ,XXX                     ~.                      .6&&&&&&&&&A,                        .~                   XXX. ,XXX
  `XXX' T                       ~.             .6&&&&&&&&&&&&&&&&&&&&&&&A,               .~                     T `XXX'
  ,XXX. |._                       ~.     .6&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&A,       .~                     _.| ,XXX.
XXX` 'XXX  ~-._                     ~.6&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&A,~                   _.-~  XXX` 'XXX
XXX. ,XXX      ~-._              6&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&A              _.-~      XXX. ,XXX
  `XXX' T          ~-._       6&&&&&&&&&&&&&&&&&&/"""""""""""""""""""""\&&&&&&&&&&&&&&&&&&A       _.-~          T `XXX'
  ,XXX. |              ~-._ 6&&&&&&&&&&&&&&&/                               \&&&&&&&&&&&&&&&A _.-~              | ,XXX.
XXX` 'XXX                  &&&&&&&&&&&&&/                                       \&&&&&&&&&&&&&                  XXX` 'XXX
XXX. ,XXX                  &&&&&&&&&&/          ,              __._    _.'         \&&&&&&&&&&                  XXX. ,XXX
  `XXX' T                  && $                                    `-.'                   $ &&                  T `XXX'
  ,XXX. |~~..__            &&$         _.      .                                           $&&            __..~~| ,XXX.
XXX` 'XXX      ~~..__      && $       ~                  _ -'- _                          $ &&      __..~~      XXX` 'XXX
XXX. ,XXX            ~~..__&&$     .-~             _ - '   .-.   ' - _        *            $&&__..~~            XXX. ,XXX
  `XXX' T                  && $                _~~   .    /7 t\  +     ~~_                $ &&                  T `XXX'
  ,XXX. |                  &&$                ._  -  _   /7   t\  .   _  _.         *'     $&&                  | ,XXX.
XXX` 'XXX                  && $     *           '- , _  /7     t\  _ , -'                 $ &&                  XXX` 'XXX
XXX. ,XXX                  &&$                         | |     | |                         $&&                  XXX. ,XXX
  `XXX' T                  && $                        | |_   _| |                        $ &&                  T `XXX'
  ,XXX. |_________________.&&$  . .     . _ .  _    _.-| | /'\ | |-._     _    . ,  _  . . $&&._________________| ,XXX.
XXX` 'XXX                  && $__________________.-~   |_|/___\|_|   ~-.__________________$ &&                  XXX` 'XXX
XXX. ,XXX                  &&$                  |'-._               _.-'|              ~~  $&&                  XXX. ,XXX
  `XXX' T                  && $          ~      |####'-._       _.-'####|    ~~_          $ &&                  T `XXX'
  ,XXX. |                  &&$   ~              |#   #.-~  .    ~-.#   #|                  $&&                  | ,XXX.
XXX` 'XXX                  && $            ~~   |# .-~   __  _  .  ~-. #|                 $ &&                  XXX` 'XXX
XXX. ,XXX            __..~~&&$       ~~-        .-~  __       __  .   ~-.         ~        $&&~~..__            XXX. ,XXX
  `XXX' T      __..~~      && $              .-~  _     ___        __    ~-.              $ &&      ~~..__      T `XXX'
  ,XXX  |__..~~            &&$            .-~      ___         ___      __  ~-.      _~    $&&            ~~..__| ,XXX.
XXX` 'XXX                  && $        .-~    ___        ___         ___       ~-.        $ &&                  XXX` 'XXX
XXX. ,XXX                  &&$    ~~.-~____        ____        ____        ____   ~-.      $&&                  XXX. ,XXX
  `XXX' T                  && $  .-~        ________         ________           ___  ~-.  $ &&                  T `XXX'
  ,XXX. |                _.&&$.-~                                                       ~-.$&&._                | ,XXX.
XXX` 'XXX            _.-~ &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ~-._            XXX` 'XXX
XXX. ,XXX        _.-~   _&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&_   ~-._        XXX. ,XXX
  `XXX' T    _.-~     -'-------------------------------------------------------------------------`-     ~-._    T `XXX'
  ,XXX. |_.-~       _&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&_       ~-._| ,XXX.
XXX` 'XXXT        -'---------------------------------------------------------------------------------`-        TXXX` 'XXX
XXX. ,XXX|      _&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&_      |XXX. ,XXX
XXXXXXXXX!____-'-----------------------------------------------------------------------------------------`-____!XXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPraseodymium 59
  ''')
  print(" you enter the right door, there is a HUGE portal that starts sokeing you in - game over ")
elif door == "left":
  print("""
                ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^
  """)
  lake = input("You enter the left door, there is a huge lake infront of you, you thinking about swimming to the other side of it, but then you notice a boat on the horizen, maybe you can wait for it to arive so you can cross the lake, but you have no idea how long you can wait for the boat.. what do you do? swim or wait?\n").lower()
else:
  print("""
                                                       ,|
                                                   -~.|
                                                _-~  /
                                             _-~    /_-~|
                                         _ -~     _-~ ,/'
                                   __--~~__--\ _-~  _/,
                             __--~~  --~~  __/~  _-~ /
                            /        __--~~  \-~~ _-~
                           /     --~~   __--~' _-~ ~|
                          /     ___---~~  ~~\~~__--~
        _.---.           /           __--~~~'~~/  _.-~"~~-.
     .-"      "=\ __    /      ~~~~~__\__---~~_.-~  _.--.  )
    (_ .-b=-   =:Y  ~~~/      ---~~~/__-----=~   ,-~__.'  ,'
   /  __      =:;l    /      ----~~/            Y (____.-"
  / o~  "c    =~:l    (      ---~~/     __  `:::|
 (  .--~"~-._=~;/'___  `----~~~~'     ,'  `\  `:|
  \(       ( ~~ ,'  ,`\              (      `\ /
.=z.       `>.-~   /   )          ___.\_     `Y.
   \`------}    .-"  _/"~~~----~~~ __./'        )
 .==)_.<---}_   __.-~          ,-~~         ,-~'
       \\    "~"              :      __.--"~
        ))                     `((((~~     -Chuckles-
  """)
  print("you didnt choose any of the doors, a magical gripin is flaying so fast towards you, you can barly see it, he grabs you with his mighty claws and take you away from the Treasure island!! Game over!")

if lake == "swim":
  print("""
  
                        ___
                     .-'   `'.
                    /         \
                    |         ;
                    |         |           ___.--,
           _.._     |0) ~ (0) |    _.---'`__.-( (_.
    __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
   ( ,.--'`   ',__ /./;   ;, '.__.'`    __
   _`) )  .---.__.' / |   |\   \__..--""  ""--.,_
  `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
        | |  .' _.-' |  |  \  \  '.               `~---`
         \ \/ .'     \  \   '. '-._)
          \/ /        \  \    `=.__`~-.
     jgs  / /\         `) )    / / `"".`\
    , _.-'.'\ \        / /    ( (     / /
     `--~`   ) )    .-'.'      '.'.  | (
            (/`    ( (`          ) )  '-;
             `      '-;         (-'
  """)
  print("You decide you wont wait for god knows how long, and you start swimming. the water feels cold, but you soon get used to it. suddenly, something touches your foot! you start swim faster, but the water monster gets you! Game over!")
elif lake  == "wait":
  print("""
                   ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-----' ,
       ___.....-----''-----/
 jgs   \                  /
   ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^
  """)
  door_color = input("you decide that swimming is rather a dengarous option, and you wait for the boat. finally after probably more than a couple of days, the boat arrived and you hop in. you realize that there is no one on this boat and it's moving with some kind of magical forxes.. you are starting to re-think if swimming was a better option.. \nFinally, you arive at the other side, where you are faced with yet another decition between 3 doors.\nRed door, Yellow door, and Blue door, which one will you choose?\n")
else:
  print("This is not a valid option! a huge tentical monster is trying to get you, and you run out of the door you came from! Game over!")


if door_color == "Red" or door_color == "red":
  print("""
                 (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")
  print("you enter the room, but there is nothing but fire, Game Over!")
elif door_color == "Yellow" or door_color == "yellow":
  print('''
  
               ,,==="""""""===,,
           ,==""' |\ |   /\   `""==,
        ,="'|\    | \|  /__\   /\  `"=,
      /"    |,"\  |  | /'  `\ /  )     "\ 
    /"  ,"  |                 `\/    /|  "\\n
   /'  |   ,                       /",|   `\\n
  /'   ",/"                           |    `\\n
 /'      I=I=I               ,d8ba,___      `\\n
/'     I=8=8=8=I_I_          88888P"""       `\\n
|   xXXXXXXXXXXXXXXXxIxx    ,888"             |
| ~XXXXXXXXXXXXXXX~-~-~-~-~ d888~-~-~-~-~-~-~ |
| ~-~-~-~-~-~-~-~-,aad888ba,8888,-~-~-~-~-~-~ |
| ~-~-~-~-~-~-,ad888888888888888b-~-~-~-~-~-~ |
\ ~-~-~-~-~,ad8888888888888888888-~-~-~-~-~-~ /
`\ -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~- /'
 `\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,-,~~~~~ /'
  `\    /"\         1 9 9 4        \ /\    /'
   `\  "\,/'                   |\   `\ `  /'
     "\      /""\   |    |     |,'\     /"
       `"=,_ \__/   |__  |__   |    ,="'  Normand
          `""=,__             __,=""'     Veilleux
               ``""=========""
               ''')
  print("You enter the room and see a Canadian Dolor coin! This one called a loonie! how awesomw is that!! you found the tresure! But of course we all know that it's all about the path we take, enjoying the jorney, and not the end goal! :D")
elif door_color == "Blue" or door_color == "blue":
  print("""
  
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
  """)
  print("you enter the room, and you see this thing staring at you, your only thought is 'NOPE!', Game Over!")
