from kivy.app import App
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import BooleanProperty
from store import cs, act
class __SimpleWidget(Screen):
    __widget__="SimpleWidget"
    click = BooleanProperty(False)
    def change_screen(self, name):
        if self.parent:
            if self.parent.has_screen(name):
                self.parent.current = name

def mapper(st, wi):
    wi.click = st.get('hi')
    print(st.get('hi'), wi)

def disp(dispatch, wi):
    return {
        'bind':{
            'on_pre_leave':lambda *largs, **kwargs:dispatch(act)
        },
        'init':{
            's':True
        }
    }
SimpleWidget = cs.connect(mapper=mapper,dispatcher=disp, widget=__SimpleWidget)
class SimpleScreen(ScreenManager):
    pass
class SimpleApp(App):
    def build(self):
        Factory.register('SimpleWidget', cls=SimpleWidget, )
        s= SimpleScreen()
        return s