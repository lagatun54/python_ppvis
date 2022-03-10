import random
import os
import numpy as np


class GardenBed:  # Сад, здесь просто список растений
    plants = []


class Warehouse:  # Склад, тут будем хранить кол-во всех растений
    contents = [0, 0, 0, 0, 0, 0, 0, 0]
    namelist = ["яблони", "груши", "вишни", "сливы", "картофель", "морковь", "капуста", "перец"]
    """
    apples
    pears
    cherries
    plums
    potatoes
    carrots
    cabbage
    pepper
    """

    def display_warehouse(self):
        if self.contents[0] > 0:
            print("Яблоки: " + str(self.contents[0]))
        if self.contents[1] > 0:
            print("Груши: " + str(self.contents[1]))
        if self.contents[2] > 0:
            print("Вишни: " + str(self.contents[2]))
        if self.contents[3] > 0:
            print("Сливы: " + str(self.contents[3]))
        if self.contents[4] > 0:
            print("Картофель: " + str(self.contents[4]))
        if self.contents[5] > 0:
            print("Морковь: " + str(self.contents[5]))
        if self.contents[6] > 0:
            print("Капуста: " + str(self.contents[6]))
        if self.contents[7] > 0:
            print("Перец: " + str(self.contents[7]))


class GameMaster:
    field = GardenBed()
    storage = Warehouse()

    def watering(self):
        number = int(input("Введите номер грядки: ")) - 1
        if number > len(self.field.plants) or number < 0:
            return
        if self.field.plants[number].is_droughted:
            self.field.plants[number].is_droughted = False
            self.field.plants[number].mods += 0.5
            self.field.plants[number].mods = np.around(self.field.plants[number].mods, 3)
        if self.field.plants[number].mods > 1.0:
            self.field.plants[number].mods = 1.0

    def age_all(self):  # Увеличивается процесс урожая ход
        for x in self.field.plants:
            x.age(self)

    def add_plant(self, plant_name):
        self.field.plants.append(plant_name)

    def add_plant_based_on_id(self, id_name):
        match id_name:
            case 0:
                self.add_plant(Apple())
            case 1:
                self.add_plant(Pear())
            case 2:
                self.add_plant(Cherry())
            case 3:
                self.add_plant(Plum())
            case 4:
                self.add_plant(Potato())
            case 5:
                self.add_plant(Carrot())
            case 6:
                self.add_plant(Cabbage())
            case 7:
                self.add_plant(Pepper())

    def display_garden(self):
        for i in self.field.plants:
            i.show_plant_status(self)

    def planting(self):
        number = int(input("Введите номер растения, которое хотите высадить:\n1 - яблоня\n2 - груша"
                       "\n3 - вишня\n4 - слива\n5 - картофель\n6 - морковь\n7 - капуста\n8 - перец\n\n")) - 1
        if number > 7 or number < 0:
           return
        #exception
        else:
            self.add_plant_based_on_id(number)

    def weeding(self):
        number = int(input("Введите номер грядки, которую хотите прополоть: ")) - 1
        if number > len(self.field.plants) or number < 0:
            return
        self.field.plants[number].weeded = False
        self.field.plants[number].mods += 0.2
        self.field.plants[number].mods = np.around(self.field.plants[number].mods, 3)
        if self.field.plants[number].mods >= 1.0:
            self.field.plants[number].mods = 1.0

    def update_screen(self):
        print("ГРЯДКИ")
        self.display_garden()
        print("\n\nСКЛАД")
        self.storage.display_warehouse()
        print()


class Plant:  # Базовый класс
    harvest_progress = 0
    harvest_max = 0
    name = 'Plant'
    mods: float = 1.0  # Шанс на то, что растение даст урожай
    is_droughted = False
    has_colorado_beatle = False
    diseases = False
    weeded = False
    id = None


