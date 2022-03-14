from .warehouse import Warehouse
from .gardenbed import GardenBed
import numpy as np
import random
import json


class GameMaster(Warehouse, GardenBed):
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

    def import_plants(self):
        with open(r'D:\Projects\2course\ppvis\sem2\laba1\lab1\field.json', 'r', encoding='utf-8') as f:
            house1 = json.loads(f.read())
            self.field.plants.clear()
            for i in range(0, len(house1)):
                current_plant: dict = house1.get(str(i))
                self.add_plant_based_on_id(i)
                self.field.plants[i].mods = current_plant.get("mods")
                self.field.plants[i].harvest_progress = current_plant.get("harvest_progress")
                self.field.plants[i].growth_progress = current_plant.get("growth_progress")
                self.field.plants[i].id = current_plant.get("id")
                self.field.plants[i].is_droughted = current_plant.get("is_droughted")
                self.field.plants[i].weeded = current_plant.get("weeded")
                self.field.plants[i].diseases = current_plant.get("diseases")
                self.field.plants[i].has_colorado_beatle = current_plant.get("has_colorado_beatle")


class Plant:  # Базовый класс
        harvest_progress: int = 0
        harvest_max: int = 0
        name: 'Plant'
        mods:  float = 1.0  # Шанс на то, что растение даст урожай
        is_droughted:  bool = False
        has_colorado_beatle: bool = False
        diseases: bool = False
        weeded: bool = False
        id: None
        plods: str ='Plods'


class Tree(Plant, GameMaster):  # Класс дерева
    growth_progress = 0
    growth_max = 0

    def show_plant_status(self, target: GameMaster):
        for x in range(0, len(target.field.plants)):
            if target.field.plants[x] == self:
                print("\n" + str(x + 1) + ": ", sep='', end='')

        if self.growth_progress < self.growth_max:
            print(self.name , ". Рост дерева: " + str(self.growth_progress) + "/" + str(self.growth_max), sep='',
                  end='')
        else:
            print(self.name, ". Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
                  str(self.mods * 100) + "%)", sep='', end='')
        if self.weeded:
            print(" | ЗАХВАЧЕНО СОРНЯКАМИ", sep='', end='')

    def age(self, target: GameMaster):
        if self.growth_progress < self.growth_max:
            self.growth_progress += 1
        else:
            if self.growth_progress < self.growth_max:
                self.growth_progress += 1
            else:
                if self.harvest_progress < self.harvest_max:
                    self.harvest_progress += 1
                if self.harvest_progress == self.harvest_max:
                    self.harvest_progress = 0
                    if random.random() < self.mods:
                        target.storage.house[self.plods] += 1


class Vegetable(Plant, GameMaster):  # Класс овощей
    def show_plant_status(self, target: GameMaster):
        for x in range(0, len(target.field.plants)):
            if target.field.plants[x] == self:
                print("\n" + str(x + 1) + ": ", sep='', end='')
        print(self.name , ". Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
              str(self.mods * 100) + "%)", sep='', end='')
        if self.weeded:
            print(" | ЗАХВАЧЕНО СОРНЯКАМИ", sep='', end='')

    def age(self, target: GameMaster):
        if self.harvest_progress < self.harvest_max:
            self.harvest_progress += 1
        if self.harvest_progress == self.harvest_max:
            self.harvest_progress = 0
            if random.random() < self.mods:
                target.storage.house[self.plods] += 1


# FRUIT TREES


class Apple(Tree):
    harvest_max = 3
    growth_max = 5
    name = 'Яблоня'
    plods = "Яблоки"
    id = 0


class Pear(Tree):
    harvest_max = 3
    growth_max = 6
    name = 'Груша'
    plods = 'Груши'
    id = 1


class Cherry(Tree):
    harvest_max = 2
    growth_max = 6
    name = 'Вишня'
    plods = 'Вишни'
    id = 2


class Plum(Tree):
    harvest_max = 2
    growth_max = 5
    name = 'Слива'
    plods = 'Сливы'
    id = 3


# VEGETABLES


class Potato(Vegetable):
    harvest_max = 2
    name = 'Картофель'
    plods = 'Картофель'
    id = 4


class Carrot(Vegetable):
    harvest_max = 3
    name = 'Морковь'
    plods = 'Морковь'
    id = 5


class Cabbage(Vegetable):
    harvest_max = 2
    name = 'Капуста'
    plods = 'Капуста'
    id = 6


class Pepper(Vegetable):
    harvest_max = 3
    name = 'Перец'
    plods = 'Перец'
    id = 7