from kivy.app import App
from kivy.uix.label import Label


class kivy_saludo(App):
    def build(self):

        return Label(text = "Hola Mundo")
    
kivy_saludo().run()