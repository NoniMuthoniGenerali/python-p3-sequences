#!/usr/bin/env python3

def print_fibonacci(length):
    n1, n2 = 0, 1
    n3 = 0
    print ("Fibonacci series:{}, {}".format(n1,n2), end=" ")
    for i in range(length):
        n3 = n1 +n2
        print("{},".format(n3), end=" ")

        n1= n2
        n2= n3
print_fibonacci()
