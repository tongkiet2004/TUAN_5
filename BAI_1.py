from collections import deque
def max_kernel(num_list, k):
    if not num_list or k == 0:
        return []
    
    result = []
    dq = deque()
    
    for i in range(len(num_list)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        while dq and num_list[dq[-1]] < num_list[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(num_list[dq[0]])
    
    return result

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))  
