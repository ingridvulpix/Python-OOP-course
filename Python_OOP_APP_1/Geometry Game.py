import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def inside_rectangle(self, rec):
        if rec.lowleft.x <= self.x <= rec.upright.x \
            and rec.lowleft.y <= self.y <= rec.upright.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
        self.base = abs(self.lowleft.x - self.upright.x)
        self.heigh = abs(self.lowleft.y - self.upright.y)



class Area(Rectangle):
    def __init__(self, rec):
        super().__init__(rec.lowleft,rec.upright)
    
    def calculate_area(self):
        self.area = float(self.base * self.heigh)

    def show_area (self):
        return str(self.area)

    def guess_area(self, guess):
        self.calculate_area()
        if self.area == guess:
            return True
        else:
            return False
    
if __name__ == '__main__':

    rectangle = Rectangle(
        Point(random.randint(0,9), random.randint(0,9)),
        Point(random.randint(10,19), random.randint(10,19))
    )

    print('\nRectangle Coordinates: ',
        f'{rectangle.lowleft.x}, {rectangle.lowleft.y}',
        f'and {rectangle.upright.x}, {rectangle.upright.y}\n')

    user_point = Point(float(input('Guess point x coord: ')), float(input('Guess point y coord: ')))

    print(f'\nYour point was inside rectangle: {user_point.inside_rectangle(rectangle)}')


    user_area = Area(rectangle)
    guess = user_area.guess_area(float(input('Guess the rectangle area: ')))

    print(f'Your guessed area was right: {guess}')
    
    if guess == False:
        print(f'The right area is: {user_area.show_area()}')
