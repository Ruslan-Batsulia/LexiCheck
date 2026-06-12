import json
import random
from pathlib import Path
from core.card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, index: int) -> Card:
        return self.cards.pop(index)

    def get_random_card(self) -> Card | None:
        return random.choice(self.cards) if self.cards else None

    def save_to_file(self, path: Path) -> None:
        data = [card.to_dict() for card in self.cards]

        with open(path, "w", encoding="utf-8") as file:
            json.dump({"cards": data}, file, ensure_ascii=False, indent=2)

    def load_from_file(self, path: Path) -> None:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.cards = [Card.from_dict(card) for card in data["cards"]]
