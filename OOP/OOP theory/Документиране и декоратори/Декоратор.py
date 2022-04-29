#Функция на декоратора:
def F(Alpha):
    class Bravo:
        value = Alpha()
    Bravo.__name__ = f"My{Alpha.__name__}"
    return Bravo
#Клас с декоратор
@F # == Charlie = F(Charlie)
class Charlie:
    def __init__(self):
        self.number = 123
    def show(self):
        print(f"Поле number: {self.number}")
#Създаване на обект:
obj = Charlie()
#Проверка на резултата:
obj.value.show()
print(f"Клас на обекта obj: {obj.__class__.__name__}")
print(f"Клас на полето value: {obj.value.__class__.__name__}")

#Чрез @F класът Charlie се предефинира (пренаписва). За основа се взема описанието на класа Charlie и с помощта на този клас се създава нов клас.
#ТОЙ СЕ СЪЗДАВА В СЪОТВЕТСТВИЕ С ИНСТРУКЦИЯТА F(Charlie). Референция към създадения клас се записва в идентификатора Charlie.
#На практика се изпълнява командата Charlie = F(Charlie). Затова ако по-рано референция към новия клас получавахме с инструкцията F(Charlie),
#то сега референция към новия клас дава инструкцията Charlie. Затова и командата на ред 18 дава, че класът на обекта obj е всъщност MyCharlie,
#а името на класа на полето value, когато бъде извикано - Charlie.
