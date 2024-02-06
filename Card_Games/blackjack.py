from deck import Deck
from player import Player


class BlackJack:

    def __init__(self):

        self.current_deck = Deck()
        self.current_deck.shuffle_deck()

        self.player = Player(self.current_deck)
        self.house = Player(self.current_deck)

        for i in range(2):
            self.player.draw_player_hand(1)
            self.house.draw_player_hand(1)

    def serialize_state(self):
        return {
            "player_hand": self.player.current_hand,
            "house_hand": self.house.current_hand,
        }

    @staticmethod
    def deserialize_state(state):
        game = BlackJack()

        game.player.current_hand = state["player_hand"]

        game.house.current_hand = state["house_hand"]

        return game

    def calculate_hand(self):
        total_val = 0
        i = 0

        for i in range(len(self.player.current_hand)):
            current_val = int(self.player.current_hand[i][0])
            i += 1

            if (current_val != 1) & (current_val <= 10):
                total_val += current_val
                pass

            if (current_val) > (10):
                current_val = 10
                total_val += current_val
                pass

            if current_val == 1:
                if (total_val + current_val) > (21):
                    current_val = 1
                    total_val += current_val
                    pass
                if (total_val + current_val) < (21):
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

            if (current_val != 1) & (current_val <= 10):
                total_val += current_val
                pass

            if current_val > 10:
                current_val = 10

            if current_val == 1:
                if (total_val + current_val) > (21):
                    current_val = 1
                    total_val += current_val
                    pass
                if (total_val + current_val) < (21):
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

    while game.calculate_hand() < 21:
        game.hit()

        current_val = game.calculate_hand()

        if current_val > 21:
            return 0

    win = False

    house_value = 0
    player_val = game.calculate_hand()

    while win != True:
        house_value = game.calculate_house_hand()

        if (house_value) == (player_val):
            return 2

        if house_value > 21:
            return 1

        if house_value > player_val:
            return 0

        game.house_hit()


def test_results(iterations):
    player_wins = 0
    house_wins = 0
    ties = 0

    for i in range(iterations):
        result = play_blackjack()

        if result == 1:
            player_wins += 1

        if result == 2:
            ties += 1

        if result == 0:
            house_wins += 1

    return player_wins, house_wins, ties
