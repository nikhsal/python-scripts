while True:
    try:
        n = 5/0
    except ZeroDivisionError:
        print("Division by Zero")
        break
