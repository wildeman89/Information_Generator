import random

def main():
    valid = False
    numbers = []
    amount = -1
    while not valid:
        try:
            amount = int(input("How many phone numbers would you like to generate? "))
            if amount > 0:
                valid = True
            else:
                print("Has to be a positive number")
        except ValueError:
            print("Enter a number.")

    # going to run the loop for the amount of phone numbers requested
    for x in range(amount):
        number = get_area_code() + get_first_half() + get_last_half()
        numbers.append(number)
    
    # Printing all the numbers -- eventually add csv file creation
    for n in range(amount):
        print(f"{n+1}: {numbers[n]}")

    write_to_file = False
    options = {
        "yes" : True,
        "y"   : True
        }
    usr_choice = input("Write to csv? (y/n) ")
    if usr_choice.lower() in options.keys():
        write_to_file = options[usr_choice.lower()]
    if write_to_file:
        write_csv(numbers)

# Functions
def get_area_code():
    area_code = "("
    for i in range(3):
        temp = get_random_number()
        area_code += str(temp)
    return area_code + ")"

def get_first_half():
    number = "-"
    for i in range(3):
        temp = get_random_number()
        number += str(temp)
    return number + "-"

def get_last_half():
    number = ""
    for i in range(4):
        temp = get_random_number()
        number += str(temp)
    return number

def get_random_number():
    return random.randint(0, 9)

def write_csv(alist):
    import csv
    filename = "numbers.csv"
    with open(filename, "w") as file:
        field_name = ["phone number"]
        writer = csv.DictWriter(file, fieldnames=field_name)
        writer.writeheader()
        # loop through all numbers and write them to csv file
        for item in alist:
            writer.writerow({field_name[0] : item})


main()
