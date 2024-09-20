Write python program that user to enter only odd numbers, else will raise an exception?

def get_odd_number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 == 0:
                raise ValueError("Error: Even number is not allowed")
            return num
        except ValueError as e:
            print(e)

get_odd_number()