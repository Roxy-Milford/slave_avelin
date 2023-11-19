# from functools import wraps

from ..typewriters.typewriters import AbstractTypewriter, Typewriter, new_indent


################################################################################
### Default values
################################################################################

DEFAULT_TYPER = Typewriter


################################################################################
### Algorithms
################################################################################


def gcd(a: int, b: int, twr: AbstractTypewriter=None) -> int:
    if twr is None:
        twr = DEFAULT_TYPER()
    def gcd(a: int, b: int, twr: AbstractTypewriter) -> int:
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

        twr.type(f"Calculate: gcd({a}, {b})", print_indent=True)

        rez = None
        with new_indent(twr) as twr:
            rez = _gcd_euclid(a, b, twr)

        twr.type(f"gcd({a}, {b}) = {rez}", print_indent=True)

        return rez

    def _gcd_euclid_iteration(r_0: int, r_1: int, r_2: int, twr: AbstractTypewriter) -> tuple:
        r_0 = r_1
        r_1 = r_2
        r_2 = r_0 % r_1

        twr.type(f"{r_0} = {r_1} * {int(r_0 / r_1)} + {r_2}", print_indent=True)

        return r_0, r_1, r_2

    def _gcd_euclid(a: int, b: int, twr: AbstractTypewriter) -> int:
        r_0, r_1, r_2 = 0, a, b

        while r_2 != 0:
            r_0, r_1, r_2 = _gcd_euclid_iteration(r_0, r_1, r_2, twr)

        return r_1
    
    # main part 
    return gcd(a=a, b=b, twr=twr)


def modular_inverse(a: int, mod: int, twr: AbstractTypewriter=None) -> int:
    if twr is None:
        twr = DEFAULT_TYPER()


    def modular_inverse_alg(a: int, mod: int, twr: AbstractTypewriter) -> int:
        """TODO: write comment
        """
        # TODO: write assertions
        temp_a = a
        while temp_a < 0:
            temp_a += mod
        
        while temp_a >= mod:
            temp_a -= mod

        if a != temp_a:
            twr.type(f"Calculate: {a}^-1 (mod{mod}) = {temp_a}^-1 (mod{mod}) ", print_indent=True)
            a = temp_a
        else:
            twr.type(f"Calculate: {a}^-1 (mod{mod})", print_indent=True)

        mi = None
        with new_indent(twr) as twr:
            mi = _modular_inverse_direct(a=a, mod=mod, twr=twr)

        return mi
    
    def _gcd_euclid_iteration(r_0: int, r_1: int, r_2: int, twr: AbstractTypewriter) -> tuple:
        r_0 = r_1
        r_1 = r_2
        r_2 = r_0 % r_1

        twr.type(f"{r_0} = {r_1} * {int(r_0 / r_1)} + {r_2}", print_indent=True)

        return r_0, r_1, r_2

    # @new_indent
    def _gcd_euclid_extended(a: int, b: int, twr: AbstractTypewriter) -> int:
        r_0, r_1, r_2 = 0, a, b
        q = []
        r=[r_1]

        while r_2 != 0:
            # next line should be at the start, because the last value: 0 is redundant
            r.append(r_2)
            q.append(int(r_1 / r_2))
            r_0, r_1, r_2 = _gcd_euclid_iteration(r_0, r_1, r_2, twr=twr)

        return r_1, q, r

    # @new_indent
    def _modular_inverse_backward_step(d: int, q: list, r: list, twr: AbstractTypewriter) -> int:
        # change lists to increase redability
        q.reverse()
        q.remove(q[0])
        r.reverse()
        r.remove(r[0])

        # find inverse and save steps for printing
        # TODO: increase readability
        equalities_chain = ""
        twr.type("1", last_in_line=False)

        # setup
        coef_cur = 1
        coef_prev = 0
        r_cur = r[0]
        r_prev = r[1]
        # algorithm
        for i in range(len(q)):
            r_cur = r[i]
            r_prev = r[i+1]
            coef_cur, coef_prev = coef_prev - coef_cur * q[i], coef_cur 
            equalities_chain += f" = {coef_cur}*{r_cur} + {coef_prev}*{r_prev}"

        twr.type(equalities_chain)

        return coef_cur

    # @new_indent
    def _modular_inverse_direct(a: int, mod: int, twr: AbstractTypewriter) -> int:
        r_0, r_1, r_2 = 0, mod, a

        # gcd calculation
        twr.type(f"Calculate: gcd({mod}, {a})", print_indent=True)


        d, q, r = None, None, None
        with new_indent(twr)as twr:
            d, q, r = _gcd_euclid_extended(a=mod, b=a, twr=twr)

        # gcd must be equal to 1        
        if d != 1:
            twr.type(f"Number {a} has no inverse with module {mod}", print_indent=True)
            return

        # d is always equal to 1, I left it for my wish
        twr.type(f"gcd({a}, {mod}) = {d}", print_indent=True)

        # calculation of inverse element
        twr.type(f"Next step", print_indent=True)
        d = _modular_inverse_backward_step(d=d, q=q, r=r, twr=twr)

        return d
    
    return modular_inverse_alg(a=a, mod=mod, twr=twr)