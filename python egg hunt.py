import random

"""Python console game. The game map is stored in a double nested dictionary.
   The user controls their movement by typing 'north', 'south', 'east', or
   'west' in the terminal."""


class Game(object):
    # The house layout is represented in this dictionary.
    wall = 'wall'
    rooms = {
        'bedroom_1': {
            'north': wall,
            'south': 'hallway_1',
            'east': wall,
            'west': wall
        },
        'bedroom_2': {
            'north': wall,
            'south': 'hallway_2',
            'east': wall,
            'west': wall
        },
        'study': {
            'north': wall,
            'south': 'hallway_3',
            'east': wall,
            'west': wall
        },
        'hallway_1': {
            'north': 'bedroom_1',
            'south': 'bathroom',
            'east': 'hallway_2',
            'west': wall
        },
        'hallway_2': {
            'north': 'bedroom_2',
            'south': 'kitchen',
            'east': 'hallway_3',
            'west': 'hallway_1'
        },
        'hallway_3': {
            'north': 'study',
            'south': 'foyer',
            'east': wall,
            'west': 'hallway_2'
        },
        'bathroom': {
            'north': 'hallway_1',
            'south': wall,
            'east': wall,
            'west': wall
        },
        'kitchen': {
            'north': 'hallway_2',
            'south': wall,
            'east': wall,
            'west': wall
        },
        'foyer': {
            'north': 'hallway_3',
            'south': wall,
            'east': wall,
            'west': wall
        }
    }

    # Functions to set up initial game state
    def __init__(self, basket_found=False, number_of_eggs=3,
                 current_room='foyer',
                 rooms_that_can_have_items=['bedroom_1', 'bedroom_2', 'study',
                                            'bathroom', 'kitchen']):
        self.basket_found = basket_found
        self.number_of_eggs = number_of_eggs
        self.current_room = current_room
        self.rooms_that_can_have_items = rooms_that_can_have_items

    def print_instructions(self):
        print("""
        EGG HUNT!

        The object of the game is to find a basket then collect three eggs.

        You move through the house by typing the cardinal directions:
              'north', 'south', 'east', or 'west'
        """)

    def randomize_basket_placement(self):
        self.basket_room = random.choice(self.rooms_that_can_have_items)
        self.rooms_that_can_have_items.remove(self.basket_room)

    def randomize_egg_placement(self):
        self.egg_rooms = []
        i = 0
        while self.number_of_eggs > i:
            egg_room = random.choice(self.rooms_that_can_have_items)
            self.egg_rooms.append(egg_room)
            self.rooms_that_can_have_items.remove(egg_room)
            i += 1

    # Functions to run game

    # Helper function
    def preview_adjacent_directions(self):
        adjacent_directions = []
        if self.rooms[self.current_room]['north'] != self.wall:
            adjacent_directions.append('north')
        if self.rooms[self.current_room]['south'] != self.wall:
            adjacent_directions.append('south')
        if self.rooms[self.current_room]['east'] != self.wall:
            adjacent_directions.append('east')
        if self.rooms[self.current_room]['west'] != self.wall:
            adjacent_directions.append('west')
        return adjacent_directions

    # Main functions
    def prompt_user_input(self):
        print()
        adjacent_directions = self.preview_adjacent_directions()
        prompt = input('Which direction would you like to move? Options: '
                       + str(adjacent_directions) + ' ').lower()
        if prompt in adjacent_directions:
            self.current_room = self.rooms[self.current_room][prompt]
        else:
            print('Dead end! Try a different direction.')

    def check_room_for_basket(self):
        if self.current_room == self.basket_room:
            self.basket_found = True
            print('YOU FOUND THE BASKET in the ' + self.current_room
                  + '. Now go get those eggs!')
        elif self.current_room in self.egg_rooms:
            print('You found an egg in the ' + self.current_room
                  + ', but you need the basket first!')
        else:
            print('Found nothing in the ' + self.current_room)

    def check_room_for_egg(self):
        if self.current_room in self.egg_rooms:
            self.number_of_eggs -= 1
            self.egg_rooms.remove(self.current_room)
            print('YOU FOUND AN EGG in the ' + self.current_room + '. ' +
                  str(self.number_of_eggs) + ' left!')
        else:
            print('Found nothing inside ' + self.current_room)

    def win_game(self):
            print()
            print('CONGRATULATIONS you have won the game.')


# Set up initial game state
game_instance = Game()
game_instance.print_instructions()
game_instance.randomize_basket_placement()
game_instance.randomize_egg_placement()

# Run game
while game_instance.number_of_eggs > 0:
    game_instance.prompt_user_input()
    if not game_instance.basket_found:
        game_instance.check_room_for_basket()
    else:
        game_instance.check_room_for_egg()
game_instance.win_game()
