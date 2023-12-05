"""

"""

class Game:
    def __init__(self, id):
        self.id = id
        self.sets = []
    
    def is_possible(self, in_set):
        for set in self.sets:
            if not(set.is_possible(in_set)):
                return False
        return True
    
    def minimum_set(self):
        cubes = {}

        for _set in self.sets:
            for k, v in _set.cubes.items():
                if (k not in cubes) or (v > cubes[k]):
                    cubes[k] = v
        
        return Set(cubes)

class Set:
    def __init__(self, cubes: dict) -> None:
        self.cubes = cubes
    
    def is_possible(self, in_set):
        for k, v in in_set.cubes.items():
            if (k in self.cubes.keys()) and (v < self.cubes[k]):
                return False
        return True
    
    def total(self):
        total = 1

        for k, v in self.cubes.items():
            total *= v

        return total

def get_lines(file_path: str):

    lines = []
    with open(file_path) as file:
        # Traitement du fichier
        for line in file.readlines():
            lines.append(line)

    return lines

def load() -> list[Game]:
    games = []
    lines = get_lines("day2/input.txt")
    
    for line in lines:
        temp = line.split(':')

        game_id = int(temp[0].split(' ')[1])
        sets = []

        sets_string = temp[1].split(';')

        for set in sets_string:
            cubes = {}
            cubes_string = set.strip().split(', ')
            for cube in cubes_string:
                temp2 = cube.split(" ")

                cubes[temp2[1]] = int(temp2[0])

            new_set = Set(cubes)
            sets.append(new_set)
        
        game = Game(game_id)
        game.sets = sets

        games.append(game)
    return games

def main():

    entry_set = {
        'red': 12 ,
        'green': 13 ,
        'blue': 14 
    }
    games = load()
    print(len(games))

    remaining_games = []

    for game in games:
        if (game.is_possible(Set(entry_set))):
            remaining_games.append(game)

    print(len(remaining_games))

    count = 0
    for game in remaining_games:
        count += game.id
    count2 = 0
    for game in games:
        minimum_set = game.minimum_set()
        count2 += minimum_set.total()
    print(count)
    print(count2)

if __name__ == '__main__':
    main()
