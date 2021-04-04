#Given a number N return the index value of Fibonacci sequence
#where the sequence is:
#0, 1, 1, 2, 3, 5, 8, 24, 32, 34, 55...
#the pattern of sequence is that each value
#is the sum of the 2 previous values
#that means for N=5 -> 2+3

def fibonacci_recursive(n):
    if (n < 2):
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

if __name__ == "__main__":

    print(fibonacci_recursive(8))

