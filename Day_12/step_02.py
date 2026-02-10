def is_prime(num):
    # Special rule: 1 is not prime
    if num == 1:
        return False
    
    # Let's test all numbers from 2 until we reach num
    for i in range(2, num):
        if num % i == 0:
            # If the remainder is 0, we found a divisor, so it is NOT prime
            return False
            
    # If the loop ends and finds no divisor, it is prime
    return True

# To test and see the result in the console (Global Scope):
print(is_prime(73)) # Should return True
print(is_prime(75)) # Should return False