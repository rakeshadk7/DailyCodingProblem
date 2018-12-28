'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


# Brute Force
def two_sum(numbers, k):
    
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if i != j and numbers[i] + numbers[j] == k:
                return True
    return False
    
    
# O(N) solution 

def two_sum(numbers, k):
    
    already_seen = set()
    
    for num in numbers:
        if k - num in already_seen:
            return True
        already_seen.add(num)
        
    return False