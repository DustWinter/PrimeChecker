# PrimeCheck1

Complexity = √n

A simple Python function that checks if an odd number is prime using a custom formula.

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
- 
# PrimeCheck2

Complexity = √n

A simple Python function that checks if an odd number is prime using a custom formula.

## How to Use

```python
from PrimeCheck import PrimeCheck

number = 17
is_prime = PrimeCheck2(number)  # Returns True
```

## Updates
The floating-point inaccuracies in PrimeCheck1 are now avoided. Same logic reasoning as PrimeCheck1
