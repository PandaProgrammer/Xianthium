from random import randint
from sys import *
import time



class Character:
    def __init__(self):
        self.name = "Tek"
        self.health = 1
        self.health_max = 1
        self.energy = 1
        self.energy_max = 1
        self.mana = 1
        self.mana_max = 1
        self.level = 1
        self.level_max = 1
        self.attack_style = ""
    def do_damage(self, enemy):
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health)
        enemy.health = enemy.health - damage
        if self.health < (self.health_max / 2):
            print ("%s is dying!" % self.name)
        if damage == 0: print ("%s evades %s's attack." % (enemy.name, self.name))
        else: print ("%s hurts %s!" % (self.name, enemy.name))
        return enemy.health <= 0

class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'a goblin'
    self.health = randint(1, player.health)
    self.energy = randint(1, player.energy)

class Soldier(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 20
    self.health_max = 20
    self.energy = 20
    self.energy_max = 20
    self.level = 1
    self.level_max = 50
    self.attack_style = "impales the"

  @staticmethod
  def quit(self):
    print ("%s can't find the way back home. \n%s plunges their sword into their stomach in defeat. \n%s has died. \nR.I.P." % (self.name, self.name, self.name))
    time.sleep(15)
    self.health = 0

  @staticmethod
  def help(self): print (Commands.keys())

  @staticmethod
  def status(self): 
      print (look)
      print ("%s's level: %d/%d" % (self.name, self.level, self.level_max))
      print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))
      print ("%s's energy: %d/%d" % (self.name, self.energy, self.energy_max))

  @staticmethod
  def tired(self):
    print ("%s used energy." % self.name)
    self.energy = max(1, self.energy - 1)
    if self.energy < (self.energy_max / 2):
        print ("%s feels tired." % self.name)

  @staticmethod
  def heal(self):
    if self.state != 'normal': print ("%s can't heal now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s heals." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely shoved by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s is all healed." % self.name)

  @staticmethod
  def rest(self):
    if self.state != 'normal': print ("%s can't rest now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s rests." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.energy < self.energy_max:
          self.energy = self.energy + 1
        else: print ("%s is not tired anymore." % self.name)

  @staticmethod
  def dance(self):
      if self.health != self.health_max and (randint(0, 99) % 3) == 0:
        print ("%s twirls around like a lunatic." % self.name)
        print ("For some odd reason, the gods liked that. The gods send their blessing.")
        self.health = self.health_max
      else:
        print ("%s twirls around like a lunatic." % self.name)

  @staticmethod
  def explore(self):
    if self.state != 'normal':
      print ("%s is too busy right now!" % self.name)
      self.enemy_attacks(self)
    else:
      print ("%s explores a twisty passage." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s encounters %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired(self)

  @staticmethod
  def flee(self):
    if self.state != 'fight': print ("%s runs in circles for a while." % self.name, self.tired(self))
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s couldn't escape from %s!" % (self.name, self.enemy.name), self.enemy_attacks(self))

  @staticmethod
  def attack(self):
    if self.state != 'fight': print ("%s swings their sword for no reason at all. Stop making a fool of yourself." % self.name, self.tired(self))
    else:
      if self.do_damage(self.enemy):
        print ("%s executes %s!" % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
            if self.level < self.level_max:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                self.energy = self.energy + 1
                self.energy_max = self.energy_max + 1
                self.level = self.level + 1
                print ("%s feels stronger!" % self.name)
      else: self.enemy_attacks(self)

  @staticmethod
  def enemy_attacks(self):
    if self.enemy.do_damage(self): 
      print ("%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name))
      time.sleep(15)




 
class Engineer(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 20
    self.health_max = 20
    self.energy = 20
    self.energy_max = 20
    self.level = 1
    self.level_max = 50
    self.attack_style = "skewers the"

  @staticmethod
  def quit(self):
    print ("%s can't find the way back home. \n%s places their crossbow under their chin and breathes one last time. \n%s has died. \nR.I.P." % (self.name, self.name, self.name))
    time.sleep(15)
    self.health = 0

  @staticmethod
  def help(self): print (Commands.keys())

  @staticmethod
  def status(self): 
      print (look)
      print ("%s's level: %d/%d" % (self.name, self.level, self.level_max))
      print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))
      print ("%s's energy: %d/%d" % (self.name, self.energy, self.energy_max))

  @staticmethod
  def tired(self):
    print ("%s used energy." % self.name)
    self.energy = max(1, self.energy - 1)
    if self.energy < (self.energy_max / 2):
        print ("%s feels tired." % self.name)

  @staticmethod
  def heal(self):
    if self.state != 'normal': print ("%s can't heal now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s heals." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely shoved by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s is all healed." % self.name)

  @staticmethod
  def rest(self):
    if self.state != 'normal': print ("%s can't rest now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s rests." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.energy < self.energy_max:
          self.energy = self.energy + 1
        else: print ("%s not tired anymore." % self.name)

  @staticmethod
  def dance(self):
      if self.health != self.health_max and (randint(0, 99) % 3) == 0:
        print ("%s twirls around like a lunatic." % self.name)
        print ("For some odd reason, the gods liked that. The gods send their blessing.")
        self.health = self.health_max
      else:
        print ("%s twirls around like a lunatic." % self.name)

  @staticmethod
  def explore(self):
    if self.state != 'normal':
      print ("%s is too busy right now!" % self.name)
      self.enemy_attacks(self)
    else:
      print ("%s explores a twisty passage." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s encounters %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired(self)

  @staticmethod
  def flee(self):
    if self.state != 'fight': print ("%s runs in circles for a while." % self.name, self.tired(self))
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s couldn't escape from %s!" % (self.name, self.enemy.name), self.enemy_attacks(self))

  @staticmethod
  def attack(self):
    if self.state != 'fight': print ("%s shoots arrows into the air for no reason at all. Stop making a fool of yourself." % self.name, self.tired(self))
    else:
      if self.do_damage(self.enemy):
        print ("%s executes %s!" % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
            if self.level < self.level_max:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                self.energy = self.energy + 1
                self.energy_max = self.energy_max + 1
                self.level = self.level + 1
                print ("%s feels stronger!" % self.name)
      else: self.enemy_attacks(self)

  @staticmethod
  def enemy_attacks(self):
    if self.enemy.do_damage(self): 
      print ("%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name))
      time.sleep(15)




 
class Necromancer(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 20
    self.health_max = 20
    self.mana = 20
    self.mana_max = 20
    self.level = 1
    self.level_max = 50
    self.attack_style = "releases the dead on"
    
  @staticmethod
  def quit(self):
    print ("%s can't find the way back home. \nThe dead grow restless and turn on %s. \n%s has died.\nR.I.P." % (self.name, self.name, self.name))
    time.sleep(15)
    self.health = 0

  @staticmethod
  def help(self): print (Commands.keys())

  @staticmethod
  def status(self): 
      print (look)
      print ("%s's level: %d/%d" % (self.name, self.level, self.level_max))
      print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))
      print ("%s's mana: %d/%d" % (self.name, self.mana, self.mana_max))

  @staticmethod
  def tired(self):
    print ("%s used mana." % self.name)
    self.mana = max(1, self.mana - 1)
    if self.mana < (self.mana_max / 2):
        print ("%s feels tired." % self.name)

  @staticmethod
  def heal(self):
    if self.state != 'normal': print ("%s can't heal now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s heals." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely shoved by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s is all healed." % self.name)

  @staticmethod
  def rest(self):
    if self.state != 'normal': print ("%s can't rest now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s rests." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.mana < self.mana_max:
          self.mana = self.mana + 1
        else: print ("%s not tired anymore." % self.name)

  @staticmethod
  def dance(self):
      if self.health != self.health_max and (randint(0, 99) % 3) == 0:
        print ("%s twirls around like a lunatic." % self.name)
        print ("For some odd reason, the gods liked that. The gods send their blessing.")
        self.health = self.health_max
      else:
        print ("%s twirls around like a lunatic." % self.name)

  @staticmethod
  def explore(self):
    if self.state != 'normal':
      print ("%s is too busy right now!" % self.name)
      self.enemy_attacks(self)
    else:
      print ("%s explores a twisty passage." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s encounters %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired(self)

  @staticmethod
  def flee(self):
    if self.state != 'fight': print ("%s runs in circles for a while." % self.name, self.tired(self))
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s couldn't escape from %s!" % (self.name, self.enemy.name), self.enemy_attacks(self))

  @staticmethod
  def attack(self):
    if self.state != 'fight': print ("%s tells the dead to fight eachother. Quit being sadistic!" % self.name, self.tired(self))
    else:
      if self.do_damage(self.enemy):
        print ("%s executes %s!" % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
            if self.level < self.level_max:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                self.mana = self.mana + 1
                self.mana_max = self.mana_max + 1
                self.level = self.level + 1
                print ("%s feels stronger!" % self.name)
      else: self.enemy_attacks(self)

  @staticmethod
  def enemy_attacks(self):
    if self.enemy.do_damage(self): 
      print ("%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name))
      time.sleep(15)





class Elementalist(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 20
    self.health_max = 20
    self.mana = 20
    self.mana_max = 20
    self.level = 1
    self.level_max = 50
    self.attack_style = "releases the golems on"
    
  @staticmethod
  def quit(self):
    print ("%s can't find the way back home. \nThe golems have turned on %s. \n%s has died.\nR.I.P." % (self.name, self.name, self.name))
    time.sleep(15)
    self.health = 0

  @staticmethod
  def help(self): print (Commands.keys())

  @staticmethod
  def status(self): 
      print (look)
      print ("%s's level: %d/%d" % (self.name, self.level, self.level_max))
      print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))
      print ("%s's mana: %d/%d" % (self.name, self.mana, self.mana_max))

  @staticmethod
  def tired(self):
    print ("%s used mana." % self.name)
    self.mana = max(1, self.mana - 1)
    if self.mana < (self.mana_max / 2):
        print ("%s feels tired." % self.name)

  @staticmethod
  def heal(self):
    if self.state != 'normal': print ("%s can't heal now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s heals." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s not tired anymore." % self.name)

  @staticmethod
  def rest(self):
    if self.state != 'normal': print ("%s can't rest now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s rests." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.energy < self.energy_max:
          self.energy = self.energy + 1
        else: print ("%s not tired anymore." % self.name)

  @staticmethod
  def dance(self):
      if self.health != self.health_max and (randint(0, 99) % 3) == 0:
        print ("%s twirls around like a lunatic." % self.name)
        print ("For some odd reason, the gods liked that. The gods send their blessing.")
        self.health = self.health_max
      else:
        print ("%s twirls around like a lunatic." % self.name)

  @staticmethod
  def explore(self):
    if self.state != 'normal':
      print ("%s is too busy right now!" % self.name)
      self.enemy_attacks(self)
    else:
      print ("%s explores a twisty passage." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s encounters %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired(self)

  @staticmethod
  def flee(self):
    if self.state != 'fight': print ("%s runs in circles for a while." % self.name, self.tired(self))
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s couldn't escape from %s!" % (self.name, self.enemy.name), self.enemy_attacks(self))

  @staticmethod
  def attack(self):
    if self.state != 'fight': print ("%s tells the golems to attack nothing causing a brawl. Quit being sadistic!" % self.name, self.tired(self))
    else:
      if self.do_damage(self.enemy):
        print ("%s executes %s!" % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
            if self.level < self.level_max:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                self.mana = self.mana + 1
                self.mana_max = self.mana_max + 1
                self.level = self.level + 1
                print ("%s feels stronger!" % self.name)
      else: self.enemy_attacks(self)

  @staticmethod
  def enemy_attacks(self):
    if self.enemy.do_damage(self): 
      print ("%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name))
      time.sleep(15)




 
class Sage(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 20
    self.health_max = 20
    self.mana = 20
    self.mana_max = 20
    self.level = 1
    self.level_max = 50
    self.attack_style = "strikes"
    
  @staticmethod
  def quit(self):
    print ("%s can't find the way back home. \nThe gods regret their decision and strike down %s with no mercy. \n%s has died. \nR.I.P." % (self.name, self.name, self.name))
    time.sleep(15)
    self.health = 0

  @staticmethod
  def help(self): print (Commands.keys())

  @staticmethod
  def status(self): 
      print (look)
      print ("%s's level: %d/%d" % (self.name, self.level, self.level_max))
      print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))
      print ("%s's mana: %d/%d" % (self.name, self.mana, self.mana_max))

  @staticmethod
  def tired(self):
    print ("%s used mana." % self.name)
    self.mana = max(1, self.mana - 1)
    if self.mana < (self.mana_max / 2):
        print ("%s feels tired." % self.name)

  @staticmethod
  def heal(self):
    if self.state != 'normal': print ("%s can't heal now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s heals." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely shoved by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s is all healed." % self.name)

  @staticmethod
  def rest(self):
    if self.state != 'normal': print ("%s can't rest now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s rests." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.energy < self.energy_max:
          self.energy = self.energy + 1
        else: print ("%s not tired anymore." % self.name)

  @staticmethod
  def dance(self):
      if self.health != self.health_max and (randint(0, 99) % 3) == 0:
        print ("%s twirls around like a lunatic." % self.name)
        print ("For some odd reason, the gods liked that. The gods send their blessing.")
        self.health = self.health_max
      else:
        print ("%s twirls around like a lunatic." % self.name)

  @staticmethod
  def explore(self):
    if self.state != 'normal':
      print ("%s is too busy right now!" % self.name)
      self.enemy_attacks(self)
    else:
      print ("%s explores a twisty passage." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s encounters %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired(self)

  @staticmethod
  def flee(self):
    if self.state != 'fight': print ("%s runs in circles for a while." % self.name, self.tired(self))
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s couldn't escape from %s!" % (self.name, self.enemy.name), self.enemy_attacks(self))

  @staticmethod
  def attack(self):
    if self.state != 'fight': print ("%s calls to the gods for assistance for no reason at all. Stop making a fool of yourself." % self.name, self.tired(self))
    else:
      if self.do_damage(self.enemy):
        print ("%s executes %s!" % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
            if self.level < self.level_max:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                self.mana = self.mana + 1
                self.mana_max = self.mana_max + 1
                self.level = self.level + 1
                print ("%s feels stronger!" % self.name)
      else: self.enemy_attacks(self)

  @staticmethod
  def enemy_attacks(self):
    if self.enemy.do_damage(self): 
      print ("%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name))
      time.sleep(15)






class Assassin(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 20
    self.health_max = 20
    self.energy = 20
    self.energy_max = 20
    self.level = 1
    self.level_max = 50
    self.attack_style = "stabs"
    
  @staticmethod
  def quit(self):
    print ("%s can't find the way back home. /nThe shadows converge and slice %s to pieces. \n%s has died. \nR.I.P." % (self.name, self.name, self.name))
    time.sleep(15)
    self.health = 0

  @staticmethod
  def help(self): print (Commands.keys())

  @staticmethod
  def status(self): 
      print (look)
      print ("%s's level: %d/%d" % (self.name, self.level, self.level_max))
      print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))
      print ("%s's energy: %d/%d" % (self.name, self.energy, self.energy_max))

  @staticmethod
  def tired(self):
    print ("%s used energy." % self.name)
    self.energy = max(1, self.energy - 1)
    if self.energy < (self.energy_max / 2):
        print ("%s feels tired." % self.name)

  @staticmethod
  def heal(self):
    if self.state != 'normal': print ("%s can't heal now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s heals." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely shoved by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s is all healed." % self.name)

  @staticmethod
  def rest(self):
    if self.state != 'normal': print ("%s can't rest now!" % self.name, self.enemy_attacks(self))
    else:
      print ("%s rests." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks(self)
      else:
        if self.energy < self.energy_max:
          self.energy = self.energy + 1
        else: print ("%s not tired anymore." % self.name)

  @staticmethod
  def dance(self):
      if self.health != self.health_max and (randint(0, 99) % 3) == 0:
        print ("%s twirls around like a lunatic." % self.name)
        print ("For some odd reason, the gods liked that. The gods send their blessing.")
        self.health = self.health_max
      else:
        print ("%s twirls around like a lunatic." % self.name)

  @staticmethod
  def explore(self):
    if self.state != 'normal':
      print ("%s is too busy right now!" % self.name)
      self.enemy_attacks(self)
    else:
      print ("%s explores a twisty passage." % self.name)
      if (randint(0, 99) % 3) == 0:
        self.enemy = Enemy(self)
        print ("%s encounters %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired(self)

  @staticmethod
  def flee(self):
    if self.state != 'fight': print ("%s runs in circles for a while." % self.name, self.tired(self))
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s couldn't escape from %s!" % (self.name, self.enemy.name), self.enemy_attacks(self))

  @staticmethod
  def attack(self):
    if self.state != 'fight': print ("%s slashes wildly in the air for nor reason at all. Stop making a fool of yourself." % self.name, self.tired(self))
    else:
      if self.do_damage(self.enemy):
        print ("%s executes %s!" % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
            if self.level < self.level_max:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                self.energy = self.energy + 1
                self.energy_max = self.energy_max + 1
                self.level = self.level + 1
                print ("%s feels stronger!" % self.name)
      else: self.enemy_attacks(self)

  @staticmethod
  def enemy_attacks(self):
    if self.enemy.do_damage(self): 
      print ("%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name))
      time.sleep(15)







 
print(  " __    __     _                            _         __  ___             _   _     _                 \n" + 
        "/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___   \ \/ (_) __ _ _ __ | |_| |__ (_)_   _ _ __ ___  \n" + 
        "\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   \  /| |/ _` | '_ \| __| '_ \| | | | | '_ ` _ \ \n" + 
        " \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |  /  \| | (_| | | | | |_| | | | | |_| | | | | | |\n" + 
        "  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  /_/\_\_|\__,_|_| |_|\__|_| |_|_|\__,_|_| |_| |_|\n" + 
        "                                                                                                     ")
print("                                     Creator: Kay Piotrowski")
print()
time.sleep(1)
print("***This world is currently in its beta.***")
print()
time.sleep(2)
print("Time to create your character!")
print()
time.sleep(1)
print("First you must pick a race.")
time.sleep(1)
print("Your choices are: Human, Elf, Fairy, Dwarf, or Giant")
time.sleep(1)
descr = input("What would you like to be? ")
descr = descr.lower()
print()


if descr == "human":
    look = "a simple looking humanoid with a "

elif descr == "elf":
    look = "a tall, thin, long eared elven with a "

elif descr == "fairy":
    look = "a small, winged fay with a "

elif descr == "dwarf":
    look = "a short stocky halfling with a "

elif descr == "giant":
    look = "a muscular colossus with a "

elif descr == "":
    print ("Okay, human then.")
    desc = "Human"
    look = "a simple looking humanoid with a "

elif descr != "":
    print ("Not a valid input. You get Human.")
    desc = "Human"
    look = "a simple looking humanoid with a "

Talent = {
    'soldier': Soldier(),
    'engineer': Engineer(),
    'necromancer': Necromancer(),
    'elementalist': Elementalist(),
    'sage': Sage(),
    'assassin': Assassin(),
    }

time.sleep(2)
print("Next, you must pick a class to fight as.")
time.sleep(1)
print("Your choices are: Soldier, Engineer, Necromancer, Elementalist, Sage, or Assassin")
time.sleep(1)
c = input("What would you like to be? ")
c = c.lower()
print()
time.sleep(1)

talentFound = False
while (talentFound is False):
    if len(c.lower()) > 0:
        for t in Talent.keys():
          if c[0] == t[:len(c[0])]:
            playerClass = Talent[c.lower()]
            talentFound = True
            break
        if not talentFound:
          print ("Not a valid class, try again!")
          c = input("What would you like to be? ")
          c = c.lower()
          time.sleep(2)

if c == "soldier": look += "suit of heavy metal armor and a sword to challenge even the bravest of foes."

elif c == "engineer": look += "suit of cloth armor, goggles, and a quiver strapped to their back, wielding a massive crossbow."

elif c == "necromancer": look += "cloak, black as death itself with shadows of souls floating around."

elif c == "elementalist": look += "ancient robe imbued with the mystical powers of the land and their elemental golems trail closely behind."

elif c == "sage": look += "godlike shining armor wielding a war hammer blessed by the gods themselves."

elif c == "assassin": look += "trench coat that blends with shadows and two daggers whose blades are glistening red."

Commands = {
    'explore': playerClass.explore,
    'status': playerClass.status,
    'attack': playerClass.attack,
    'flee': playerClass.flee,
    'heal': playerClass.heal,
    'rest': playerClass.rest,
    'dance':playerClass.dance,
    'help': playerClass.help,
    'quit': playerClass.quit,
    }

p = playerClass
print("Next you must choose a name.")
time.sleep(2)
p.name = input("What is your character's name? ")
p.name = p.name.title()
time.sleep(1)
if (p.name == ""):
    p.name = "Balducci"
    print("Fine, you get Balducci as your name.")
time.sleep(.5)
look = p.name + ", " + look
print()
print(look)
print()
time.sleep(4)
print("Goodluck on your adventure!")
print()
print (Commands.keys())
print ("\n(type help to get the list of actions again)\n")
time.sleep(4)
print ("%s enters a dark cave, searching for adventure." % p.name)
 
while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for a in Commands.keys():
      if args[0] == a[:len(args[0])]:
        Commands[a](Talent[c])
        commandFound = True
        break
    if not commandFound:
      print ("%s doesn't understand the suggestion." % p.name)


      """ BASE GAME COPYRIGHT INFO
Copyright 2010 Francesco Balducci
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
See <http://www.gnu.org/licenses/> for a copy of the GNU General Public License.
"""
