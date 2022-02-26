class Garden_bed: # Сад, здесь просто список растений
    plants = []

    def display_garden(self):
        for i in self.plants:
            i.show_plant_status()


class Warehouse: # Склад, тут будем хранить кол-во всех растений
    apples = 0
    pears = 0
    cherries = 0
    plums = 0
    potatoes = 0
    carrots = 0
    cabbage = 0
    pepper = 0

    def display_warehouse(self):
        print("Яблоки: " + str(self.apples))
        print("Груши: " + str(self.pears))
        print("Вишни: " + str(self.cherries))
        print("Сливы: " + str(self.plums))
        print("Картофель: " + str(self.potatoes))
        print("Морковь: " + str(self.carrots))
        print("Капуста: " + str(self.cabbage))
        print("Перец: " + str(self.pepper))


class Game_master: # Игрок, пока что тут ничего нет, ну и ладно
    field = Garden_bed()

    def add_plant(self, plant_name):
        self.field.plants.append(plant_name)

    def update_screen(self):
        self.field.display_garden()


class Plant: # Базовый класс
    harvest_progress = 0
    harvest_max = 0
    name = 'Plant'
    mods = 0


class Tree(Plant): # Класс дерева
    growth_progress = 0
    growth_max = 0

    def show_plant_status(self):
        if self.growth_progress < self.growth_max:
            print(self.name + ": Рост дерева: " + str(self.growth_progress) + "/" + str(self.growth_max))
        else:
            print(self.name + ": Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (" +
                  str(self.mods) + "%)")


class Vegetable(Plant): # Класс овощей
    def show_plant_status(self):
        print(self.name + ": Урожай: " + str(self.harvest_progress) + "/" + str(self.harvest_max) + " (" +
              str(self.mods) + "%)")

# FRUIT TREES


class Apple(Tree):
    harvest_max = 3
    growth_max = 5
    name = 'Яблоня'


class Pear(Tree):
    harvest_max = 3
    growth_max = 6
    name = 'Груша'


class Cherry(Tree):
    harvest_max = 2
    growth_max = 6
    name = 'Вишня'


class Plum(Tree):
    harvest_max = 2
    growth_max = 5
    name = 'Слива'

# VEGETABLES


class Potato(Vegetable):
    harvest_max = 2
    name = 'Картофель'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    player = Game_master()

    apple1 = Apple()
    plum1 = Plum()


    Game_master.add_plant(player, apple1)
    Game_master.add_plant(player, plum1)
    Game_master.add_plant(player, Potato())

    player.update_screen()