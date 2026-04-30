# this is the class for the heros in the party
print("you enter ")

class hero:
    def __init__(self,name,hp,dmg,):
        self.name = name
        self.hp = hp
        self.dmg = dmg
       # self.heal = heal
#this allows the heros to attack
    def attack(self):
        print(f"{self.name} attacks the dragon for {self.dmg} damage")
#this heals heros
    def heal(self):
        
        print(f"{self.name} heals {self.name} for 20")
#this is the inspect for your heros
    def inspect(self):
        print(f"{self.name} has {self.hp} hp")
    
    def debuff(self):
        print(f"{self.name} debuffs the dragon reducing its max health by 70" )
    
    def fireball(self):
        print(f"{self.name} casts fire ball causing an explosion dealing 10 damage to the party but also damages the dragon for {self.dmg}")
    
    def buff(self):
        print(f"{self.name} has buffed the party giving everyone one an extra 5 damage on attack for 3 turns.")


#these are the hero classes to chose from

barbarian = hero("barbarian", 150, 35)

ranger =  hero("ranger", 120, 40)

healer =  hero("healer", 70, 20)

wizard = hero("wizard", 80, 60 )

warlock = hero("warlock", 100, 70 )

bard = hero("bard", 70, 25)

#these are the actions the heros are using

barbarian.attack()

ranger.attack()

healer.heal()

ranger.inspect()

wizard.fireball()

warlock.debuff()

bard.buff()

# this is the class for the boss and enemys
class enemy:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def attack(self):
        print(f"{self.name} attacks you for {self.dmg} damage")

    def AOE_fire_dragon(self):
        print(f"the {self.name} roars, before it spews fire at the party. dealing {self.dmg} damage to the party.")

    def servent_meal(self):
        print(f"{self.name} heals {self.name} for 20 health")

grunt = enemy("kobold", 30, 10)

boss = enemy("dragon", 500, 25)

grunt.attack()

grunt.servent_meal()

boss.attack()

boss.AOE_fire_dragon()
