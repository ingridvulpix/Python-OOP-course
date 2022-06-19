import random

class Rectangle:
    def __init__(self):
        self.x1 = random.randint(0,5)
        self.y1 = random.randint(0,5)
        self.x2 = random.randrange(self.x1+1,10,1)
        self.y2 = random.randrange(self.y1+1,10,1)
        self.triggers()
    
    def triggers(self):
        self.show_rect_coord()
        self.get_guess()
    
    def show_rect_coord(self):
        print(f'Rectangle Coordinates: {self.x1},{self.y1} and {self.x2}, {self.y2}')

    def get_guess(self):
        guess_x = int(input('Guess point x coord: '))
        guess_y = int(input('Guess point y coord: '))
        self.is_in(guess_x,guess_y)
    
    def is_in(self,x_user,y_user):
        is_in_x = False
        is_in_y = False
        if x_user in range(self.x1,self.x2+1):
            is_in_x = True
        else:
            is_in_x = False
        if y_user in range(self.y1,self.y2+1):
            is_in_y = True
        else:
            is_in_y = False
        self.coord_answer(is_in_x , is_in_y)
    
    def coord_answer(self, is_in_x, is_in_y):
        is_in = is_in_x and is_in_y
        print(f'Your point was inside rectangle: {is_in}')
        return

test1 = Rectangle()

    


