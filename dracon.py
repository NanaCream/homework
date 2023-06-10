
class Dragon():
    def __init__(self, height, fire_resist, color):
        self.height = height
        self.fire_resist = fire_resist
        self.color = color
    def __eq__(self, other):
        if (self.height == other.height) and (self.fire_resist == other.fire_resist) and (self.color == other.color):
            return True
        else:
            return False
    def __add__(self, other):
        import math
        color2 = min(self.color, other.color)
        height2 = math.floor((self.height + other.height)/2)
        fire_resist2 = max(self.fire_resist, other.fire_resist)
        dr2 = Dragon(height2, fire_resist2, color2)
        return(dr2)
    def __repr__(self) -> str:
        return f'Dragon {self.height}, {self.fire_resist}, {self. color} '
    def str(self):
        return f'Dragon with height {self.height}, danger {self.fire_resist} and color {self.color}'
    def change_color(self):
        new_color = input('Введите новый цвет: ')
        self.color = new_color
        return self
    def __sub__(self, number):
        number = int(input('Введите число: '))
        self.height = self.height - int(self.height / number)
        self.fire_resist = self.fire_resist + self.fire_resist % number
        return self
    def str1(self):
        string = input('Введите строку: ')
        print(string * self.fire_resist)
    
dr = Dragon(69, 5, 'brown')
dr1 = Dragon(69, 5, 'gray')


