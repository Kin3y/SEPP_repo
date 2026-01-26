# SEPP_repo
A repository for the SEPP module

## Python Calculator

A simple command-line calculator application that supports basic arithmetic operations.

### Features

- Addition
- Subtraction
- Multiplication
- Division
- Power (exponentiation)
- Modulo (remainder)
- Error handling for division/modulo by zero
- Interactive command-line interface

### Installation

No external dependencies required. Only Python 3.x is needed.

### Usage

To run the calculator:

```bash
python main.py
```

Or make it executable and run directly:

```bash
chmod +x main.py
./main.py
```

### Running Tests

To run the unit tests:

```bash
python test_calculator.py
```

Or use unittest discovery:

```bash
python -m unittest test_calculator.py
```

### Example

```
Welcome to the Simple Calculator!

==================================================
SIMPLE CALCULATOR
==================================================
Available operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (^)
6. Modulo (%)
0. Exit
==================================================

Select an operation (0-6): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0
```

### Module Usage

You can also import the calculator module in your Python code:

```python
import calculator

result = calculator.add(5, 3)
print(result)  # Output: 8

result = calculator.divide(10, 2)
print(result)  # Output: 5.0
```
