from kivy.uix.button import Button
from kivy.app import App
from functools import partial


"""El método siempre se llamará build, para que lo encuentre
la classe App, ademas nsiempre recibirá como herencia self, que  és 
la palabra reservada para acceder a sus atributos
class my_Button(App):
    def build(self):
        return Button(text = "Entrar", backgraund_color = (155,0,51,53))

my_Button().run()"""
class myButton(App):
    def disable(self, instance,*args):
        instance.disabled = True
    

    def update(self, instance, *args):
        instance.text = "Estoy deshabilitado"
        
    def build(self):
        mybtn = Button(text = "haaz clic para desactivarme", background_color = (155,0,51,53))
        mybtn.bind(on_press = partial(self.disable, mybtn))
        mybtn.bind(on_press = partial(self.update, mybtn))

        return mybtn
    
myButton().run()


    
