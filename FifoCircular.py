from datetime import datetime
import random
from random import randrange

class FIFOCircular():

    data = [];
    last = 0;
    
    def __init__(self):
       self.generateValues();
       self.inAction();
       print(self.last)

    def changeFrame(self, values):

      position = {
          'time':datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"),
          'weight': values['weight'],
          'next': values['next'],
          'BR':0,
          'BM':0
        }

      return position;

    def inAction(self):
      for values in self.data:
        index = self.data.index(values)
        if(values['BM'] == 1):
          self.data.remove(values)
          self.data.insert(index, self.changeFrame(values))
          continue;
        if(values['BR'] == 1):
          values['BR'] = 0
          continue;
        else:
          values['BR'] = 1
          self.last = self.data.index(values)
          break;
        

    def generateValues(self):
      i = 0;
      for i in range(0, 201):

        position = {
          'time':datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f"),
          'weight': random.random(),
          'next': i if i != 200 else 0,
          'BR':randrange(2),
          'BM':randrange(2)
        }

        self.data.append(position)

if __name__ == '__main__':
    FIFOCircular()
