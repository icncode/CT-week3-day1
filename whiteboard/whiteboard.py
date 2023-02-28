# Given a list of integers, write a function determining whether the sum of its elements is odd or even.

# Return your answer as a string matching "odd" or "even".

# If the input array is empty, consider it as [0](array with a zero).

def solution(list_nums):
    return 'even' if sum(list_nums) % 2 == 0 else 'odd'
    

print(solution([]))

