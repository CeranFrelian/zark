import string
from items.Item import Item


class Sword(Item):
    def __init__(self, sword_name: string, sword_damage: int, sword_description: string):
        super(Sword, self).__init__()
        self.sword_name = sword_name
        self.sword_damage = sword_damage
        self.sword_description = sword_description

    def interact(self, command):
        if command == 'slice':
            self.slice()
            return
        elif command == 'stab':
            self.stab()
            return
        elif command == 'inspect':
            self.inspect()
            return

    def slice(self):
        print('I slice my opponent')

    def stab(self):
        print('I stab my opponent')

    def inspect(self):
        print(f'{self.sword_name}: {self.sword_description}')
