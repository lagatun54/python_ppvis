class GardenBed: # Сад, здесь просто список растений
    plants = []

    def display_garden(self):
        for i in self.plants:
            i.show_plant_status()


class Warehouse: # Склад, тут будем хранить кол-во всех растений
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
        print("Яблоки: " + str(self.contents[0]))
        print("Груши: " + str(self.contents[1]))
        print("Вишни: " + str(self.contents[2]))
        print("Сливы: " + str(self.contents[3]))
        print("Картофель: " + str(self.contents[4]))
        print("Морковь: " + str(self.contents[5]))
        print("Капуста: " + str(self.contents[6]))
        print("Перец: " + str(self.contents[7]))


class GameMaster: # Игрок, пока что тут ничего нет, ну и ладно
    field = GardenBed()
    storage = Warehouse()

    def add_plant(self, plant_name):
        self.field.plants.append(plant_name)

    def update_screen(self):
        print("ГРЯДКИ")
        self.field.display_garden()
        print("\nСКЛАД")
        self.storage.display_warehouse()


class Plant: # Базовый класс
    harvest_progress = 0
    harvest_max = 0
    name = 'Plant'
    mods = 0
    id = -1


class Tree(Plant): # Класс дерева
    growth_progress = 0
    growth_max = 0

    def show_plant_status(self):
        if self.growth_progress < self.growth_max:
            print(self.name + ": Рост дерева: " + str(self.growth_progress) + "/" + str(self.growth_max))
        else:
            print(self.name + ": Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
                  str(self.mods) + "%)")

    def age(self):
        if self.growth_progress < self.growth_max:
            self.growth_progress += 1
        else:
            if self.harvest_progress < self.harvest_max:
                self.harvest_progress += 1
            if self.harvest_progress == self.harvest_max:
                self.harvest_progress = 0
                player.storage.contents[self.id] += 1


class Vegetable(Plant): # Класс овощей
    def show_plant_status(self):
        print(self.name + ": Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (M " +
              str(self.mods) + "%)")

    def age(self):
        if self.harvest_progress < self.harvest_max:
            self.harvest_progress += 1
        if self.harvest_progress == self.harvest_max:
            self.harvest_progress = 0
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


def age_all():
    for x in GardenBed.plants:
        x.age()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    player = GameMaster()

    apple1 = Apple()
    plum1 = Plum()

    GameMaster.add_plant(player, apple1)
    GameMaster.add_plant(player, plum1)
    GameMaster.add_plant(player, Potato())

    while True:
        player.update_screen()
        age_all()
        if input() != '':
            exit()