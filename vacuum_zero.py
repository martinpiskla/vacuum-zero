from itertools import islice

def calculator(list_of_numbers, position, list_of_answers):
    k = position
    total = 0
    for i, number in enumerate(list_of_numbers[position:], k):
                    total += number
                    if total == 0:
                        list_of_answers.append("yes")
                        return True
                    if i == len(list_of_numbers) - 1:
                            if k != len(list_of_numbers) - 2:
                                k += 1
                                calculator(list_of_numbers, k, list_of_answers)
                            else:
                                list_of_answers.append("no")


def write_to_file(filepath, list_content):
    with open(filepath, "w", encoding="utf-8-sig") as file:
        for i in list_content:
            file.write(i)
            file.write("\n")

def calculate_zero(file_path):
    total = 0
    answers = []
    with open(file_path, "r", encoding="utf-8-sig") as file:
            next(file)
            for line in islice(file, 1, None, 2):
                numbers = [int(n) for n in line.split()]
                total = 0
                if sum(numbers) == 0:
                    answers.append("yes")
                    break
                for i, number in enumerate(numbers, 1):
                    if number == 0:
                        answers.append("yes")
                        break
                    total += number
                    if total == 0:
                        answers.append("yes")
                        break
                    if i == len(numbers):
                        calculator(numbers, 1, answers)
    try:                    
        write_to_file(r"C:\Users\Martin\Downloads\vacuum_labs\my_output.out", answers)
    except Exception:
        print("something went wrong with the file")

calculate_zero(r"C:\Users\Martin\Downloads\vacuum_labs\test.in")