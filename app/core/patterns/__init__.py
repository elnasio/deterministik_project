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
    analyze_prime,
    analyze_arithmetic,
    analyze_geometric,
    analyze_fibonacci,
    analyze_even,
    analyze_odd,
    analyze_factorial,
    analyze_second_order,
    analyze_repeating,
    analyze_triangular,
    analyze_cubic,
    analyze_modulo_cycle,
    analyze_digit_repetition,
    analyze_polynomial,
    analyze_interleaved,
    analyze_palindrom,
    analyze_bit_pattern,
    analyze_pascal,
    analyze_power_series,
    analyze_interleaved_multi,
    analyze_noise_tolerant,
    analyze_pascal_grid,
    analyze_digit_mirror,
    analyze_digit_sequence,
    analyze_digit_compression,
    analyze_digit_logic,
    analyze_digit_middle_logic,
    analyze_debug,
]
