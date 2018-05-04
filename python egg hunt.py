import random

"""Python console game. The game map is stored in a double nested dictionary.
   The user controls movement by typing 'north', 'south', 'east', or 'west'
   in the terminal. The win condition is to find a basket, then three eggs."""


class Game(object):
    # class constants that store game map
    WALL = 'wall'
    ROOMS = {
        'bedroom_1': {
            'north': WALL,
            'south': 'hallway_1',
            'east': WALL,
            'west': WALL
        },
        'bedroom_2': {
            'north': WALL,
            'south': 'hallway_2',
            'east': WALL,
            'west': WALL
        },
        'study': {
            'north': WALL,
            'south': 'hallway_3',
            'east': WALL,
            'west': WALL
        },
        'hallway_1': {
            'north': 'bedroom_1',
            'south': 'bathroom',
            'east': 'hallway_2',
            'west': WALL
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
            'east': WALL,
            'west': 'hallway_2'
        },
        'bathroom': {
            'north': 'hallway_1',
            'south': WALL,
            'east': WALL,
            'west': WALL
        },
        'kitchen': {
            'north': 'hallway_2',
            'south': WALL,
            'east': WALL,
            'west': WALL
        },
        'foyer': {
            'north': 'hallway_3',
            'south': WALL,
            'east': WALL,
            'west': WALL
        }
    }

    # Set up initial game state.
    # instance variables that track game state
    def __init__(
            self,
            basket_on_map=True,  # True or False
            eggs_on_map=3,  # 1-4
            rooms_that_can_have_items=['bedroom_1', 'bedroom_2', 'study',
                                       'bathroom', 'kitchen'],
            basket_room='',
            egg_rooms=[],
            current_room='foyer'):
        # settings variables
        self.basket_on_map = basket_on_map  # assign basket?, track win condition
        self.eggs_on_map = eggs_on_map  # assign how many eggs?, track win condition
        self.rooms_that_can_have_items = rooms_that_can_have_items
        # application variables
        self.basket_room = basket_room  # randomized each game
        self.egg_rooms = egg_rooms  # randomized each game
        self.current_room = current_room

    def __str__(self):
        return 'Left on map - Basket: ' + str(self.basket_on_map) + ', Eggs: '\
            + str(self.eggs_on_map)

    # functions that initialize game
    def print_instructions(self):
        print("""
        EGG HUNT!

        The object of the game is to find a basket then collect three eggs.

        You move through the house by entering:
              'north', 'south', 'east', or 'west'
        """)

    def randomize_basket_placement(self):
        if self.basket_on_map:
            self.basket_room = random.choice(self.rooms_that_can_have_items)
            self.rooms_that_can_have_items.remove(self.basket_room)

    def randomize_egg_placement(self):
        i = 0
        while self.eggs_on_map > i:
            egg_room = random.choice(self.rooms_that_can_have_items)
            self.egg_rooms.append(egg_room)
            self.rooms_that_can_have_items.remove(egg_room)
            i += 1

    # Functions to run game

    # Helper function
    def get_options(self):
        options = []
        if self.ROOMS[self.current_room]['north'] != self.WALL:
            options.append('north')
        if self.ROOMS[self.current_room]['south'] != self.WALL:
            options.append('south')
        if self.ROOMS[self.current_room]['east'] != self.WALL:
            options.append('east')
        if self.ROOMS[self.current_room]['west'] != self.WALL:
            options.append('west')
        return options

    # Main game functions
    def prompt_user_input(self):
        print()
        options = self.get_options()
        prompt = input('Enter the direction you want to move? Options: '
                       + str(options) + '  ').lower()
        if prompt in options:
            self.current_room = self.ROOMS[self.current_room][prompt]
        else:
            print('Dead end! Try a different direction.')

    def check_room_for_basket(self):
        if self.current_room == self.basket_room:
            self.basket_on_map = False
            print('YOU FOUND THE BASKET in the ' + self.current_room
                  + '. Now go get those eggs!')
        elif self.current_room in self.egg_rooms:
            print('You found an egg in the ' + self.current_room
                  + ', but you need the basket first!')
        else:
            print('Found nothing in the ' + self.current_room)

    def check_room_for_egg(self):
        if self.current_room in self.egg_rooms:
            self.eggs_on_map -= 1
            self.egg_rooms.remove(self.current_room)
            print('YOU FOUND AN EGG in the ' + self.current_room + '. ' +
                  str(self.eggs_on_map) + ' left!')
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
while game_instance.eggs_on_map > 0:
    game_instance.prompt_user_input()
    if game_instance.basket_on_map:
        game_instance.check_room_for_basket()
    else:
        game_instance.check_room_for_egg()
game_instance.win_game()
