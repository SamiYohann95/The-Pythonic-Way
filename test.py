def is_prime(n): 
    if n <= 1: 
        return False 
    if n == 2: 
        return True 
    if n % 2 == 0: 
        return False 
    max_divisor = int(n ** 0.5) + 1 
    for i in range(3, max_divisor, 2): 
        if n % i == 0: 
            return False 
    return True 
 
def find_prime_numbers_in_list(lst): 
    prime_numbers = [] 
    for num in lst: 
        if is_prime(num): 
            prime_numbers.append(num)
    return prime_numbers 
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
prime_numbers = find_prime_numbers_in_list(numbers) 
print("Prime numbers in the list:", prime_numbers) 