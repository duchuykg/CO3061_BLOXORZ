import time
from ultis import *

"""class Node:
    def __init__(self, data=(0, 0, 0, 0), prev_node=None, map=[], xo_objects_states={}, is_splitted=False):
        if not ((data[0] < data[2]) or ((data[0] == data[2]) and data[1] < data[3])):
            temp_data = (data[2], data[3], data[0], data[1])
            self.data = temp_data
        else:
            self.data = data
        self.prev_node = prev_node
        self.map = map_copy(map)
        self.xo_objects_states = dict(xo_objects_states)
        self.is_splitted = is_splitted

    def is_stand(self):
        return self.data[0] == self.data[2] and self.data[1] == self.data[3]"""
# from index import State

def dfs(state):
    # start = time.time()
    current_state = Node
    # BFS operation
    start = time.time()
    while len(state.states) != 0:
        # if time.time() - start > 15:
        #     break
        current_state = state.states.pop(0)
        state.set_player_position(current_state)
        if state.check_goal():
            break
        state.add_valid_state(current_state, -120)
    pointer = current_state
    path = []
    # Backtracking all the previous moves to reach this goal state
    while pointer:
        path.insert(0, pointer)
        pointer = pointer.prev_node
    # And print them out
    # for p in path:
    #     print(p.data)
    return path