class Tree(Plant):  # Класс дерева
    growth_progress = 0
    growth_max = 0

    def show_plant_status(self, target: GameMaster):
        for x in range(0, len(target.field.plants)):
            if target.field.plants[x] == self:
                print("\n" + str(x + 1) + ": ",  sep='', end='')

        if self.growth_progress < self.growth_max:
            print(self.name + ". Рост дерева: " + str(self.growth_progress) + "/" + str(self.growth_max), sep='',
                  end='')
        else:
            print(self.name + ". Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
                  str(self.mods * 100) + "%)", sep='', end='')
        if self.weeded:
            print(" | ЗАХВАЧЕНО СОРНЯКАМИ", sep='', end='')

    def age(self, target: GameMaster):
        if self.growth_progress < self.growth_max:
            self.growth_progress += 1
        else:
            if self.harvest_progress < self.harvest_max:
                self.harvest_progress += 1
            if self.harvest_progress == self.harvest_max:
                self.harvest_progress = 0
                if random.random() < self.mods:
                    target.storage.contents[self.id] += 1


class Vegetable(Plant):  # Класс овощей
    def show_plant_status(self, target: GameMaster):
        for x in range(0, len(target.field.plants)):
            if target.field.plants[x] == self:
                print("\n" + str(x + 1) + ": ", sep='', end='')
        print(self.name + ". Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
              str(self.mods * 100) + "%)", sep='', end='')
        if self.weeded:
            print(" | ЗАХВАЧЕНО СОРНЯКАМИ", sep='', end='')

    def age(self, target: GameMaster):
        if self.harvest_progress < self.harvest_max:
            self.harvest_progress += 1
        if self.harvest_progress == self.harvest_max:
            self.harvest_progress = 0
            if random.random() < self.mods:
                target.storage.contents[self.id] += 1


# FRUIT TREES


class Apple(Tree):
    harvest_max = 3
    growth_max = 5
    name = 'Яблоня'
    id = 0


class Pear(Tree):
    harvest_max = 3
    growth_max = 6
    name = 'Груша'
    id = 1


class Cherry(Tree):
    harvest_max = 2
    growth_max = 6
    name = 'Вишня'
    id = 2


class Plum(Tree):
    harvest_max = 2
    growth_max = 5
    name = 'Слива'
    id = 3


# VEGETABLES


class Potato(Vegetable):
    harvest_max = 2
    name = 'Картофель'
    id = 4


class Carrot(Vegetable):
    harvest_max = 3
    name = 'Морковь'
    id = 5


class Cabbage(Vegetable):
    harvest_max = 2
    name = 'Капуста'
    id = 6


class Pepper(Vegetable):
    harvest_max = 3
    name = 'Перец'
    id = 7


