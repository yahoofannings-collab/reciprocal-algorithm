from decimal import Decimal, getcontext

def calculate_reciprocal(n: int, verbose: bool = True):
    """
    Calculates the exact reciprocal of an integer n using the non-iterative
    method described in the paper "A Non-Iterative Method for Reciprocal
    Computation by Exact Error Cancellation."

    Args:
        n: The integer for which to compute the reciprocal.
        verbose: If True, prints the step-by-step calculation details.

    Returns:
        The exact reciprocal as a high-precision Decimal object.
    """
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")

    # Step 1: Setup
    # Get the number of digits in n and define the block size k.
    d = len(str(n))
    k = 2 * d

    # Set the precision for the decimal calculation. It must be high enough
    # to reliably capture at least two full blocks of k digits.
    getcontext().prec = 2 * k + 4  # Add a buffer for safety

    # Step 2 & 3: Get Digit Blocks and Compute Ratio
    # Calculate the reciprocal to the required precision.
    reciprocal_decimal = Decimal(1) / Decimal(n)

    # Convert the decimal to a string, which truncates at the current precision
    # without the rounding behaviour of the format() function.
    reciprocal_str = str(reciprocal_decimal)[2:]

    # Extract the first block (N1) and second block (N2) as integers.
    n1_str = reciprocal_str[:k]
    n2_str = reciprocal_str[k:2*k]
    
    # Handle potential leading zeros in the blocks by converting to int.
    n1 = int(n1_str)
    n2 = int(n2_str)

    if n1 == 0:
        raise ZeroDivisionError(
            "First digit block (N1) is zero. The algorithm requires a non-zero N1, "
            "which may require a larger block size k for some n."
        )

    # Compute the integer ratio R.
    R = n2 // n1

    # Define the initial approximation 'a' and the correction factor 'r'.
    # We use the Decimal type to maintain precision throughout.
    power_of_10 = Decimal(10) ** k
    a = Decimal(n1) / power_of_10
    r = Decimal(R) / power_of_10

    # Step 4: Final Calculation
    # Apply the geometric series formula to get the exact result.
    s = a / (Decimal(1) - r)

    if verbose:
        print(f"--- Calculation for n = {n} ---")
        print(f"Number of digits (d) = {d}, Block size (k) = {k}")
        print(f"1/{n} = {reciprocal_decimal}")
        print(f"First block (N1)  = {n1_str} -> {n1}")
        print(f"Second block (N2) = {n2_str} -> {n2}")
        print(f"Integer Ratio (R) = {n2} // {n1} = {R}")
        print(f"Initial Approx (a) = {a}")
        print(f"Correction Term (r) = {r}")
        print(f"Final Result (s) = {s.normalize()}")
        numerator, denominator = s.as_integer_ratio()
        print(f"As fraction: {numerator} / {denominator}")
        print("-" * (25 + len(str(n))))

    return s

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    print("--- Reciprocal Calculator ---")
    print("Enter an integer (e.g., 41) to see the calculation.")
    print("Type 'q', 'quit', or 'exit' to end the program.")
    
    while True:
        user_input = input("\nPlease enter an integer > ").strip()

        if user_input.lower() in ['q', 'quit', 'exit']:
            print("Exiting program.")
            break

        try:
            # Convert the user's input to an integer.
            number = int(user_input)
            
            # Call the main algorithm function. The function already has
            # a check for n > 1, so we don't need to repeat it here.
            calculate_reciprocal(number)

        except ValueError:
            # This handles cases where the input is not a valid integer.
            print(f"Error: '{user_input}' is not a valid integer. Please try again.")
        except Exception as e:
            # This catches other errors from the function, like n <= 1.
            print(f"An error occurred: {e}")

