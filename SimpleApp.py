from kivy.app import App, Widget
import kivy.properties as properties
class SimpleWidget(Widget):
    name = properties.StringProperty("Test")
    name_2 = properties.StringProperty("Test 2")
    
class SimpleApp(App):

    def build(self):
        return SimpleWidget()