import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, red=None, green=None, orange=None, black=None, blue=None, pink=None, yellow=None, test=None, striped=None) -> None:
    self.red = red
    self.orange = orange
    self.black = black
    self.blue = blue
    self.pink = pink
    self.striped = striped
    self.green = green
    self.yellow = yellow
    self.test = test
    self.contents = []

    for value in self.__dict__:
      dict_value = self.__dict__[value]

      if dict_value is not None and isinstance(dict_value, list) is False:
        for _ in range(dict_value):
          self.contents.append(value)

  def draw(self, balls):
    to_draw = balls
    drawn = []
    if to_draw > len(self.contents):
      return self.contents

    while to_draw > 0:
      index = random.randint(0, len(self.contents)-1)
      drawn.append(self.contents[index])
      self.contents.pop(index)
      to_draw -= 1

    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_success = 0
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)
    success = True
    for key, value in expected_balls.items():
      if drawn.count(key) < value:
        success = False
        break
    if success:
      num_success += 1

  return num_success / num_experiments