import Game
import Player

def main():
    game_obj = Game.Game()

    choice = input('=== Welcome to the card game War! === \nPlease input the number of the desired mode'
        '\n1) Versus Computer\n2) Versus Player\n>> ')

    while choice != 1 or choice != 2:
        choice = input('Please input either 1 or 2 from the menu')

    is_player = False
    if choice == 1:
        is_player = True

    name1 = input('Player 1, what is your name?\n>> ')
    name2 = input('What is your opponents name?\n>> ')
    hand1 = list()
    hand2 = list()
    game_obj.deck.give_hands(hand1, hand2)
    game_obj.player1 = Player.Player(name1, hand1, 1)
    game_obj.player2 = Player.Player(name2, hand2, is_player)

    match = game_obj.start()
    while match:
        pass

    

if __name__ == '__main__':
    main()
