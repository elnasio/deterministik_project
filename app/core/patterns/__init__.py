from .arithmetic import analyze_arithmetic
from .prime import analyze_prime
from .geometric import analyze_geometric
from .fibonacci import analyze_fibonacci
from .even import analyze_even
from .odd import analyze_odd
from .factorial import analyze_factorial
from .second_order import analyze_second_order

ALL_ANALYZERS = [
    analyze_prime,
    analyze_arithmetic,
    analyze_geometric,
    analyze_fibonacci,
    analyze_even,
    analyze_odd,
    analyze_factorial,
    analyze_second_order,
]
