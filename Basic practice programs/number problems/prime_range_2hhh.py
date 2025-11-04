def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    
    return [i for i, is_prime in enumerate(primes) if is_prime]

def prime_in_range(start, end):
    all_primes = sieve_of_eratosthenes(end)
    result = [p for p in all_primes if p >= start]
    print(f"Prime numbers between {start} and {end}: {result}")

prime_in_range(10, 50)