import pytest

from app.services.learner_service import learner_service


@pytest.mark.parametrize("numbers,prediction,expected_pattern", [
    # Arithmetic progression
    ([2, 4, 6, 8], [10, 12], "arithmetic"),
    # Second-order difference
    ([1, 4, 9, 16], [25, 36], "second_order"),
    # Prime
    ([2, 3, 5, 7], [11, 13], "prime"),
    # Geometric
    ([3, 6, 12, 24], [48, 96], "geometric"),
    # Fibonacci
    ([1, 1, 2, 3, 5], [8, 13], "fibonacci"),
    # Factorial (next_number=[720])
    ([1, 2, 6, 24, 120], [720], "factorial"),
    # Even
    ([2, 4, 6, 8], [10, 12], "even"),
    # Odd
    ([1, 3, 5, 7], [9, 11], "odd"),
    # Interleaved 2-way: (even/odd)
    ([2, 1, 4, 3, 6, 5], [8, 7], "interleaved_2_way"),
    # Interleaved 3-way, seperti kasus custom
    ([2, 3, 4, 5, 6, 8, 8, 11, 16, 11, 18, 32], [14, 27, 64], "interleaved_3_way"),
])
def test_patterns(numbers, prediction, expected_pattern):
    count = len(prediction)
    result = learner_service.analyze_sequence(numbers, count)
    assert result["pattern"].startswith(expected_pattern)
    assert result["next_number"] == prediction
