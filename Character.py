from Weapon import fists
from health_bar import HealthBar

class Character:
   
    
    
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health
       # self.damage = damage 
        
        self.Weapon = fists
         
    def attack (self, target) -> None:
            target.health -=self.Weapon.damage
            target.health = max(target.health, 0)
            target.health_bar.update()
            print(f"{self.name} dealt {self.Weapon.damage} damage to {target.name} with {self.Weapon.name}")
     
            

class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int
                 )->None:
        super().__init__(name=name, health=health)
        
        self.default_weapon = self.Weapon
        self.health_bar = HealthBar(self, color="green")
        
    def equip(self, weapon)->None:
        self.Weapon=weapon
        print(f"{self.name} equipped a(n){self.Weapon.name}!")
        
    def drop(self)->None:
        print(f"{self.name} dropped the {self.Weapon.name}!")
        self.Weapon = self.default_weapon
        
        
        
class Enemy(Character):
   def __init__(self,
             name: str,
             health: int,
             weapon
             ) -> None:
    super().__init__(name=name, health=health)
    self.Weapon = weapon 
    self.health_bar = HealthBar(self, color="red")
