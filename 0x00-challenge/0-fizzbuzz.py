#!/usr/bin/python3
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        fizzbuzz(int(sys.argv[1]))
    else:
        print("Usage: ./0-fizzbuzz.py <number>")
