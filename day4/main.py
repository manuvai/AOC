
def get_lines(file_path: str):

    lines = []
    with open(file_path) as file:
        # Traitement du fichier
        for line in file.readlines():
            lines.append(line)

    return lines

class Hand:
    def __init__(self, numbers: list[str]) -> None:
        new_numbers = []
        for el in numbers:
            el = el.strip()
            if (len(el) > 0):
                el = int(el)
                new_numbers.append(el)

        self.numbers = new_numbers

    def corresponding(self, other) -> int:
        count = 0
        for el in other.numbers:
            if (el in self.numbers):
                count+=1
        return count
    
def get_hands_numbers(line: str) -> tuple[Hand]:
    temp = line.split(":")[1]

    left = temp.split("|")[0].strip()
    right = temp.split("|")[1].strip()

    left_hand = Hand(left.split(" "))
    right_hand = Hand(right.split(" "))

    return left_hand, right_hand

def main():
    lines = get_lines("day4/test.txt")

    count = compute2(lines)

    print(count)

def compute2(lines: list[str]) -> int:
    copy_lines = []
    for i in range(len(lines)):
        left_hand, right_hand = get_hands_numbers(lines[i])
        
        corresponding = left_hand.corresponding(right_hand)

        j = 0
        while j < len(lines) and j < corresponding:
            copy_lines.append(lines[i + j])
            j+=1

    return compute1(copy_lines)



def compute1(lines: list[str]) -> int:
    count = 0
    for line in lines:
        left_hand, right_hand = get_hands_numbers(line)
        
        corresponding = left_hand.corresponding(right_hand)
        if (corresponding > 0):
            count += 2 ** (corresponding - 1)
    return count

main()