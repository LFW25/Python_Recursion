def fib(n):
    """ computes and returns the n-th Fibonacci number
    in O(log n) time"""
    # Set up an initial fibonacci matrix like
    # [[Fn+1, Fn],
    #  [Fn, Fn-1]]
    # where Fn is initially 1
    fib_matrix = [[1, 1], 
                  [1, 0]]

    # If you have run out of numbers, stop!
    if n == 0:
        return 0
    
    # Call the power function
    power(fib_matrix, n - 1)
         
    return fib_matrix[0][0]
     
def multiply(fib_matrix, identity_matrix):
     
    f00 = fib_matrix[0][0] * identity_matrix[0][0] + fib_matrix[0][1] * identity_matrix[1][0] # fn+1 = fn+1 * 1 + fn * 1
    f01 = fib_matrix[0][0] * identity_matrix[0][1] + fib_matrix[0][1] * identity_matrix[1][1] # fn = fn+1 * 1 + fn * 0
    f10 = fib_matrix[1][0] * identity_matrix[0][0] + fib_matrix[1][1] * identity_matrix[1][0] # fn = fn * 1 + fn-1 * 1
    f11 = fib_matrix[1][0] * identity_matrix[0][1] + fib_matrix[1][1] * identity_matrix[1][1] # fn-1 = fn * 1 + fn-1 * 0

    fib_matrix[0][0] = f00
    fib_matrix[0][1] = f01
    fib_matrix[1][0] = f10
    fib_matrix[1][1] = f11

def power(fib_matrix, n):
 
    if n == 0 or n == 1:
        return
    identity_matrix = [[1, 1],
                       [1, 0]]
         
    power(fib_matrix, n // 2)
    multiply(fib_matrix, fib_matrix)
         
    if n % 2 != 0:
        multiply(fib_matrix, identity_matrix)