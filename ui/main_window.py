import pyglet
from core.deck import Deck
from core.card import Card
from core.session import Session
from pyglet.window import Window


class MainWindow(Window):
    def __init__(self, deck: Deck) -> None:
        super().__init__(
            width = 500,
            height = 300,
            caption = "LexiCheck",
        )

        self.session = Session(deck, duration = 300)
        self.session.on_skill_check = self.show_skill_check
        self.session.start()

        pyglet.clock.schedule_interval(self.update, 1.0)

        self.label = pyglet.text.Label(
            "Прогрес 0%",
            font_name = "Arial",
            font_size = 24,
            color = (0, 0, 0, 255),
            x = 20,
            y = self.height - 50,
        )

    def update(self, dt: float) -> None:
        self.session.tick(dt)

        self.label.text = (
            f"Прогрес: {self.session.progress:.0f}%   "
            f"Час: {self.session.elapsed_time:.0f}/{self.session.duration}с"
        )

    def show_skill_check(self, card: Card) -> None:
        print(f"SKILL CHECK: {card.sentence}")

    def on_draw(self) -> None:
        self.clear()
        pyglet.gl.glClearColor(0.95, 0.95, 0.95, 1.0)
        self.label.draw()
