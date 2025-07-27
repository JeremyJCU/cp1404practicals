from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):

    def build(self):
        """Build Kivy GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    #Part 4 5
    def handle_greet(self):
        """Prints a greeting to name entered into the GUI"""
        print("Greet!")
        #Part 7 & 9
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    #Part 9
    def handle_clear(self):
        """Clear input field and output field"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""

BoxLayoutDemo().run()
