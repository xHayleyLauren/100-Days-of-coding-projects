print(r'''


                        /\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
     ` ``


''')
print("Welcome Dragon Warrior.")
print("Your mission is to find the Marauder's scroll.")
left_or_right = input("You've come at a crossroad. Do you go left or right?")
if left_or_right.lower() == "left":
    print("You've made the right choice and found a castle.")
    tower_or_water = input("Will you climb the tower or swim in through the water? "
                           "Type 'tower' to climb the tower. Type 'water' to swim ")

    if tower_or_water.lower() == "water":
        print("You've entered the castle without being seen by the guards. Great job!")
        colour_of_door = input("you found the secret room and are now face with 3 doors."
                               " A black door, a white door and a brown door."
                                "Which colour door will you enter? ")

        if colour_of_door.lower() == "white":
            print("You've found a the Marauder's scroll. Congratulations!")
        elif colour_of_door.lower() == "black":
            print("You've been cursed by the Black Druid and died. Game over")
        elif colour_of_door.lower() =="brown":
            print("You've fallen down into the Eternal Snakepit. Game over")
        else:
            print("That wasn't an option."
                  "The Black Druid spotted you and cursed you"
                  "Game Over")
    else:
        print("You've been shot down by the guards. Game over")
else: print("You chose poorly and died. Game over")
