"""
CP1404 Practical
Miles to Kilometers Converter
Jeremy Wiseman
Started 27/07/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETERS = 1.60934
INCREASE_UP = 1
INCREASE_DOWN = -1


class ConvertMiles(App):
    #Observer patten GUI value
    converted_distance = StringProperty("54.71756")

    def build(self):
        """Create Kivy input application form for converting miles to kilometers."""
        self.title = 'Convert miles to kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """Carry out miles to kilometers conversion and display on Kivy GUI."""
        self.converted_distance = str(self.get_valid_float(self.root.ids.input_miles.text) * MILES_TO_KILOMETERS)

    def handle_kilometer_change(self, is_up):
        """Increase or decrease miles to kilometers conversion by INCREASE_UP/DOWN value."""
        if is_up:
            self.root.ids.input_miles.text = str(self.get_valid_float(self.root.ids.input_miles.text) + INCREASE_UP)
        else:
            self.root.ids.input_miles.text = str(self.get_valid_float(self.root.ids.input_miles.text) + INCREASE_DOWN)
        self.handle_calculation()

    def get_valid_float(self, field_input):
        """Convert a string to float value or return a 0.0 value."""
        try:
            number = float(field_input)
        except ValueError:
            return 0.0
        return number


ConvertMiles().run()
