import datetime
from kivy.storage.jsonstore import JsonStore
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage

from KivyCalendar import DatePicker
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.checkbox import CheckBox
# from kivy.uix.togglebutton import ToggleButton
# from kivy.uix.button import Button


class DermRoot(BoxLayout):
    dict_filled_from_form = {}

    def add_entry_to_db(self,dict_filled_from_form):
        store = JsonStore('helishit.json')
        store.put('')

class DemographForm(BoxLayout):
    __events__ = ('on_save', )

    def on_save(self, data):
        pass

    data = DictProperty({})
    sex = ObjectProperty()
    age_input = ObjectProperty()

    def handle_checkbox(self, checkbox):
        if checkbox not in self.data:
            self.data[checkbox] = True
        elif self.data[checkbox]:
            self.data[checkbox] = False
        else:
            self.data[checkbox] = True

    def edit(self, data=None):
        if data is not None:
            self.data = data
        else:
            self.data = {}  # reset the for

    def Picker(self):
        self.laDate = self.datepicker.text
        self.datepicked = datetime.datetime.strptime(self.laDate, '%d.%m.%Y').strftime('%d/%m/%Y')
        self.myLabel.text = str(self.datepicked)


    class ShowcaseScreen(BoxLayout):
        pass

class DermApp(App):
    pass

if __name__ == '__main__':
    DermApp().run()