from itertools import permutations

def check_prime(num):
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    prime_list = []
    n = list(numbers)
    lst = []
    
    for i in range(1, len(n)+1):
        lst += list(permutations(n, i))
    
    for i in lst:
        num = int(''.join(i))
        if num < 2:
            continue

        elif check_prime(num) and num not in prime_list:
            answer += 1
            prime_list.append(num)
    
    
    return answer
    

    
    
