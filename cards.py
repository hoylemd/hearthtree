def slugify():
    pass


class Card(object):
    def __init__(self, name, cost, rarity, text):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.text = text

        self.slug = slugify(name)


class Minion(Card):
    def __init__(self, attack, health, race=None, *args, **kwargs):
        super(self, Minion).__init__(*args, **kwargs)

        self.attack = attack
        self.health = health
        self.race = race


class Spell(object):
    pass


class Weapon(Card):
    def __init__(self, damage, durability, *args, **kwargs):
        super(self, Minion).__init__(*args, **kwargs)

        self.damage = damage
        self.durability = durability
