import time

class Abilities():
    """
    Ability class to define possible actions for cards.

    Arguments:
        name (str): The name of the ability (e.g., 'explore', 'attack').

    Methods:
        condition(): The condition for the ability to trigger. Defined in subclass.
        execute(): Exectures action() if condition() is met.
        action(): Performs the specific ability. Defined in subclass.
    """
    def __init__(self, name: str):
        self.name = name
    
    def condition(self, card, *args, **kwargs):     # method will be overwritten by subclass
        pass

    def execute(self, card, *args, **kwargs):
        if self.condition(card, *args, **kwargs):
            self.action(*args, **kwargs)
    
    def action(self, card, *args, **kwargs):        # method will be overwritten by subclass
        pass

class Attack(Abilities):
    """
    Standard attack ability that only attacks other enemy units
    """
    def __init__(self, cooldown: int=10):
        super().__init__("acttack")
        self.cooldown = cooldown
        self.last_attack_time = None                # Track the last time the attack was used
    
    def condition(self, card, target):
        return target.card_type == "Enemy"
    
    def action(self, card, target):
        current_time = time.time()
        if self.last_attack_time is None or current_time - self.last_attack_time >= self.cooldown:
            self.last_attack_time = current_time
            target.hp =- card.atk
            card.hp =- target.atk
            print(f"{current_time}: {card.name} attacked {target.name}, dealing {card.atk} damage.")
            print(f"{current_time}: {target.name} dealt {target.atk} damage to {card.name}.")

class Explore(Abilities):
    def __init__(self):
        super().__init__("explore")

    def condition(self, card, *args, **kwargs):
        return card.card_type == "Explore"

    def action(self, card, *args, **kwargs):
        print(f"{card.name} in on an exploration.")

class Summon(Abilities):
    def __init__(self):
        super().__init__("summon")

    def condition(self, card, *args, **kwargs):
        # Need to figure out how to do summoning/crafting.
        return card.card_type == "Summon"
    
    def action(self, card, *args, **kwargs):
        print(f"{card.name} summons a familiar.")

witch_abilities = [Explore(), Summon(), Attack()]
enemy_abilities = [Attack()]