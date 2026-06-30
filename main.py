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


from pathlib import Path
from core.deck import Deck
from core.card import Card
from core.session import Session


def show_skill_check(card: Card):
    print("\n--- SKILL CHECK ---")
    print(card.sentence)
    print(f"Виділено: {card.get_highlighted_text()}")
    print("Варіанти:")
    for i, option in enumerate(card.options):
        print(f"  {i}: {option}")


def main():
    deck = Deck()
    deck.load_from_file(Path("data/cards.json"))
    print(f"Завантажено карток: {len(deck.cards)}")

    session = Session(deck, duration=10)
    session.on_skill_check = show_skill_check
    session.start()

    print("\nПочинаємо симуляцію...")

    for _ in range(3):
        session.tick(5.0)
        print(
            f"Час: {session.elapsed_time:.1f}, "
            f"прогрес: {session.progress}, "
            f"активна: {session.is_running}"
        )

    print(f"\nПравильних: {session.correct_answers}")
    print(f"Неправильних: {session.wrong_answers}")

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
