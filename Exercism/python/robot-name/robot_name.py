import random

class Robot(object):
    def __init__(self):
        self.name = self.genName()
    
    def genName(self):
        number = random.randint(0,1000)
        if number < 10:
            strNumber = '00'+str(number)
        elif number < 100:
            strNumber = '0'+str(number)
        else:
            strNumber = str(number)
        letter1 = chr(random.randint(65,91))
        letter2 = chr(random.randint(65,91))
        return letter1 + letter2 + strNumber

    def reset(self):
        random.seed('Alimorph The Almighty')
        self.name = self.genName()