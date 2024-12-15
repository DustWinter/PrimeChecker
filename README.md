# PrimeChecker

A simple Python function that checks if a number is prime using a custom formula.

## How to Use

```python
from PrimeCheck import PrimeCheck

number = 17
is_prime = PrimeCheck(number)  # Returns True
```

## How it Works

Uses the formula: `(((n-1)/2)-a) / ((2*a)+1)`
- If the formula ever results in a whole number, the input is not prime
- Otherwise, the number is prime
