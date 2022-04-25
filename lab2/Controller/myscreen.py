from View.myscreen import MyScreenView


class MyScreenController:
    _observers = []

    def __init__(self, model):
        self.model = model
        self.view = MyScreenView(controller=self, model=self.model)
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, data):
        for x in self._observers:
            x.model_is_changed(data)

    def refresh(self):
        self.model.refresh_stock_in_table()

    def get_screen(self):
        return self.view.build()

    def input_stock(self, data):
        self.model.add_new_stock(row=data)

    def dialog(self, mode, dialog):
        self.open_dialog(mode, dialog)

    def get_degrees(self):
        return self.model.get_all_degrees()

    def filter_stock(self, data):
        self.model.filter_stock_in_table(filters=data)

    def delete_stock(self, data):
        delete_list = self.model.delete_stock_from_table(filters=data)
        return delete_list

    def upload_from_file(self, file_name):
        self.model.read_from_file(file_name)

    def save_in_file(self, file_name):
        self.model.write_to_file(file_name)

    def open_dialog(self, dialog, mode):
        self.dialog_ = dialog

    def close_dialog(self, dialog_data: list = []):
        data = dialog_data
        self.model.notify_observers(data)
        self.dialog_ = None
