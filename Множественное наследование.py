class Horse:
    def __init__(self):
        self.x_distance = 0 #пройденный путь
        self.sound = 'Frrr' #звук, который издаёт лошадь
        super().__init__()

    #Метод "run" увеличивает x_distance на dx(изменение дистанции)
    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0 #высота полёта
        self.sound = 'I train, eat, sleep, and repeat' #звук, который издаёт орёл

    # Метод "fly" увеличивает y_distance на dy(изменение дистанции)
    def fly(self, dy):
        self.y_distance += dy


'''Pegasus - класс описывающий пегаса. Наследуется от 
Horse и Eagle в том же порядке'''
class Pegasus(Horse, Eagle):
    '''Объект такого класса должен обладать атрибутами
    классов родителей в порядке наследования.'''
    def __init__(self):
        super().__init__()

    def move(self, dx, dy): #dx и dy изменения дистанции
        '''В этом методе должны запускаться наследованные
        методы run и fly соответственно'''
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
print(Pegasus.mro())




