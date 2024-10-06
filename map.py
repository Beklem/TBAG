#coding the map

class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {} #starts an empty dictionary
        self.character = None
        self.visited_rooms = set()

    def visit_room(self, room_name):
        self.visited_rooms.add(room_name)

    def has_visited(self, room_name):
        return room_name in self.visited_rooms
    
    def check_event_trigger(room_visits):
        if room_visits.has_visited("meetingRoom") and  room_visits.has_visited("storytimeRoom"):


            def set_linked_rooms(self, direction, room):
                self.linked_rooms[direction] = room

    def get_linked_room(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            return None

    def get_description(self):
        return self.description
    
    def set_description(self, room_description):
        self.description == room_description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name
    
    def get_details(self):
        print(self.name)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            if isinstance(room, Room):
                print(f"The {room.get_name()} is {direction}.")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_room[direction]
        else:
            print("The spirits whoosh all around you. They urge to to turn back, as unfathomable danger follows closely.")
            return None
        
