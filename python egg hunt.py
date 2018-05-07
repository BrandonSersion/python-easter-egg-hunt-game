import random

"""Python console game. The game map is stored in a double nested dictionary.
   The user controls movement by typing 'north', 'south', 'east', or 'west'
   in the terminal. The win condition is to find a basket, then three eggs."""


class Game:
    # Game map.
    WALL = 'wall'
    ROOMS = {
        'bedroom_1': {
            'west': WALL,
            'east': WALL,
            'south': 'hallway_1',
            'north': WALL
        },
        'bedroom_2': {
            'west': WALL,
            'east': WALL,
            'south': 'hallway_2',
            'north': WALL
        },
        'study': {
            'west': WALL,
            'east': WALL,
            'south': 'hallway_3',
            'north': WALL
        },
        'hallway_1': {
            'west': WALL,
            'east': 'hallway_2',
            'south': 'bathroom',
            'north': 'bedroom_1'
        },
        'hallway_2': {
            'west': 'hallway_1',
            'east': 'hallway_3',
            'south': 'kitchen',
            'north': 'bedroom_2'
        },
        'hallway_3': {
            'west': 'hallway_2',
            'east': WALL,
            'south': 'foyer',
            'north': 'study'
        },
        'bathroom': {
            'west': WALL,
            'east': WALL,
            'south': WALL,
            'north': 'hallway_1'

        },
        'kitchen': {
            'west': WALL,
            'east': WALL,
            'south': WALL,
            'north': 'hallway_2'
        },
        'foyer': {
            'west': WALL,
            'east': WALL,
            'south': WALL,
            'north': 'hallway_3'
        }
    }

    # Set up.
    def __init__(
            self,
            basket_on_map=True,  # True or False
            eggs_on_map=3,  # 1-4
            rooms_that_can_have_items=['bedroom_1', 'bedroom_2', 'study',
                                       'bathroom', 'kitchen'],
            basket_room='',
            egg_rooms=[],
            current_room='foyer'):

        self.basket_on_map = basket_on_map
        self.eggs_on_map = eggs_on_map
        self.rooms_that_can_have_items = rooms_that_can_have_items
        self.basket_room = basket_room
        self.egg_rooms = egg_rooms
        self.current_room = current_room

    def __str__(self):
        return 'Remaining on the map - Basket: ' + str(self.basket_on_map) + ', Eggs: '\
            + str(self.eggs_on_map)

    def print_instructions(self):
        print("""
        EGG HUNT!

        The object of the game is to find a basket then collect three eggs.

        You move through the house by entering:
              'north', 'south', 'east', or 'west'
        """)

    def randomize_basket_room(self):
        if self.basket_on_map:
            self.basket_room = random.choice(self.rooms_that_can_have_items)
            self.rooms_that_can_have_items.remove(self.basket_room)

    def randomize_egg_rooms(self):
        i = 0
        while self.eggs_on_map > i:
            egg_room = random.choice(self.rooms_that_can_have_items)
            self.egg_rooms.append(egg_room)
            self.rooms_that_can_have_items.remove(egg_room)
            i += 1

    # Run game helper.
    def get_prompt_options(self):
        options = ['status']
        for key, value in self.ROOMS[self.current_room].items():
            if value != self.WALL:
                options.insert(0, key)
        return options

    # Run game.
    def prompt_user_input(self):
        print()
        options = self.get_prompt_options()
        prompt = input('Enter the direction you want to move? Options: '
                       + str(options) + '  ').lower()
        if prompt == 'status':
            print(self.__str__())
        elif prompt in options:
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
            print('You are in the ' + self.current_room + '.')

    def check_room_for_egg(self):
        if self.current_room in self.egg_rooms:
            self.eggs_on_map -= 1
            self.egg_rooms.remove(self.current_room)
            print('YOU FOUND AN EGG in the ' + self.current_room + '. ' +
                  str(self.eggs_on_map) + ' left!')
        else:
            print('You are in the ' + self.current_room + '.')

    def win_game(self):
            print()
            print('CONGRATULATIONS you have found all the eggs.')


def main():
    # Set up.
    game_instance = Game()
    game_instance.print_instructions()
    game_instance.randomize_basket_room()
    game_instance.randomize_egg_rooms()

    # Run game.
    while game_instance.eggs_on_map > 0:
        game_instance.prompt_user_input()
        if game_instance.basket_on_map:
            game_instance.check_room_for_basket()
        else:
            game_instance.check_room_for_egg()
    game_instance.win_game()


if __name__ == "__main__":
    main()
