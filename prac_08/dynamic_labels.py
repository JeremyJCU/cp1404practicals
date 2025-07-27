"""
CP1404 Practical
Dynamic Kivy Widgets
Dynamic Labels
Jeremy Wiseman
Started 27/07/2025
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import StringProperty

class DynamicLabelApp(App):
    #Observer pattern
    label_text = StringProperty()

    def __init__(self, **kwargs):
        """Model created for dynamic labels"""
        #Don't know what this is doing
        super().__init__(**kwargs)
        #List of label names
        self.usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                     'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                     'bob']

    def build(self):
        """Build Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create Kivy dynamic label widgets"""
        for label in self.usernames:
            text_label = Label(text=label)
            self.root.ids.main.add_widget(text_label)



DynamicLabelApp().run()