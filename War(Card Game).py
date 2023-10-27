from random import shuffle
import re

class Card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        return (self.value, self.suit) < (other.value, other.suit)

    def __gt__(self, other):
        return (self.value, self.suit) > (other.value, other.suit)

    def __repr__(self):
        return f"{self.values[self.value]} of {self.suits[self.suit]}"

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in range(2, 15) for suit in range(4)]
        shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        return None

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.hand = []

class Game:
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player(self.get_valid_name("Player 1 name: "))
        self.p2 = Player(self.get_valid_name("Player 2 name: "))

    def get_valid_name(self, prompt):
        while True:
            name = input(prompt)
            if not re.search(r"\W", name):
                return name
            else:
                print("Please, don't use special characters")

    def display_winner(self, winner):
        print(f"{winner} wins this round")

    def draw(self, p1, p2):
        print(f"{p1.name} drew {p1.hand[-1]} | {p2.name} drew {p2.hand[-1]}")

    def play_game(self):
        print("Beginning War!")
        while len(self.p1.hand) < len(self.deck.cards):
            response = input("Press 'q' to quit, or any key to play: ")
            if response == "q":
                break
            p1_card = self.deck.draw_card()
            p2_card = self.deck.draw_card()
            self.p1.hand.append(p1_card)
            self.p2.hand.append(p2_card)
            self.draw(self.p1, self.p2)
            if p1_card > p2_card:
                self.p1.wins += 1
                self.display_winner(self.p1.name)
            elif p1_card < p2_card:
                self.p2.wins += 1
                self.display_winner(self.p2.name)

        winner = self.winner(self.p1, self.p2)
        print(f"War is over. {winner} wins")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

if __name__ == "__main__":
    game = Game()
    game.play_game()
