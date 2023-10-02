class Player:

    def __init__(self, deck):
        self.current_hand = list()
        self.current_deck = deck


    def draw_player_hand(self, amount):
        return self.current_hand.extend(self.current_deck.draw_card(amount))
    

    def remove_player_hand(self, pos):
        return self.current_hand.pop(pos - 1)


    def print_hand(self):
        x = 0

        for i in self.current_hand:
            print(self.current_hand[x])
            
            x += 1
    