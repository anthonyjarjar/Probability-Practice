from random import randint
from unshuffled import suits, values


class Deck:

    def __init__(self):
        self.current_deck = list()
        self.deck_len = 52


    def shuffle_deck(self):
        card_count = 0

        while card_count != self.deck_len:
            suit_int = randint(0,3)
            value_int = randint(0,12)

            temp = (values[value_int], suits[suit_int])

            if temp in self.current_deck:
                pass
            else:
                self.current_deck.append(temp)
                card_count += 1


    def draw_card(self, card_amount):
        current_draw = []

        for i in range(card_amount):
            current_draw.append(self.current_deck[0])
            self.current_deck.pop(0)
            self.deck_len -= 1

        return current_draw


    def print_deck(self):
        x = 0

        for i in self.current_deck:
            print(self.current_deck[x])
            
            x += 1

        return print(len(self.current_deck))
    