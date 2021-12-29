_______ t__
_______ random

____ actors _______ Wizard, Creature, SmallAnimal, Dragon


___ main():
    print_header()
    game_loop()


___ print_header():
    # Yes, I added this after I recorded the video
    # but I thought you'd get a kick out if it. ;)
    print()
    print('-----------------------------------------------------------------------')
    print('''
   (  )   /\   _                 (
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \\
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
     WIZARD BATTLE        )        \_____________  `              \  /
(__       APP      +- .( -'.- <. - _  VVVVVVV VV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \\
    ''')
    print()
    print('-----------------------------------------------------------------------')
    print()


___ game_loop():
    creatures  [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, T..),
        Wizard('Evil Wizard', 1000)
    ]

    # print(creatures)

    hero  Wizard('Gandolf', 75)

    w___ T...

        active_creature  random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd  input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        __ cmd __ 'a':
            __ hero.attack(active_creature):
                creatures.remove(active_creature)
            ____:
                print("The wizard runs and hides taking time to recover...")
                t__.sleep(5)
                print("The wizard returns revitalized!")
        ____ cmd __ 'r':
            print('The wizard has become unsure of his power and flees!!!')
        ____ cmd __ 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            ___ c __ creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        ____:
            print("OK, exiting game... bye!")
            _____

        __ n.. creatures:
            print("You've defeated all the creatures, well done!")
            _____

        print()


__ __name__ __ '__main__':
    main()
