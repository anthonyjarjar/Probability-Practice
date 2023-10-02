from deck import Deck
from player import Player

class BlackJack:

    def __init__(self):
        print("Welcome to Black Jack!\n")

        self.current_deck = Deck()
        self.current_deck.shuffle_deck()

        self.player = Player(self.current_deck)
        self.house = Player(self.current_deck)

        for i in range(2):
            self.player.draw_player_hand(1)
            self.house.draw_player_hand(1)

        print(f"The current house hand is: [blind] & {self.house.current_hand[1]} \n")
        print(f"The player hand is currently: {self.player.current_hand[0]} & {self.player.current_hand[1]}\n")


    def calculate_hand(self):
        total_val = 0
        i = 0

        for i in range(len(self.player.current_hand)):
            current_val = int(self.player.current_hand[i][0])
            i += 1

            if ((current_val != 1) & (current_val <= 10)):
                total_val += current_val
                pass

            if ((current_val) > (10)):
                current_val = 10 
                total_val += current_val
                pass    

            if current_val == 1: 
                if ((total_val + current_val) > (21)):
                    current_val = 1
                    total_val += current_val
                    pass
                if ((total_val + current_val) < (21)):
                    current_val = 11
                    total_val += current_val
                    pass
        
        return total_val
    

    def calculate_house_hand(self):
        total_val = 0
        i = 0

        for i in range(len(self.house.current_hand)):
            current_val = int(self.house.current_hand[i][0])
            i += 1

            if ((current_val != 1) & (current_val <= 10)):
                total_val += current_val
                pass

            if current_val > 10:
                current_val = 10 

            if current_val == 1: 
                if ((total_val + current_val) > (21)):
                    current_val = 1
                    total_val += current_val
                    pass
                if ((total_val + current_val) < (21)):
                    current_val = 11
                    total_val += current_val
                    pass

            total_val += current_val

        
        return total_val


    def hit(self):
        self.player.draw_player_hand(1)

    def house_hit(self):
        self.house.draw_player_hand(1)

    def print_player_hand(self):
        self.player.print_hand()


def play_blackjack():

    game = BlackJack()

    print(f"The current player's value is {game.calculate_hand()}")

    players_choice = input("\n--------------- Hit or stand? (h/s) ---------------\n")

    current_val = 0

    while players_choice == 'h':
        game.hit()

        current_val = game.calculate_hand()

        print("Current Player Hand: ")
        game.print_player_hand()

        print(f"\nPlayer's value: {current_val}")

        if current_val > 21:
            print("\nYOU LOST, HOUSE WON!")
            return 0

        players_choice = input("\n--------------- Hit or stand? (h/s) ---------------\n")

    win = False
    print("Current House Hand: ")
    game.house.print_hand()
    house_value = 0
    player_val = game.calculate_hand()
    print(game.calculate_house_hand())

    while win != True:
        house_value = game.calculate_house_hand()

        if (house_value) == (player_val):
            print("Current House Hand: ")
            game.house.print_hand()
            print(f"\nIt's a tie! House value: {house_value}\n")
            return 0

        if house_value > 21:
            print("Current House Hand: ")
            game.house.print_hand()
            print(f"\n House value: {house_value} \n HOUSE LOST! YOU WON!")
            return 0

        if house_value > player_val:
            print("Current House Hand: ")
            game.house.print_hand()
            print(f"\n House value: {house_value} \n Player value: {player_val} \n HOUSE WON! ")
            return 0
        
        game.house_hit()

play_blackjack()
