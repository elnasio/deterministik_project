from __future__ import annotations

from app.core.patterns import ALL_ANALYZERS


class PatternLearner:
    def __init__(self):
        self.sequence = []
        self.diff = None
        self.level2_diff = None
        self.is_prime_sequence = False

    def reset(self):
        self.sequence.clear()
        self.diff = None
        self.level2_diff = None
        self.is_prime_sequence = False

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def learn(self, numbers: list[int]):
        self.sequence = numbers
        self.is_prime_sequence = all(self.is_prime(n) for n in numbers if n > 1) and len(
            [n for n in numbers if self.is_prime(n)]) >= 3

        if len(numbers) >= 2 and not self.is_prime_sequence:
            diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
            if len(set(diffs)) == 1:
                self.diff = diffs[0]
            else:
                level2_diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
                if len(set(level2_diffs)) == 1:
                    self.level2_diff = level2_diffs[0]

    def analyze(self, numbers: list[int], count: int = 1) -> dict:
        for checker in ALL_ANALYZERS:
            result = checker(numbers, count)
            if result:
                return result
        return {"pattern": "unknown", "next_number": None}

    def next_prime(self, n: int) -> int:
        candidate = n + 1
        while not self.is_prime(candidate):
            candidate += 1
        return candidate

    def predict_next(self) -> int | None:
        if self.diff is not None:
            return self.sequence[-1] + self.diff
        elif self.level2_diff is not None and len(self.sequence) >= 3:
            diffs = [self.sequence[i + 1] - self.sequence[i] for i in range(len(self.sequence) - 1)]
            next_diff = diffs[-1] + self.level2_diff
            return self.sequence[-1] + next_diff
        elif self.is_prime_sequence:
            return self.next_prime(self.sequence[-1])
        return None

    def get_state(self) -> dict:
        return {
            "sequence": self.sequence,
            "diff": self.diff,
            "level2_diff": self.level2_diff,
            "is_prime_sequence": self.is_prime_sequence
        }
