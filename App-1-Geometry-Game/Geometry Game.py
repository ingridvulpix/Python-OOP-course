import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def inside_rectangle(self, rec):
        if rec.point_1.x <= self.x <= rec.point_2.x \
            and rec.point_1.y <= self.y <= rec.point_2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        self.base = abs(self.point_1.x - self.point_2.x)
        self.heigh = abs(self.point_1.y - self.point_2.y)



class Area(Rectangle):
    def __init__(self, rec):
        super().__init__(rec.point_1,rec.point_2)
    
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
        f'{rectangle.point_1.x}, {rectangle.point_1.y}',
        f'and {rectangle.point_2.x}, {rectangle.point_2.y}\n')

    user_point = Point(float(input('Guess point x coord: ')), float(input('Guess point y coord: ')))

    user_area = Area(rectangle)
    guess = user_area.guess_area(float(input('Guess the rectangle area: ')))

    print(f'\nYour point was inside rectangle: {user_point.inside_rectangle(rectangle)}')

    print(f'Your guessed area was right: {guess}')
    
    if guess == False:
        print(f'The right area is: {user_area.show_area()}')