class Events:  # случайное событие, не зависящее от игрока
    drought = False
    colorado_attack = False
    illness = False
    rainy = False
    idDisease = -1

    @staticmethod
    def drought_start(target: GameMaster):  # бьёт по всем
        print("Начало засухи!")
        Events.drought = True
        for x in target.field.plants:
            if x.mods > 0.5:
                x.mods -= 0.5
                x.mods = np.around(x.mods, 2)
                x.is_droughted = True
            else:
                x.mods = 0.0

    @staticmethod
    def drought_end(target: GameMaster):  # бьёт по всем
        Events.drought = False
        print("Конец засухи!")
        for x in target.field.plants:
            if x.is_droughted:
                x.mods += 0.5
                x.mods = np.around(x.mods, 3)
                x.is_droughted = False

    @staticmethod
    def colorado_beatle_start(target: GameMaster):  # бьёт по картошке
        Events.colorado_attack = True
        print("Тревога! Атака колорадских жуков!")
        for x in target.field.plants:
            if x.id == 4 and x.mods > 0.3 and not x.has_colorado_beatle:
                x.mods -= 0.3
                x.mods = np.around(x.mods, 2)
                x.has_colorado_beatle = True
            elif x.id == 4 and x.mods <= 0.3 and not x.has_colorado_beatle:
                x.mods = 0.0
                x.has_colorado_beatle = True

    @staticmethod
    def colorado_beatle_end(target: GameMaster):
        Events.colorado_attack = False
        print("Колорадские жуки отступают")
        for x in target.field.plants:
            if x.id == 4 and x.has_colorado_beatle:
                x.mods += 0.3
                x.mods = np.around(x.mods, 3)
                x.has_colorado_beatle = False
                if x.mods > 1.0:
                    x.mods = 1.0

    @staticmethod
    def rain_start(target: GameMaster):
        print("Пошёл дождь.")
        Events.rainy = True
        for x in target.field.plants:
            x.mods += 0.05
            x.mods = np.around(x.mods, 3)

    @staticmethod
    def rain_end(target: GameMaster):
        print("Конец дождя.")
        Events.rainy = False
        for x in target.field.plants:
            x.mods -= 0.05
            x.mods = np.around(x.mods, 3)

    # def disease_start():
    #     illness = True
    #     disease = random.randint(0, 7)
    #     idDisease = disease
    #     print("Болезнь пришла по " + player.storage.namelist[idDisease])
    #     for x in player.field.plants:
    #         if x.id == disease:
    #             x.mods -= 0.15
    #             if x.mods < 0:
    #                 x.mods = 0.0
    #             x.mods = np.around(x.mods, 3)
    #             x.diseases = True
    #         elif x.id == idDisease and x.diseases:
    #             x.mods += 0.15
    #             x.mods = np.around(x.mods, 3)
    #             x.diseases = False
    #             print("Болезнь вида " + player.storage.namelist[idDisease] + " закончилась")

    @staticmethod
    def weed_infestation(target: GameMaster):
        weed_place = random.randint(0, len(target.field.plants) - 1)
        if target.field.plants[weed_place].weeded:
            return
        target.field.plants[weed_place].weeded = True
        print(target.field.plants[weed_place].name + " под номером " + str(weed_place + 1) +
              " подвергается атаке сорняков")
        if target.field.plants[weed_place].mods >= 0.2:
            target.field.plants[weed_place].mods -= 0.2
            target.field.plants[weed_place].mods = np.around(target.field.plants[weed_place].mods, 3)
        else:
            target.field.plants[weed_place].mods = 0.0

    @staticmethod
    def start_disasters(target: GameMaster):
        if len(target.field.plants) == 0:
            return
        if random.random() < 0.15 and not Events.drought and not Events.rainy:
            Events.drought_start(target)
        elif random.random() < 0.05 and Events.drought:
            Events.drought_end(target)
        if random.random() < 0.30 and not Events.rainy:
            Events.rain_start(target)
            if Events.drought:
                Events.drought_end(target)
        elif random.random() < 0.30 and Events.rainy:
            Events.rain_end(target)
        if random.random() < 0.25 and not Events.colorado_attack:
            Events.colorado_beatle_start(target)
        elif random.random() < 0.20 and Events.colorado_attack:
            Events.colorado_beatle_end(target)
        # if random.random() < 0.15 and not Events.illness:
        #     Events.disease_start()
        # elif random.random() < 0.15 and Events.illness:
        #     Events.disease_end()
        chance = random.random()
        if (chance < 0.35 and not Events.rainy) or (chance < 0.55 and Events.rainy):
            Events.weed_infestation(target)


if __name__ == '__main__':
    player = GameMaster()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        player.update_screen()
        Events.start_disasters(player)
        print("\n\n\n1 - высадка растений\n2 - поливка растений\n3 - прополка грядок")
        step = input()
        match step:
            case '':
                player.age_all()
            case '1':
                player.planting()
                player.age_all()
            case '2':
                player.watering()
                player.age_all()
            case '3':
                player.weeding()
                player.age_all()
            case _:
                exit()

# прополка

# события это класс, в котором есть флажки и методы
# методы понижают модификатор каждого растения
# события имеют рандомную продолжительность, после которой они заканчиваются и модификаторы возвращаются в норму
# поливать можно отдельные грядки, это снимет их флажок и восстановит модификатор
# по завершению события метод проходит по всем растениям и повышает модификатор у тех, у кого остался флажок


"""
Статика существует не в контексте объекта, а в контексте класса! 
Из этого вытекает то, что на протяжении всего жизненного цикла вашего кода 
будет существовать лишь одно глобальное состояние статических членов класса.

Использовать статику нужно в случае, если то, что вы ей описываете принадлежит 
всей группе объектов, а не одному. Например, у класса Human может быть статический 
метод numberOfLegs(), который возвращает количество ног у людей. Количество ног - 
это общее свойство для всех людей (Речь идет о здоровых людях). В данном случае 
можно было использовать константу класса, но это не так важно, ведь, по сути, 
константа - это тоже статический контекст. А вот имя - это уже свойство каждого 
отдельного человека. 
"""