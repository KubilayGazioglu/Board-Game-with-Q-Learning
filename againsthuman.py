from AI import *
from Board import *

class againsthuman:

    def __init__(self,name):
        self.name = name


    def board_indices(self,x_indice,y_indices):

        rows = { "a" : 0,"b":1,"c":2,"d":3,"e":4,"f":5,"g": 6 }
        columns = {"1" : 0,"2" : 1, "3": 2,"4": 3, "5": 4 ,"6":5, "7":6 }

        return rows[x_indice],columns[y_indices]

    def choose_action(self,available_moves,current_board,symbol):

        while True:

            try:
                a = list(input("Choose where you want to go : "))
                b = list(input("Choose where you want to block: "))

                move = self.board_indices(a[0], a[1])
                block = self.board_indices(b[0], b[1])

                final = (move,block)

                if final in available_moves and move != block:
                    return move,block
                else:
                    print("Invalid input")
            except:
                print("Invalid input")
                continue


        def addState(self, state):
            # append a hash state
            pass

        # at the end of game, backpropagate and update states value
        def feedReward(self, reward):
            pass

        def reset(self):
            pass


