class Card:
    def __init__(
        self,
        sentence: str,
        highlight_start: int,
        highlight_end: int,
        options: list[str],
        correct_index: int,
        tags: list[str] | None = None,
    ) -> None:
        self.sentence = sentence
        self.highlight_start = highlight_start
        self.highlight_end = highlight_end
        self.options = options
        self.correct_index = correct_index
        self.tags = tags if tags is not None else []

        if len(self.options) != 4:
            raise ValueError(
                f"Card must have exactly 4 options, got {len(self.options)}"
            )
        if not (0 <= self.correct_index <= 3):
            raise ValueError(
                f"correct_index must be between 0 and 3, got {self.correct_index}"
            )
        if self.highlight_start < 0 or self.highlight_end > len(self.sentence):
            raise ValueError(
                f"Highlight indices are out of sentence bounds"
            )
        if self.highlight_start >= self.highlight_end:
            raise ValueError(
                f"highlight_start must be less than highlight_end"
            )


    def get_highlighted_text(self) -> str:
        return self.sentence[self.highlight_start:self.highlight_end]


    def is_correct(self, index: int) -> bool:
        return index == self.correct_index

    def __repr__(self) -> str:
        return (
            f"Card("
            f"sentence={self.sentence!r}, "
            f"highlight={self.get_highlighted_text()!r}, "
            f"correct={self.options[self.correct_index]!r}"
            f")"
        )

    def to_dict(self) -> dict:
        return {
            "sentence": self.sentence,
            "highlight_start": self.highlight_start,
            "highlight_end": self.highlight_end,
            "options": self.options,
            "correct_index": self.correct_index,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Card":
        return cls(
            sentence=data["sentence"],
            highlight_start=data["highlight_start"],
            highlight_end=data["highlight_end"],
            options=data["options"],
            correct_index=data["correct_index"],
            tags=data.get("tags", []),
        )
