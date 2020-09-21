from kivy.app import App
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from store import cs, act
class __SimpleWidget(Screen):
    __widget__="SimpleWidget"
    # click = BooleanProperty(False)
    def change_screen(self, name):
        if self.parent:
            if self.parent.has_screen(name):
                self.parent.current = name

def mapper(st, wi):
    wi.click = st.get('hi')

def disp(dispatch, wi):
    return {
        'bind':{
            'on_pre_leave':lambda *largs, **kwargs:dispatch(act)
        },
        'init':{
            'click':False
        }
    }
SimpleWidget = cs.connect(mapper=mapper,dispatcher=disp, widget=__SimpleWidget)
def mapper_func(st, wi):
    wi.hi = st.get('hi')

def dispatcher_func(dis, wi):
    return {
        'bind':{
            'hi':lambda *largs, **kwargs: print(wi.hi)
        },
        'init':{
            'hi':True
        }
    }

def SimpleLabelFunc(*largs, **kwargs):
    component = Label(*largs, **kwargs)
    return component

SimpleLabelFunc= cs.connect(mapper_func, dispatcher_func, SimpleLabelFunc)

class SimpleScreen(ScreenManager):
    pass
class SimpleApp(App):
    def build(self):
        Factory.register('SimpleWidget', cls=SimpleWidget, )
        Factory.register('SimpleLabelFunc', cls=SimpleLabelFunc)
        s= SimpleScreen()
        return s