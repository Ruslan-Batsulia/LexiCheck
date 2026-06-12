# LexiCheck
# Copyright (C) 2025  Ruslan Batsulia
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


# from core.deck import Deck
# from core.card import Card
# from pathlib import Path


def main():
    pass
    # deck = Deck()

    # deck.add_card(Card(
    #     "Define a variable to store the user's name.",
    #     0,
    #     6,
    #     [
    #         "викликати (функцію)",
    #         "повертати (значення)",
    #         "визначити / оголосити",
    #         "реалізувати / впровадити",
    #     ],
    #     2,
    # ))

    # deck.add_card(Card(
    #     "Implement the function that returns the sum.",
    #     0,
    #     9,
    #     [
    #         "фрагмент коду",
    #         "помилка в коді / баг",
    #         "застарілий / не рекомендований",
    #         "реалізувати / впровадити",
    #     ],
    #     3,
    # ))

    # save_path = Path("data/cards.json")
    # save_path.parent.mkdir(parents=True, exist_ok=True)
    # deck.save_to_file(save_path)
    # print("Збережено!")

    # deck.load_from_file(save_path)
    # print(f"Завантажено карток {len(deck.cards)}")
    # for card in deck.cards:
    #     print(card)


if __name__ == "__main__":
    main()
