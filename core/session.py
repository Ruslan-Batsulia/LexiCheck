import random
from core.deck import Deck
from core.card import Card
from typing import Callable


class Session:
    def __init__(self, deck: Deck, duration: int = 300) -> None:
        self.deck: Deck = deck
        self.duration: int = duration
        self.elapsed_time: float = 0.0
        self.progress: float = 0.0
        self.is_running: bool = False
        self.next_check_time: float = 0.0
        self.skill_check_active: bool = False

        self.correct_answers: int = 0
        self.wrong_answers: int = 0

        self.on_skill_check: Callable[[Card], None] | None = None

    def start(self) -> None:
        self.is_running = True
        self.schedule_next_check()

    def stop(self) -> None:
        self.is_running = False

    def schedule_next_check(self) -> None:
        interval = random.uniform(45.0, 120.0)
        self.next_check_time = self.elapsed_time + interval

    def on_correct_answer(self) -> None:
        self.progress = min(100.0, self.progress + 5.0)
        self.correct_answers += 1
        self.skill_check_active = False
        self.schedule_next_check()

    def on_wrong_answer(self) -> None:
        self.progress = max(0.0, self.progress - 15.0)
        self.wrong_answers += 1
        self.skill_check_active = False
        self.schedule_next_check()

    def on_timeout(self) -> None:
        self.progress = max(0.0, self.progress - 15.0)
        self.wrong_answers += 1
        self.skill_check_active = False
        self.schedule_next_check()

    def tick(self, dt: float) -> None:
        if not self.is_running:
            return

        self.elapsed_time += dt

        if self.elapsed_time >= self.duration:
            self.stop()
            return

        if self.skill_check_active:
            return

        if self.elapsed_time >= self.next_check_time:
            card = self.deck.get_random_card()
            if card is None:
                self.schedule_next_check()
                return
            self.skill_check_active = True
            if self.on_skill_check:
                self.on_skill_check(card)
