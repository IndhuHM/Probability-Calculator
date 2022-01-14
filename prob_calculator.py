import copy
import random
# Consider using the modules imported above.

class Hat:
   def __init__(self,**arg):
     self.contents=[]
     for key, value in arg.items():
       for i in range(value):
         self.contents.append(key)
     print (self.contents)

   def draw(self,number):
     drawn_balls = []
     if (number>len(self.contents)):
       return self.contents
     for i in range(number):
       chosen_balls = random.choice(self.contents)
       drawn_balls.append(chosen_balls)
       self.contents.remove(chosen_balls)
     return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count=0
  for i in range(num_experiments):
    expected_copy=copy.deepcopy(expected_balls)
    hat_copy=copy.deepcopy(hat)
    colors_got=hat_copy.draw(num_balls_drawn)

    for color in colors_got:
      if (color in expected_copy):
        expected_copy[color]-=1
  
    if(all(x<=0 for x in expected_copy.values())):
      count +=1

  return count/num_experiments