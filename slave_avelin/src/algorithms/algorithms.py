# from functools import wraps

from ..typewriters.typewriters import Typewriter, new_indent


################################################################################
### Default values
################################################################################

# _DEFAULT_PRINTER = LazyPrinter


################################################################################
### Algorithms
################################################################################


def gcd(a: int, b: int, twr: Typewriter) -> int:
    def gcd(a: int, b: int, twr: Typewriter) -> int:
        """TODO: write comment
        """
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError(f"Error: gcd doesn't support ({type(a)}, {type(b)}) values")

        if a < 0 or b < 0:
            raise ValueError(f"Error: gcd doesn't support negative values")
        
        if a == 0:
            return b
        
        if b == 0:
            return a
        
        if a == 1 or b == 1:
            return 1
        
        if a < b:
            a, b = b, a

        twr.ind_type(f"Calculate: gcd({a}, {b})")

        rez = None
        with new_indent(twr) as twr:
            rez = _gcd_euclid(a, b, twr)

        twr.ind_type(f"gcd({a}, {b}) = {rez}")

        return rez

    def _gcd_euclid_iteration(r_0: int, r_1: int, r_2: int, twr: Typewriter) -> tuple:
        r_0 = r_1
        r_1 = r_2
        r_2 = r_0 % r_1

        twr.ind_type(f"{r_0} = {r_1} * {int(r_0 / r_1)} + {r_2}")

        return r_0, r_1, r_2

    # @new_indent
    def _gcd_euclid(a: int, b: int, twr: Typewriter) -> int:
        r_0, r_1, r_2 = 0, a, b

        while r_2 != 0:
            r_0, r_1, r_2 = _gcd_euclid_iteration(r_0, r_1, r_2, twr)

        return r_1
    
    # main part 
    return gcd(a=a, b=b, twr=twr)