#Сайков К и Осипов Н группа ПМ1802
import random
class bird: 
     def fly(self,y):
          if self.flying :
               self.y += y
               print("персонаж " + self.name + " переместился в точку " + str(self.y) + " по y")
          else:
               print("ne mogy letat")
          
class carapter(bird):
     def __init__(self,name, flying , case=[{'еда':[],'одежда':[]}] , x = 0 , y = 0, health = 100 , speed = 1000 , obj=0, tp = 0):
          self.flying = flying
          self.x = 0
          self.y = 0
          self.case = [{'еда':[],'одежда':[]}]
          self.name = name
          self.health = 100
          self.speed = 1000
          self.obj = obj
          self.tp = tp
          print("Ia rodilsa " + self.name)
          
     def run(self,x):
          self.x = self.x + x
          
     def take(self, obj, tp):
         if tp == 'еда' or tp == 'одежда':
              for line in self.case:
                   line[tp].append(obj)
                   print('Ura, noviy predmet!')
                   if tp == 'одежда' and 0 < self.health <90:
                        self.health += 10
                        print("vashe zdorovie popvisilos na 10")
                   else:
                        self.health = 100
                        print("vashe zdorovie na max")
         else:
               print('ошибка ввода')
                   
                   

     def eat(self):
         for line in self.case:
             if len(line['еда']) > 0:
                 line['еда'] = line['еда'][1:]
                 if 0 < self.health < 90:
                     self.health += 10
                 elif self.health >= 90:
                     self.health = 100
                 print("vashe zdorovie popvisilos na 10")
             else:
                 print('Edy net, no vi dergitec')
              
                 
     def shoot(self , other):
          if len(other)> 0 :
               other[0].health -= random.randint(1, other[0].health)
               other[0].speed   = other[0].speed * other[0].health / 100
               print(other[0].name +" 'ААААА Я РАНЕН'" + " ,но у меня еще есть здоровье! " + str(other[0].health) + " en moy skoroct' " + str(round(other[0].speed)))
               if other[0].health > 0 :
                    print("Я вернусь...")
               else :
                    print("или нет....")
                    del  other[0]
hero_1 = carapter("Ivan",True ) 
hero_2 = carapter("Ira", False) 
hero_1.run(3)
hero_1.take('banan','еда')
hero_1.shoot([hero_2]) 
hero_1.run(100)
hero_1.fly(1000)
hero_2.take('banan','еда')
hero_2.eat()
hero_2.take('jacket','одежда')
hero_2.health


