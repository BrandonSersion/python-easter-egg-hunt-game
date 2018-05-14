import random

"""Python console game.

   The game map is stored in a double nested dictionary.
   The user controls movement by typing 'north', 'south', 'east', or 'west'
   in the terminal. The win condition is to find a basket, then three eggs."""


class Game:
    # Game map.
    WALL = 'wall'
    ROOMS = {
        'bedroom': {
            'west': WALL,
            'east': WALL,
            'south': 'hallway 1',
            'north': WALL,
        },
        'dining room': {
            'west': WALL,
            'east': WALL,
            'south': 'hallway 2',
            'north': WALL,
        },
        'study': {
            'west': WALL,
            'east': WALL,
            'south': 'hallway 3',
            'north': WALL,
        },
        'hallway 1': {
            'west': WALL,
            'east': 'hallway 2',
            'south': 'bathroom',
            'north': 'bedroom',
        },
        'hallway 2': {
            'west': 'hallway 1',
            'east': 'hallway 3',
            'south': 'kitchen',
            'north': 'dining room',
        },
        'hallway 3': {
            'west': 'hallway 2',
            'east': WALL,
            'south': 'foyer',
            'north': 'study',
        },
        'bathroom': {
            'west': WALL,
            'east': WALL,
            'south': WALL,
            'north': 'hallway 1',
        },
        'kitchen': {
            'west': WALL,
            'east': WALL,
            'south': WALL,
            'north': 'hallway 2',
        },
        'foyer': {
            'west': WALL,
            'east': WALL,
            'south': WALL,
            'north': 'hallway 3',
        }
    }

    # Set up.
    def __init__(
            self,
            basket_on_map=True,  # True or False
            eggs_on_map=3,  # 1-4
            # WARNING the following default gets overwritten on manipulation.
            # (All mutable types behave this way.)
            rooms_that_can_have_items=
                ['bedroom', 'dining room', 'study', 'bathroom', 'kitchen',],
            basket_room='',
            egg_rooms=[],
            current_room='foyer'):
        self.basket_on_map = basket_on_map
        self.eggs_on_map = eggs_on_map
        self.rooms_that_can_have_items = rooms_that_can_have_items
        self.basket_room = basket_room
        self.egg_rooms = egg_rooms
        self.current_room = current_room

    def __repr__(self):
        basket_status = 'Yes' if self.basket_on_map else 'No'
        return (
            'Remaining on the map -' 
            f' Basket: {basket_status}, Eggs: {self.eggs_on_map}')

    @staticmethod
    def print_instructions():
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

    # 'Run game' helper.
    def get_nearby_directions(self):
        for key, value in self.ROOMS[self.current_room].items():
            if value is not self.WALL:
                yield key
        yield 'status'

    # Run game.
    def prompt_user_input(self):
        print()
        directions = self.get_nearby_directions()
        prompt = (input(
            'Enter the direction you want to move. Options: '
            f'{", ".join([*directions])}.     >')
            .lower())
        directions = self.get_nearby_directions()  # reset generator
        if prompt == 'status':
            print(self)
        elif prompt in [*directions]:
            self.current_room = self.ROOMS[self.current_room][prompt]
        else:
            print('Dead end! Try a different direction.')

    def check_room_for_basket(self):
        if self.current_room is self.basket_room:
            self.basket_on_map = False
            print(
                f'YOU FOUND THE BASKET in the {self.current_room}.'
                ' Now go get those eggs!')
        elif self.current_room in self.egg_rooms:
            print(
                f'You found an egg in the {self.current_room}'
                ', but you need the basket first!')
        else:
            print(f'You are in the {self.current_room}.')

    def check_room_for_egg(self):
        if self.current_room in self.egg_rooms:
            self.eggs_on_map -= 1
            self.egg_rooms.remove(self.current_room)
            print(
                f'YOU FOUND AN EGG in the {self.current_room}.'
                f' {self.eggs_on_map} left!')
        else:
            print(f'You are in the {self.current_room}.')

    @staticmethod
    def win_game():
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
