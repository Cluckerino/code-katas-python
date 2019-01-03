"""
Given a number d, count all -reduced- fractions with denominator d (i.e. for 1/d...d/d, find all
n/d where n and d are coprime).
https://www.codewars.com/kata/number-of-proper-fractions-with-denominator-d/python
"""

import itertools

import numpy


def is_prime(num):
    """Check if a number is prime."""
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i = i + 1
    return True


def get_unique_prime_factors(num):
    """Gather up all of the unique prime factors here."""
    if num == 1:
        return []

    found_primes = []

    def check_multiple(num):
        """Checks if number divides into any previous primes found."""
        return any(
            map(lambda prev: num % prev == 0, found_primes)
        )
    cur_num = 2
    # This is the number left over after dividing by the prime factor each step.
    # i.e. number was 72, this would be divided repeatedly by 2 to become 9.
    leftover = num
    while cur_num * cur_num <= num and cur_num < leftover:
        # If cur_num is a new prime (i.e. not multiple of previous prime) and denom is divisible
        # by cur_num
        if not check_multiple(cur_num) and leftover % cur_num == 0:
            found_primes.append(cur_num)
            # Decompose the leftover by our found prime.
            while leftover % cur_num == 0:
                leftover = leftover // cur_num
            print("Found {}, leftover {}".format(cur_num, leftover))
            # Check if our leftover is itself a prime
            other_prime_maybe = leftover
            if other_prime_maybe != cur_num and is_prime(other_prime_maybe):
                found_primes.append(other_prime_maybe)
                # Decompose the leftover by our other found prime.
                while leftover % other_prime_maybe == 0:
                    leftover = leftover // other_prime_maybe
                print("Found other {}, leftover {}".format(
                    other_prime_maybe, leftover))
        cur_num = cur_num + 1
    return found_primes


def proper_fractions_brute_force(denom):
    """Count the number of reduced fractions with denominator denom."""
    print("Checking {}".format(denom))
    tally = denom - 1
    primes = get_unique_prime_factors(denom)
    print("Found primes: {}".format(primes))

    # tally algorithm:
    # If prime factors are 3, 5, 7 (e.g. 1575):
    #   remove multiples of 3, 5, and 7 from tally
    #   add multiples of 3*5=15, 3*7=21, and 5*7=35 from tally
    #   remove mutiples of 3*5*7=105 from tally
    # items is how many factors to take
    # sign is whether to add/remove
    # factor is current product of primes whose multiples should be removed.
    sign = -1
    for items in range(1, len(primes)+1):
        for prime_comb in itertools.combinations(primes, items):
            factor = numpy.prod(prime_comb)
            tally = tally + sign * ((denom//factor) - 1)
        sign = sign * -1

    return tally


def proper_fractions_totient(num):
    """Calculate using the Euler totient function."""
    # Totient function description:
    # https://en.wikipedia.org/wiki/Euler%27s_totient_function
    # Method proof:
    # Totient function is defined as follows:
    # phi(n) = n * Pi(1 - 1/p) for prime numbers where p | n
    # Start with
    #  phi_0 = n
    # Let p_k be the kth prime number with p_k | n
    # Define phi_k = phi_k-1 - phi_k-1 / p_k
    #  phi_k = phi_k-1 * (1 - 1 / p_k)
    #  phi_1 = phi_0 * (1 - 1 / p_1) = n * (1 - 1 / p_1)
    #  phi_2 = phi_1 * (1 - 1 / p_2) = n * (1 - 1 / p_1) * (1 - 1 / p_2)
    # Etc.
    # To iterate through unique prime factors:
    # Start with leftover = n
    # Iterate through p = 2..sqrt(n)
    #   if p | leftover:
    #     p is prime
    #     Repeat leftover = leftover / p until not p | leftover
    #     leftover should now be just factors of the remaining primes.
    # Since p only iterates through primes < sqrt(n):
    #   if leftover > 1
    #     leftover is a also a prime (> sqrt(n))
    if num == 1:
        return 0
    phi = num
    leftover = num
    p = 2
    while p * p <= num:
        if not leftover % p:
            phi -= phi // p
            while not leftover % p:
                leftover //= p
        p += 1
    # This step is to capture the last prime if it's > sqrt(n).
    if leftover > 1:
        phi -= phi // leftover
    return phi


# Use the totient methood cuz it's cool
proper_fractions = proper_fractions_totient
