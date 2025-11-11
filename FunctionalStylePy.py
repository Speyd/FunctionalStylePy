import time
from typing import Iterable
import string
import math
from functools import reduce

print("=== 1. Декоратор log_calls ===")
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

print(add(2, 3))


print("\n=== 2. Декоратор timeit ===")
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

print(slow(10))


print("\n=== 3. Перевірка сильного пароля ===")
def is_strong_password(s: str) -> bool:
    return (len(s) >= 8 and
            any(c.isupper() for c in s) and
            any(c.islower() for c in s) and
            any(c.isdigit() for c in s) and
            any(c in string.punctuation for c in s))

print(is_strong_password("Qwerty12!"))  
print(is_strong_password("qwerty12")) 


print("\n=== 4. Перевірка all_close ===")
def all_close(xs: Iterable[float], tol: float = 1e-6) -> bool:
    xs = list(xs)
    return all(abs(x - xs[0]) <= tol for x in xs)

print(all_close([1.0, 1.0000005, 0.9999999], tol=1e-5))  
print(all_close([1.0, 1.1], tol=1e-3))                  


print("\n=== 5. Перевірка наявності простого числа ===")
def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def has_prime(nums: Iterable[int]) -> bool:
    return any(is_prime(x) for x in nums)

print(has_prime([4, 6, 8, 9]))    
print(has_prime([4, 6, 7, 9, 10])) 


print("\n=== 6. Масштабування і зсув ===")
def scale_and_shift(xs: Iterable[float], scale: float, shift: float) -> list[float]:
    return list(map(lambda x: scale * x + shift, xs))

print(scale_and_shift([1, 2, 3], 2.0, -1.0))


print("\n=== 7. Фільтрація e-mail ===")
def filter_emails(items: Iterable[str]) -> list[str]:
    return list(filter(lambda s: "@" in s and "." in s.split("@")[-1], items))

emails = ["a@b.com", "wrong@", "x@y", "john.doe@mail.org"]
print(filter_emails(emails))


print("\n=== 8. Частотний словник символів ===")
def char_hist(s: str) -> dict[str, int]:
    return reduce(lambda d, c: {**d, c: d.get(c, 0) + 1}, s, {})

print(char_hist("aba c"))


print("\n=== 9. Топ-K студентів ===")
def top_k(students: list[dict[str, int | str]], k: int) -> list[str]:
    return [s['name'] for s in sorted(students, key=lambda x: (-x['score'], x['name']))[:k]]

students = [{"name":"Ann","score":90},{"name":"Bob","score":95},{"name":"Ada","score":95}]
print(top_k(students, 2)) 


print("\n=== 10. Мін-макс нормалізація ===")
def minmax_scale(xs: list[float]) -> list[float]:
    if not xs:
        return []
    mn, mx = min(xs), max(xs)
    if mn == mx:
        return [0.0]*len(xs)
    return [(x - mn)/(mx - mn) for x in xs]

print(minmax_scale([10, 20, 30]))  
print(minmax_scale([5, 5, 5]))  
