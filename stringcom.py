import sys

def compare_strings(str1, str2):
    if str1.lower() == str2.lower():
        print("It's a match")
    else:
        print("Does not match")

def main():
    compare_strings(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

