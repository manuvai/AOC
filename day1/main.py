"""
"""

import re

def get_numbers(line: str):
    correspondings = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    
    regex_pattern = r"(\d|one|two|three|four|five|six|seven|eight|nine)"
    numbers = []
    i = 0
    is_end = len(line) - 1 == i

    cursor = i
    while not is_end:
        
        string_studied = line[i:len(line)]
        search_result = re.search(regex_pattern, string_studied)

        if (search_result is None):

            is_end = True
        else:
            numbers.append(search_result.group())
            i = cursor + search_result.start() + 1
            cursor = i
        
    print()
    print("Ligne : {}".format(line))
    print(numbers)


    for i in range(len(numbers)):
        if (numbers[i] in correspondings.keys()):
            numbers[i] = correspondings[numbers[i]]

    return numbers

def get_number_from_list(numbers: list):
    response = ""

    if (len(numbers) > 0):
        response += numbers[0] + numbers[-1]

    return int(response) if len(response) > 0 else 0

def get_lines(file_path: str):

    lines = []
    with open(file_path) as file:
        # Traitement du fichier
        for line in file.readlines():
            lines.append(line)

    return lines

file = "day1/input.txt"

count = 0
lines = get_lines(file)
for line in lines:
    numbers = get_numbers(line)
    print(numbers)
    to_count = get_number_from_list(numbers)
    count += to_count

print("Total {}".format(count))
