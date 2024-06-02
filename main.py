import os
from Character import Hero, Enemy
from Weapon import short_bow, iron_sword

hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon = short_bow)

while True:
    os.system("cls")
    
    hero.attack(enemy)
    enemy.attack(hero)
    hero.health_bar.draw()
    enemy.health_bar.draw()
     
     #hero.drop()
    input()