import os
import sys
import time

from valley import *


if __name__ == '__main__':
    default_settings = ''
    if len(sys.argv) != 1:
        default_settings = str(sys.argv[1])

    player = GameMaster()

    if default_settings != "new":
        player.import_plants()
        player.storage.import_warehouse()
    else:
        player.storage.nullify_warehouse()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        player.update_screen()
        Events.start_disasters(player)
        print("\n\n\n1 - высадка растений\n2 - поливка растений\n3 - прополка грядок\n9 - снести поле комбайном")
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
            case '9':
                player.storage.nullify_warehouse()
                player.nullify_field()
                player.age_all()
            case _:
                print("\n\nВыходим из программы!")
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