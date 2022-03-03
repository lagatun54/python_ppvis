import random
import os


class GardenBed:  # Сад, здесь просто список растений
    plants = []

    def display_garden(self):
        for i in self.plants:
            i.show_plant_status()


class Warehouse:  # Склад, тут будем хранить кол-во всех растений
    contents = [0, 0, 0, 0, 0, 0, 0, 0]
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

    def update_screen(self):
        print("ГРЯДКИ")
        self.field.display_garden()
        print("\nСКЛАД")
        self.storage.display_warehouse()


class Plant:  # Базовый класс
    harvest_progress = 0
    harvest_max = 0
    name = 'Plant'
    mods: float = 1.0  # Шанс на то, что растение даст урожай
    is_droughted = False
    has_colorado_beatle = False
    id = None


class Tree(Plant):  # Класс дерева
    growth_progress = 0
    growth_max = 0

    def show_plant_status(self):
        for x in range(0, len(player.field.plants)):
            if player.field.plants[x] == self:
                print(str(x + 1) + ": ",  sep='', end='')

        if self.growth_progress < self.growth_max:
            print(self.name + ". Рост дерева: " + str(self.growth_progress) + "/" + str(self.growth_max))
        else:
            print(self.name + ". Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
                  str(self.mods * 100) + "%)")

    def age(self):
        if self.growth_progress < self.growth_max:
            self.growth_progress += 1
        else:
            if self.harvest_progress < self.harvest_max:
                self.harvest_progress += 1
            if self.harvest_progress == self.harvest_max:
                self.harvest_progress = 0
                if random.random() < self.mods:
                    player.storage.contents[self.id] += 1


class Vegetable(Plant):  # Класс овощей
    def show_plant_status(self):
        for x in range(0, len(player.field.plants)):
            if player.field.plants[x] == self:
                print(str(x + 1) + ": ", sep='', end='')
        print(self.name + ". Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
              str(self.mods * 100) + "%)")

    def age(self):
        if self.harvest_progress < self.harvest_max:
            self.harvest_progress += 1
        if self.harvest_progress == self.harvest_max:
            self.harvest_progress = 0
            if random.random() < self.mods:
                player.storage.contents[self.id] += 1


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


def age_all():  # Увеличивается процесс урожая ход
    for x in GardenBed.plants:
        x.age()


class Events:  # случайное событие, не зависящее от игрока
    drought = False
    colorado_attack = False

    def drought_start(self):  # бьёт по всем
        print("\nНачало засухи!")
        self.drought = True
        for x in player.field.plants:
            if x.mods > 0.5:
                x.mods -= 0.5
                round(x.mods, 2)
                x.is_droughted = True
            else:
                x.mods = 0

    def drought_end(self):  # бьёт по всем
        self.drought = False
        print("\nКонец засухи!")
        for x in player.field.plants:
            if x.is_droughted == True:
                x.mods += 0.5
                round(x.mods, 2)
                x.is_droughted = False

    def colorado_beatle_start(self):  # бьёт по картошке
        self.colorado_attack = True
        print("\nТревога! Атака колорадских жуков!")
        for x in player.field.plants:
            if x.id == 4 and x.mods > 0.3 and not x.has_colorado_beatle:
                x.mods -= 0.3
                round(x.mods, 2)
                x.has_colorado_beatle = True
            elif x.id == 4 and x.mods <= 0.3 and not x.has_colorado_beatle:
                x.mods = 0

    def colorado_beatle_end(self):
        self.colorado_attack = False
        print("\nКолорадские жуки отступают")
        for x in player.field.plants:
            if x.id == 4 and x.has_colorado_beatle:
                x.mods += 0.3
                round(x.mods, 2)
                x.has_colorado_beatle = False
                if x.mods > 1.0:
                    x.mods = 1.0


    def muchnaya_rosa_start(self): # бьёт по деревьям
        pass

    def start_disasters(self):
        if random.random() < 0.15 and not event.drought:
            Events.drought_start(event)
        else:
            if random.random() < 0.05 and event.drought:
                Events.drought_end(event)

        if random.random() < 0.25 and not event.colorado_attack:
            Events.colorado_beatle_start(event)
        else:
            if random.random() < 0.20 and event.colorado_attack:
                Events.colorado_beatle_end(event)



def watering():
    number = int(input("Введите номер грядки: ")) - 1
    if player.field.plants[number].is_droughted:
        player.field.plants[number].is_droughted = False
        player.field.plants[number].mods += 0.5
        round(player.field.plants[number].mods, 2)
        if player.field.plants[number].mods > 1.0:
            player.field.plants[number].mods = 1.0

def planting():
    number = int(input("Введите номер растения, которое хотите высадить:\n1 - яблоня\n2 - груша"
                       "\n3 - вишня\n4 - слива\n5 - картофель\n6 - морковь\n7 - капуста\n8 - перец\n\n")) - 1
    GameMaster.add_plant_based_on_id(player, number)


if __name__ == '__main__':
    player = GameMaster()
    event = Events()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        player.update_screen()
        event.start_disasters()
        print("\n\n\n1 - высадка растений\n2 - поливка растений\n3 - прополка грядок")
        step = input()
        match step:
            case '':
                age_all()
            case '1':
                planting()
                age_all()
            case '2':
                watering()
                age_all()
            case _:
                exit()

# прополка

# события это класс, в котором есть флажки и методы
# методы понижают модификатор каждого растения
# события имеют рандомную продолжительность, после которой они заканчиваются и модификаторы возвращаются в норму
# поливать можно отдельные грядки, это снимет их флажок и восстановит модификатор
# по завершению события метод проходит по всем растениям и повышает модификатор у тех, у кого остался флажок
