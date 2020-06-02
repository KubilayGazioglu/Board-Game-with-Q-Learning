import numpy as np
import pickle
from Board import *

HEIGHT = 7
WIDTH = 7
class Agent:
    def __init__(self, name, exp_rate=0.3):
        self.states = []
        self.lr = 0.2
        self.exp_rate = exp_rate
        self.decay_gamma = 0.9
        self.states_value = {}
        self.name = name

    def choose_action(self, positions,current_board,symbol):
        if np.random.uniform(0, 1) <= self.exp_rate:
            # take random action
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            for p in positions:
                next_board = current_board.copy()
                next_board[p] = symbol
                next_board_hash = self.get_hash(next_board)
                value = 0 if self.states_value.get(next_board_hash) is None else self.states_value.get(next_board_hash)
                if value >= value_max:
                    value_max = value
                    action = p
        return action

    def feed_reward(self, reward):
        for st in reversed(self.states):
            if self.states_value.get(st) is None:
                self.states_value[st] = 0
            self.states_value[st] += self.lr * (self.decay_gamma * reward - self.states_value[st])
            reward = self.states_value[st]

    def reset(self):
        self.states = []

    # append a hash state
    def add_state(self, state):
        self.states.append(state)

    # hash state
    def get_hash(self, board):
        board_hash = str(board.reshape(HEIGHT * WIDTH))
        return board_hash

    def save_policy(self):
        fw = open('for_' + str(self.name), 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    def load_policy(self, file):
        fr = open(file, 'rb')
        self.states_value = pickle.load(fr)
        fr.close()





