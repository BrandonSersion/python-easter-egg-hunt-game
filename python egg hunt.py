import random

class BasketEggHunt(object):
    current_room = "foyer"
    error = "error"
    number_of_eggs = 3
    basket_counter = 0
    egg_counter = 0
    won = False
    change = False
    move = False
    rooms = {
    "bedroom_1": {"north" : "error",
               "south" : "hallway_1",
               "east" : "error",
               "west" : "error"
               },
    "bedroom_2": {"north" : "error",
               "south" : "hallway_2",
               "east" : "error",
               "west" : "error"
              },
    "study":     {"north" : "error",
               "south" : "hallway_3",
               "east" : "error",
               "west" : "error"
              },
    "hallway_1": {"north" : "bedroom_1",
               "south" : "bathroom",
               "east" : "hallway_2",
               "west" : "error"
              },
    "hallway_2": {"north" : "bedroom_2",
               "south" : "kitchen",
               "east" : "hallway_3",
               "west" : "hallway_1"
              },
    "hallway_3": {"north" : "study",
               "south" : "foyer",
               "east" : "error",
               "west" : "hallway_2"
              },
    "bathroom": {"north" : "hallway_1",
               "south" : "error",
               "east" : "error",
               "west" : "error"
              },
    "kitchen": {"north" : "hallway_2",
               "south" : "error",
               "east" : "error",
               "west" : "error"
            },
    "foyer": {"north" : "hallway_3",
               "south" : "error",
               "east" : "error",
               "west" : "error"
           }
    }

    #global basket and egg counter  
    def __init__(self):
        print("Egg hunt!")
        print()
    
    def randomItems(self):
        room_choices = ["study", "kitchen", "bathroom", "bedroom_1", "bedroom_2"]
        self.basket_room = random.choice(room_choices)
        room_choices.remove(self.basket_room)
        i = 0
        self.egg_rooms = []
        while i < self.number_of_eggs:
            egg_room = random.choice(room_choices)
            self.egg_rooms.append(egg_room)
            room_choices.remove(egg_room)
            i+=1
        return self.basket_room, self.egg_rooms 
    
    def prompt_input(self):
        print("You are currently in the " + self.current_room)
        print()
        prompt = input(self.generate_prompt()).lower()
        if prompt == "north" or prompt == "south" or prompt == "east" or prompt == "west":
            if self.rooms[self.current_room][prompt] != "error":
                self.current_room = self.rooms[self.current_room][prompt]
                self.move = True
            else:
                print("Dead end! Try a different direction.")
        return self.current_room
    
    def generate_prompt(self):
        prompt_list = []
        if self.rooms[self.current_room]["north"] != "error":
            prompt_list.append("north")
        if self.rooms[self.current_room]["south"] != "error":
            prompt_list.append("south")
        if self.rooms[self.current_room]["east"] != "error":
            prompt_list.append("east")
        if self.rooms[self.current_room]["west"] != "error":
            prompt_list.append("west")
        self.prompt_full = "Which direction would you like to move? Options: " + str(prompt_list) + " "
        return self.prompt_full

    def check_basket(self):
        if self.current_room in self.basket_room:
            self.basket_counter = 1
            self.basket_room = ""
            print ("YOU FOUND THE BASKET, now go get those eggs")
            self.change = True

    def check_egg(self):
        if self.current_room in self.egg_rooms and self.basket_counter == 1:
            self.egg_counter+= 1
            self.egg_rooms.remove(self.current_room)
            print("YOU COLLECTED AN EGG!")
        elif self.current_room in self.egg_rooms and self.basket_counter == 0:
            print("You found an egg, but you need the basket first!")
        elif (self.change == False) and (self.move == True):
            print("Found nothing inside " + self.current_room + ". Keep moving!")
            
    def win_game(self):
        if self.basket_counter is 1 and self.egg_counter is 3:
            print()
            print ("CONGRATULATIONS you have won the game.")
            self.won = True
            

a = BasketEggHunt()
a.randomItems()
while not a.won:
    a.change = False
    a.move = False
    a.prompt_input()
    a.check_basket()
    a.check_egg()
    a.win_game()
