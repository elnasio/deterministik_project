from .arithmetic import analyze_arithmetic
from .bit_pattern import analyze_bit_pattern
from .cubic import analyze_cubic
from .debug import analyze_debug
from .digit_compression import analyze_digit_compression
from .digit_logic import analyze_digit_logic
from .digit_middle_logic import analyze_digit_middle_logic
from .digit_mirror import analyze_digit_mirror
from .digit_repetition import analyze_digit_repetition
from .digit_sequence import analyze_digit_sequence
from .even import analyze_even
from .factorial import analyze_factorial
from .fibonacci import analyze_fibonacci
from .geometric import analyze_geometric
from .interleaved import analyze_interleaved
from .interleaved_multi import analyze_interleaved_multi
from .modulo_cycle import analyze_modulo_cycle
from .noise_tolerant import analyze_noise_tolerant
from .odd import analyze_odd
from .palindrom import analyze_palindrom
from .pascal import analyze_pascal
from .pascal_grid import analyze_pascal_grid
from .polynomial import analyze_polynomial
from .power_series import analyze_power_series
from .prime import analyze_prime
from .repeating import analyze_repeating
from .second_order import analyze_second_order
from .triangular import analyze_triangular

ALL_ANALYZERS = [
    analyze_interleaved_multi,  # Multi-way interleaved, paling atas!
    analyze_arithmetic,  # Arithmetic sequence
    analyze_second_order,  # Level 2 difference
    analyze_geometric,  # Geometric progression
    analyze_fibonacci,  # Fibonacci sequence
    analyze_prime,  # Prime numbers
    analyze_factorial,  # Factorial
    analyze_triangular,  # Triangular numbers
    analyze_cubic,  # Cubic numbers
    analyze_polynomial,  # General polynomial (degree 2+)
    analyze_modulo_cycle,  # Modulo/cyclic pattern
    analyze_repeating,  # Repeating/cycle difference pattern
    analyze_digit_repetition,  # Repetition in digits
    analyze_bit_pattern,  # Bit-pattern (2ⁿ−1)
    analyze_pascal,  # Pascal triangle
    analyze_power_series,  # Power/base^n
    analyze_noise_tolerant,  # Noise-tolerant arithmetic
    analyze_pascal_grid,  # Flattened Pascal grid
    analyze_digit_mirror,  # Mirror/mountain digits
    analyze_digit_sequence,  # Digit sequence growth
    analyze_digit_compression,  # Digit sum/compression
    analyze_digit_logic,  # Digit logic
    analyze_digit_middle_logic,  # First + last = middle logic
    analyze_even,  # Even numbers (letakkan paling bawah)
    analyze_odd,  # Odd numbers (letakkan paling bawah)
    analyze_palindrom,  # Palindrome (boleh agak bawah)
    analyze_interleaved,  # Single interleaved (lama, boleh bawah)
    analyze_debug,  # Debug/analyzer catch-all (paling akhir)
]
