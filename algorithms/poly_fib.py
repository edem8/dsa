#Fibonnaci is an exponential algorithm- exponential algos are slower than class p algos
# Expo Fib - find the fib at a certain position
def expo_fib(n):
    if n == 0:return 0
    if n == 1: return 1

    return expo_fib(n-1) + expo_fib(n-2)




# converting the exxpo fib into poly fib - faster and more efficient
def poly_fib(n):
    if n == 0: return 0
    if n == 1: return 1


    current = 0
    next  = 1
    previous = 0

    for _ in range(0, n-1):
        current = next + previous
        previous = next
        next = current
    return current

