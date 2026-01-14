def is_prime(num):
    if num<2:
        return True
                        # If the number is 1.
    elif num>=2:
        for i in range(2, num):
            if num%i==0:
                return False
                        # Breaks the loop if there is one instance where it divides out to zero
                        # Case of when the number is greater than 1. 
        return True