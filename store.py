from kivyredux.store import Store
from kivyredux.actions import Action
from kivyredux.state import State
from kivyredux.reducers import Reducer

s = State(hi=False)
def red(action, state=s):
    if action.type == "hi":
        state.update('hi', not state.get('hi'))
    else:
        pass
    return state

r = Reducer(id='btn', reducer_cb=red)

act = Action(action_type="hi")

cs = Store(reducers=[r], state=s)