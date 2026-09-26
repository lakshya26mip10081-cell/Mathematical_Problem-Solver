from src.find_base_converter import base_a_to_base_b
from src.find_GCD import calculate_gcd
from src.find_prime_factorization import prime_factorization
from src.find_smallest_divisor import smallest_divisor
from src.find_square_root import calculate_square_root
from src.find_random_number import generate_random_number

print("Welcome To Mathematical Problem Solver")
def show_menu():
    print("\n" + "=" * 40)
    print("MATHEMATICAL PROBLEM SOLVER")
    print("=" * 40)
    print("1. Find Base Conversion")
    print("2. Find GCD")
    print("3. Find Prime Factorization")
    print("4. Find Smallest Divisor")
    print("5. Find Square Root")
    print("6. Find Random Number Generator")
    print("=" * 40)


def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                number = input("Enter number: ").strip()
                base_a = int(input("Enter source base: "))
                base_b = int(input("Enter target base: "))

                result = base_a_to_base_b(number, base_a, base_b)

                print("Converted number:", result)
                print("Thank you for using Mathematical Problem Solver.")

            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))

                result = calculate_gcd(a, b)

                print("GCD:", result)
                print("Thank you for using Mathematical Problem Solver.")
                

            except ValueError:
                print("Please enter valid integers.")

        elif choice == "3":
            try:
                number = int(input("Enter a number: "))

                if number < 2:
                    print("Please enter an integer greater than or equal to 2.")
                else:
                    result = prime_factorization(number)

                    print(
                        "Prime Factorization:",
                        " × ".join(map(str, result))
                    )
                    print("Thank you for using Mathematical Problem Solver.")
                    

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "4":
            try:
                number = int(input("Enter a number: "))

                result = smallest_divisor(number)

                if result is None:
                    print("Please enter a number greater than 1.")
                else:
                    print("Smallest Divisor:", result)
                    print("Thank you for using Mathematical Problem Solver.")
                    

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "5":
            try:
                number = float(input("Enter a number: "))

                result = calculate_square_root(number)

                if result is None:
                    print("Square root of a negative number is not supported.")
                else:
                    print("Square Root:", result)

            except ValueError:
                print("Please enter a valid number.")
                print("Thank you for using Mathematical Problem Solver.")
                

        elif choice == "6":
            try:
                start = int(input("Enter starting number: "))
                end = int(input("Enter ending number: "))

                result = generate_random_number(start, end)

                if result is None:
                    print(
                        "Invalid range. Starting number must be "
                        "less than or equal to ending number."
                    )
                else:
                    print("Random Number:", result)
                    print("Thank you for using Mathematical Problem Solver.")
                    

            except ValueError:
                print("Please enter valid integers.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
