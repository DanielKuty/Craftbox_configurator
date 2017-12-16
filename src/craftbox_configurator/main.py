from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from passlib.utils import pbkdf2
from kivy.uix.image import Image
import binascii
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        def generate_psk(instance):
            passphrase = str(instance.parent.passphrase.text)
            ssid = str(instance.parent.ssid.text)
            encoded = pbkdf2.pbkdf2(str.encode(passphrase), str.encode(ssid), 4096, 32)
            instance.parent.psk.text = binascii.hexlify(encoded).decode("utf-8")
        self.cols = 4
        self.row_force_default = True
        self.row_default_height = 40
        self.add_widget(Label(text='SSID'))
        self.ssid = TextInput(multiline=False)
        self.add_widget(self.ssid)
        self.add_widget(Label(text='passphrase'))
        self.passphrase = TextInput(password=True, multiline=False)
        self.add_widget(self.passphrase)
        self.add_widget(Label(text="PSK"))
        self.psk = TextInput(multiline=False)
        self.add_widget(self.psk)
        self.button = Button(text="Configure", font_size=15)
        self.button.bind(on_press=generate_psk)
        self.add_widget(self.button)
        
        # wimg = Image(source='mylogo.png')
class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()



