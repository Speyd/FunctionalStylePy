## Tasks

### Task 1: Log Function Calls

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"→ {func.__name__}({', '.join(map(str, args))}" +
              (", " if kwargs else "") +
              ", ".join(f"{k}={v}" for k, v in kwargs.items()) + ")")
        result = func(*args, **kwargs)
        print(f"← {func.__name__} = {result}")
        return result
    return wrapper

@log_calls
def add(a: int, b: int) -> int:
    return a + b
```

Logs every call to a function along with its arguments and result.

### Task 2: Time Function Execution

```python
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start)*1000:.0f} ms")
        return result
    return wrapper

@timeit
def slow(n: int) -> int:
    time.sleep(0.05)
    return n*n
```

Measures the execution time of a function in milliseconds.

### Task 3: Strong Password Check

```python
import string

def is_strong_password(s: str) -> bool:
    return (len(s) >= 8 and
            any(c.isupper() for c in s) and
            any(c.islower() for c in s) and
            any(c.isdigit() for c in s) and
            any(c in string.punctuation for c in s))
```

Checks if a password is strong (uppercase, lowercase, digit, special character, ≥8 chars).

### Task 4: Check All Close Numbers

```python
from typing import Iterable

def all_close(xs: Iterable[float], tol: float = 1e-6) -> bool:
    xs = list(xs)
    return all(abs(x - xs[0]) <= tol for x in xs)
```

Returns `True` if all numbers in the list are within a given tolerance.

### Task 5: Check for Prime Numbers

```python
import math

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def has_prime(nums: Iterable[int]) -> bool:
    return any(is_prime(x) for x in nums)
```

Returns `True` if at least one number in the iterable is prime.

### Task 6: Scale and Shift List

```python
def scale_and_shift(xs: Iterable[float], scale: float, shift: float) -> list[float]:
    return [scale * x + shift for x in xs]
```

Applies the transformation `x*scale + shift` to each element of the list.

### Task 7: Filter Valid Emails

```python
def filter_emails(items: Iterable[str]) -> list[str]:
    return [s for s in items if "@" in s and "." in s.split("@")[-1]]
```

Filters a list of strings, returning only valid-looking email addresses.

### Task 8: Character Frequency Histogram

```python
from functools import reduce

def char_hist(s: str) -> dict[str, int]:
    return reduce(lambda d, c: {**d, c: d.get(c, 0) + 1}, s, {})
```

Builds a dictionary with character counts for a string.

### Task 9: Top-K Students

```python
def top_k(students: list[dict[str, int | str]], k: int) -> list[str]:
    return [s['name'] for s in sorted(students, key=lambda x: (-x['score'], x['name']))[:k]]
```

Returns the names of the top `k` students by score, breaking ties alphabetically.

### Task 10: Min-Max Normalization

```python
def minmax_scale(xs: list[float]) -> list[float]:
    if not xs:
        return []
    mn, mx = min(xs), max(xs)
    if mn == mx:
        return [0.0]*len(xs)
    return [(x - mn)/(mx - mn) for x in xs]
```

Scales numbers in a list to the [0,1] range. If all numbers are equal, returns 0.0 for all.

## Main Function

```python
if __name__ == "__main__":
    print(add(2, 3))
    print(slow(10))
    print(is_strong_password("Qwerty12!"))
    print(all_close([1.0, 1.0000005, 0.9999999], tol=1e-5))
    print(has_prime([4, 6, 7, 9, 10]))
    print(scale_and_shift([1,2,3], 2.0, -1.0))
    print(filter_emails(["a@b.com", "wrong@", "x@y", "john.doe@mail.org"]))
    print(char_hist("aba c"))
    students = [{"name":"Ann","score":90},{"name":"Bob","score":95},{"name":"Ada","score":95}]
    print(top_k(students, 2))
    print(minmax_scale([10, 20, 30]))
```
