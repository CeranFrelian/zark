from items.weapons.Sword import Sword

starter_sword = Sword(sword_name='Rusty Sword', sword_damage=2,
                      sword_description='A Sword that has more rust than lethality. Brittle to the touch, it is only '
                                        'the weapon of one who is desperate.')

print('Here is your sword!')
starter_sword.interact('inspect')
