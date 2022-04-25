from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from Controller.myscreen import MyScreenController
from Model.myscreen import MyScreenModel
from kivy.core.window import Window
from kivy.metrics import dp


class PassMVC(MDApp):
    def __init__(self):
        super().__init__()
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            size_hint=(0.7, 0.65),
            use_pagination=True,
            elevation=2,
            rows_num=4,
            pagination_menu_height=120,
            background_color=(0, 1, 0, .10),
            column_data=[
                ("[color=#123487]Product Name[/color]", dp(40)),
                ("[color=#123487]Manufacturer's name[/color]", dp(40)),
                ("[color=#123487]Manufacturer's UNP[/color]", dp(40)),
                ("[color=#123487]Quantity in stock[/color]", dp(40)),
                ("[color=#123487]Warehouse address[/color]", dp(40)),
            ],
        )
        self.model = MyScreenModel(table=self.table)
        self.controller = MyScreenController(self.model)

    def build(self):
        Window.size = (640, 480)
        return self.controller.get_screen()


PassMVC().run()
