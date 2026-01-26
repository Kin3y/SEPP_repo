#!/usr/bin/env python3
"""
Calculator - A simple command-line calculator application.

Usage:
    python main.py
"""

import calculator


def display_menu():
    """Display the calculator menu."""
    print("\n" + "="*50)
    print("SIMPLE CALCULATOR")
    print("="*50)
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulo (%)")
    print("0. Exit")
    print("="*50)


def get_numbers():
    """Get two numbers from the user."""
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input! Please enter valid numbers.")


def main():
    """Main function to run the calculator."""
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        
        choice = input("\nSelect an operation (0-6): ")
        
        if choice == '0':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice! Please select a valid operation.")
            continue
        
        a, b = get_numbers()
        
        try:
            if choice == '1':
                result = calculator.add(a, b)
                print(f"\nResult: {a} + {b} = {result}")
            elif choice == '2':
                result = calculator.subtract(a, b)
                print(f"\nResult: {a} - {b} = {result}")
            elif choice == '3':
                result = calculator.multiply(a, b)
                print(f"\nResult: {a} * {b} = {result}")
            elif choice == '4':
                result = calculator.divide(a, b)
                print(f"\nResult: {a} / {b} = {result}")
            elif choice == '5':
                result = calculator.power(a, b)
                print(f"\nResult: {a} ^ {b} = {result}")
            elif choice == '6':
                result = calculator.modulo(a, b)
                print(f"\nResult: {a} % {b} = {result}")
        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
