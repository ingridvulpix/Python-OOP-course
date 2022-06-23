import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def inside_rectangle(self, rec):
        if rec.lowleft.x < self.x < rec.upright.x \
            and rec.lowleft.y < self.y < rec.upright.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    
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


