#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given integer.

    Function Description:
    ---------------------
    Computes the factorial of a non-negative integer by recursively multiplying it with all positive integers less than itself.

    Parameters:
    -----------
    n : int
        The integer for which the factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input integer n.

    Raises:
    -------
    ValueError
        If n is negative, as factorials for negative numbers are not defined.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    # Ensure the user provides exactly one command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 factorial.py <non-negative-integer>")
        sys.exit(1)

    try:
        # Convert input to an integer
        num = int(sys.argv[1])

        # Calculate the factorial
        result = factorial(num)

        # Print the factorial result
        print(f"The factorial of {num} is {result}")
    except ValueError as e:
        # Handle invalid input, including non-integers or negative numbers
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
