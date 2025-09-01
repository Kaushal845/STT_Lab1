"""
main.py
Simple program for Lab 1.
Demonstrates functions, loops, and basic calculations.
"""


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b


def greet_user(name):
    """Return a greeting message for the given user."""
    return f"Hello, {name}!"


def main():
    """Main function to run the program."""
    print("Welcome to the Lab 1 Python Program")
    print("-" * 40)

    # Greeting
    print(greet_user("Alice"))
    print(greet_user("Bob"))

    # Arithmetic examples
    print("5 + 3 =", add_numbers(5, 3))
    print("4 * 7 =", multiply_numbers(4, 7))

    # Loop example
    print("Squares of numbers 1 to 5:")
    for i in range(1, 6):
        print(i, "squared is", multiply_numbers(i, i))

    # Small list example
    fruits = ["apple", "banana", "cherry"]
    print("Fruit list:")
    for fruit in fruits:
        print("-", fruit)


if __name__ == "__main__":
    main()
