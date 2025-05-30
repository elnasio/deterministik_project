from app.core.constants import *


def generate_dataset():
    return [
        # Arithmetic
        {SEQUENCE_LABEL: [2, 4, 6, 8], "label": "arithmetic"},
        {SEQUENCE_LABEL: [10, 15, 20, 25], "label": "arithmetic"},

        # Second-order difference (quadratic)
        {SEQUENCE_LABEL: [1, 4, 9, 16], "label": "second_order"},
        {SEQUENCE_LABEL: [0, 1, 4, 9], "label": "second_order"},

        # Prime
        {SEQUENCE_LABEL: [2, 3, 5, 7], "label": "prime"},
        {SEQUENCE_LABEL: [11, 13, 17, 19], "label": "prime"},

        # Geometric
        {SEQUENCE_LABEL: [3, 6, 12, 24], "label": "geometric"},
        {SEQUENCE_LABEL: [2, 4, 8, 16], "label": "geometric"},

        # Fibonacci
        {SEQUENCE_LABEL: [1, 1, 2, 3], "label": "fibonacci"},
        {SEQUENCE_LABEL: [2, 3, 5, 8], "label": "fibonacci"},

        # Even
        {SEQUENCE_LABEL: [2, 4, 6, 8], "label": "even"},
        {SEQUENCE_LABEL: [10, 12, 14, 16], "label": "even"},

        # Odd
        {SEQUENCE_LABEL: [1, 3, 5, 7], "label": "odd"},
        {SEQUENCE_LABEL: [9, 11, 13, 15], "label": "odd"},

        # Factorial
        {SEQUENCE_LABEL: [1, 2, 6, 24], "label": "factorial"},
        {SEQUENCE_LABEL: [2, 6, 24, 120], "label": "factorial"},

        # Triangular (n*(n+1)/2)
        {SEQUENCE_LABEL: [1, 3, 6, 10], "label": "triangular"},
        {SEQUENCE_LABEL: [10, 15, 21, 28], "label": "triangular"},

        # Cubic
        {SEQUENCE_LABEL: [1, 8, 27, 64], "label": "cubic"},
        {SEQUENCE_LABEL: [0, 1, 8, 27], "label": "cubic"},

        # Polynomial
        {SEQUENCE_LABEL: [1, 4, 11, 22], "label": "polynomial"},
        {SEQUENCE_LABEL: [1, 6, 17, 34], "label": "polynomial"},

        # Pascal Triangle Row
        {SEQUENCE_LABEL: [1, 3, 3, 1], "label": "pascal"},
        {SEQUENCE_LABEL: [1, 4, 6, 4, 1], "label": "pascal"},

        # Flattened Pascal Grid
        {SEQUENCE_LABEL: [1, 2, 1, 3, 3, 1], "label": "pascal_grid"},
        {SEQUENCE_LABEL: [1, 5, 10, 10, 5, 1], "label": "pascal_grid"},

        # Power Series
        {SEQUENCE_LABEL: [1, 2, 4, 8, 16], "label": "power_series"},
        {SEQUENCE_LABEL: [3, 9, 27, 81], "label": "power_series"},

        # Interleaved
        {SEQUENCE_LABEL: [1, 100, 2, 99, 3, 98], "label": "interleaved"},
        {SEQUENCE_LABEL: [5, 10, 4, 9, 3, 8], "label": "interleaved"},

        # Interleaved Multi
        {SEQUENCE_LABEL: [1, 10, 2, 20, 3, 30], "label": "interleaved_multi"},

        # Repeating / Cyclic
        {SEQUENCE_LABEL: [1, 2, 3, 1, 2, 3], "label": "digit_repetition"},
        {SEQUENCE_LABEL: [7, 8, 7, 8], "label": "digit_repetition"},

        # Palindromes
        {SEQUENCE_LABEL: [1, 2, 3, 2, 1], "label": "palindrom"},
        {SEQUENCE_LABEL: [4, 5, 6, 5, 4], "label": "palindrom"},

        # Digit Growth
        {SEQUENCE_LABEL: [1, 11, 111], "label": "digit_growth"},
        {SEQUENCE_LABEL: [3, 33, 333], "label": "digit_growth"},

        # Digit Compression (e.g., sum of digits)
        {SEQUENCE_LABEL: [123, 6, 222, 6], "label": "digit_compression"},

        # Noise-tolerant Arithmetic
        {SEQUENCE_LABEL: [2, 5, 7, 10], "label": "noise_tolerant"},

        # Mirror / Mountain Digits
        {SEQUENCE_LABEL: [1, 3, 5, 3, 1], "label": "mirror"},
        {SEQUENCE_LABEL: [2, 4, 6, 4, 2], "label": "mirror"},

        # Digit Logic
        {SEQUENCE_LABEL: [10, 12, 14, 16], "label": "digit_logic"},

        # Digit Multiplication
        {SEQUENCE_LABEL: [2, 4, 8, 16], "label": "digit_mult"},
        {SEQUENCE_LABEL: [3, 6, 12, 24], "label": "digit_mult"}
    ]
