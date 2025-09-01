"""
This file is written for Lab 1.
It demonstrates basic Python functions (fibonacci, squares, subtract)
with corrected style for pylint.
"""


def subtract(a: int, b: int) -> int:
    """Return the result of subtracting b from a."""
    return a - b


def welcome(user: str) -> None:
    """Print a welcome message for the given user."""
    print("Welcome " + user)


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def squares(limit: int) -> None:
    """Print squares of numbers from 0 up to (limit - 1)."""
    for i in range(limit):
        print(i, "squared is", i * i)


def main() -> None:
    """Main function to run the program."""
    print("Fibonacci numbers:")
    for j in range(6):
        print(fibonacci(j))

    welcome("Kaushal")

    print("Subtract 10 - 4 =", subtract(10, 4))

    print("Squares up to 5:")
    squares(5)


if __name__ == "__main__":
    main()
