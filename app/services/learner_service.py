from __future__ import annotations

from app.core.pattern_learner import PatternLearner


class LearnerService:
    def __init__(self):
        self.learner = PatternLearner()

    def learn_sequence(self, numbers: list[int]):
        self.learner.learn(numbers)

    def predict_next(self) -> int | None:
        return self.learner.predict_next()

    def reset(self):
        self.learner.reset()

    def get_state(self) -> dict:
        return self.learner.get_state()

    def analyze_sequence(self, numbers: list[int], count: int = 1) -> dict:
        return self.learner.analyze(numbers, count)


learner_service = LearnerService()
