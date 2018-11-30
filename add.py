import sys
import math

def add_numbers(num1, num2):
    num3 = int(num1) + 0 + int(num2) 
    print(num3)
    return num3

def main():
    add_numbers(sys.argv[1], sys.argv[2])
	
if __name__ == "__main__":
    main()

