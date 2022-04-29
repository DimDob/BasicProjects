class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __setattr__(self, name, val):
         # self.name = val # В този случай __setattr__() започва да извиква себе си след всяка итерация, т.е. влиза в рекурсия. В този случай трябва да извикаме специалния метод от класа object.
        return object.__setattr__(self, name, val) #Трябва да извикваме метода __setattr__() от класа object, за да не се създава рекурсивно извикване, появяващо се при присвояване на стойност val на атрибута на обекта self.

p = Person(12, 'Dimithur')

print(p.name)
p.__setattr__('name', 'Ivan')

print(p.name)
setattr(p, 'name', 'Ivan')
print(p.name)