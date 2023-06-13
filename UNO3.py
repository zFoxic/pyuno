from dataclasses import dataclass
from random import shuffle

@dataclass
class Card:
    color: str = ""
    rank: str = ""
    is_wild = False

    def __post_init__(self):
        if not self.is_wild:
            self.display_value = f'{self.color[0]}-{self.rank}'

@dataclass
class WildCard(Card):
    color = "wild"
    rank = "choose"
    is_wild = True
    display_value = "WILD CHOOSE!"

@dataclass
class Draw4Card(WildCard):
    rank = "draw 4"
    display_value = "WILD DRAW 4!"

deck = []
color_list =  ["red", "yellow", "blue", "green"]
for color in color_list:
    for num in range(0,10):
        deck.append(Card(color, str(num)))
    deck.append(Card(color, "skip"))
    deck.append(Card(color, "reverse"))
    deck.append(Card(color, "draw 2"))
deck.append(WildCard())
deck.append(Draw4Card())

#shuffle(deck)


print([e.display_value for e in deck])
   