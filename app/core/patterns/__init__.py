from .arithmetic import analyze_arithmetic
from .cubic import analyze_cubic
from .debug import analyze_debug
from .digit_repetition import analyze_digit_repetition
from .even import analyze_even
from .factorial import analyze_factorial
from .fibonacci import analyze_fibonacci
from .geometric import analyze_geometric
from .modulo_cycle import analyze_modulo_cycle
from .odd import analyze_odd
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
    analyze_debug,
]
