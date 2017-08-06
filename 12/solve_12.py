"""Solution to the 12th problem on Project Euler."""

# find triangle numbers.
def triangle_numbers(limit):
    """Generates triangle numbers."""
    triangle_number = 1
    for number in range(2, limit):
        yield triangle_number
        triangle_number += number

# find all primes under limit.
def prime_sieve(limit):
    """Generate primes using the sieve of Eratosthenes."""
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

# find number of divisors.
def divisors(number, primes):
    """Finds number of divisors of a number using prime factorization."""
    prime_factors_pow = []
    if number < 2:
        prime_factors_pow.append(0)
    for p in primes:
        if p > number:
            break
        n = 0
        while number % p == 0:
            n += 1
            number //= p
        prime_factors_pow.append(n)
    num_divisors = 1
    for k in prime_factors_pow:
        num_divisors *= k + 1
    return num_divisors

def main():
    """prints the first triangle number with more than 500 divisors."""
    primes = list(prime_sieve(10**5))
    for number in triangle_numbers(10**5):
        if divisors(number, primes) > 500:
            print("{} is the number".format(number))
            break

if __name__ == '__main__':
    main()
