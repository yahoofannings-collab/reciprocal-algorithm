from decimal import Decimal, getcontext

def get_period(numerator, denominator):
    """
    Calculates the length of the repeating part (period) of a fraction's
    decimal expansion.

    Args:
        numerator: The numerator of the fraction.
        denominator: The denominator of the fraction.

    Returns:
        The length of the repeating part of the decimal, or 0 if it terminates.
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")

    n = denominator
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5

    if n == 1:
        return 0

    remainder = 10 % n
    period = 1
    while remainder != 1:
        remainder = (remainder * 10) % n
        period += 1
        if period > denominator:
             return -1 # Should not happen

    return period

def calculate_reciprocal(n: int):
    """
    Calculates the reciprocal and prints all variables used in the algorithm
    and its proof of validity.
    """
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")

    # --- Setup and Direct Calculation (from the Algorithm) ---
    d = len(str(n))
    k = 2 * d
    
    # This single integer division gives both N1 (quotient) and R1 (remainder)
    N1, R1 = divmod(10**k, n)
    R = R1 # R from the algorithm is the same as R1 from the proof

    # Calculate the numerator and denominator of the confirmation fraction (1-r)/a
    confirmation_num = 10**k - R
    confirmation_den = N1

    # Use Decimal for high-precision final calculation
    getcontext().prec = k * 6  # Increased precision for safety
    power_of_10 = Decimal(10)**k
    a = Decimal(N1) / power_of_10
    r = Decimal(R) / power_of_10

    # --- Final Calculation 's' and Confirmation '1/s' ---
    s = a / (Decimal(1) - r)
    confirmation_val = (Decimal(1) - r) / a

    # --- Calculate N2 and R2 (for the proof of validity) ---
    # From the proof: 10^k * R1 = n * N2 + R2
    N2, R2 = divmod(10**k * R1, n)

    # --- Main Output ---
    print(f"\n--- Calculation for n = {n} ---")
    one_over_n = Decimal(1) / Decimal(n)
    print(f"1/n (for reference)  = {one_over_n}")
    print(f"Algorithm Variables:")
    print(f"  d = {d}")
    print(f"  k = {k}")
    print(f"  Quotient (N1)      = {N1}")
    print(f"  Remainder (R)      = {R}")
    print(f"  a = N1/10^k        = {a}")
    print(f"  r = R/10^k         = {r}")
    print(f"  s = a/(1-r)        = {s.normalize()}")
    print(f"  1/s (as number)    = {confirmation_val.normalize()}")
    print(f"  1/s (as fraction)  = (1-r)/a = ({confirmation_num})/({confirmation_den})")
    
    # --- Output for Proof of Validity ---
    print(f"\nProof of Validity Variables:")
    print(f"  n = {n}")
    print(f"  10^k = {10**k}")
    print(f"  From '10^k = n*N1 + R1':")
    print(f"    N1 = {N1}")
    print(f"    R1 = {R1}")
    print(f"  From '10^k*R1 = n*N2 + R2':")
    print(f"    N2 = {N2}")
    print(f"    R2 = {R2}")
    
    # Calculate R from the blocks to show it's identical to R1
    R_from_blocks = N2 // N1
    print(f"  R (as floor(N2/N1)) = {R_from_blocks}")

    # --- Period Length Calculation and Display ---
    period_length = get_period(1, n)
    if period_length > 100:
        period_display = "> 100"
    else:
        period_display = str(period_length)
    print(f"\nPeriod of decimal = {period_display}")
    print("-" * (25 + len(str(n))))


# --- Main execution block with interactive prompt ---
if __name__ == "__main__":

    print("Non-Iterative Reciprocal Computation by Exact Error Cancellation")
    print("Calculates the exact reciprocal of an integer n > 1.")
    print(" ")
    print("Demonstrating that the geometric series summation formula, s = a/(1 − r),")
    print("with the terms a and r derived for the integer, will collapse into the algebraic identity 1/n")
    print("after determining a, the first term of the series (the initial approximation), and")
    print("r, which serves as the common ratio in the geometric series formula and  functions")
    print("as a correction factor that precisely accounts for the residual error in the initial approximation, a.")
    print(" ")
    print("While s = a/(1-r) = 1/n is valid, the decimal module will calculate this division and")
    print("round the result to x significant digits. For periodic decimals, this number will be")
    print("extremely close, but it is not the exact repeating decimal.")
    print("To correct for this, the output displys both s and 1/s = (1-r)/a")
    print(" ")

    print("Type 'q', 'quit', or 'exit' to end the program.")
    
    while True:
        user_input = input("\nPlease enter an integer n > ").strip().lower()

        if user_input in ['q', 'quit', 'exit']:
            print("Exiting program.")
            break
        
        try:
            n_val = int(user_input)
            if n_val <= 1:
                print("Error: Please enter an integer greater than 1.")
                continue
            calculate_reciprocal(n_val)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


