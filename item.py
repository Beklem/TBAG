class Item:
    def __init__(self):
        self.name = "Camera"
        self.description = None
        self.uses = 0

    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.description = item_description

    def use(self):
        self.uses += 1
        if self.uses == 1:
            print("The camera captures a cute picture of Aligail with a peace sign.")
            print("You receive a cute photo!")
        if self.uses == 2:
            print("The camera snaps Haley in a beautiful capsule of her own divine energy!")
            print("You receive a flirty photo!")
        if self.uses == 3:
            print("The camera captures an eccentric ghost in a moment of uproaring, almost villianious laughter!")
            print("You receive a candid photo!")

    def get_uses(self):
        return self.uses
    