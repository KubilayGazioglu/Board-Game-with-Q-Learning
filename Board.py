import numpy as np
import random
from AI import *
import pickle
from IPython.display import clear_output, display


class Board:
    HEIGHT = 7
    WIDTH = 7

    def __init__(self,p1,p2):
        self.cells = np.zeros((self.HEIGHT, self.WIDTH))
        self.p1 = p1
        self.p2 = p2
        self.is_game_end = False
        self.board_hash = None
        self.startpositions()

    def chunks(self, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def get_symbol(self, location):

        """
        replace number for piece value 'x' or 'o'
        to display the board with correct pieces

        """

        if location == 0:
            return " "

        elif location == 1:
            return "B"

        elif location == 2:
            return "R"

        elif location == -1:
            return "X"

    def print_board(self):
        row, col = np.indices(self.cells.shape)
        indices = list(zip(col.flatten('F'), row.flatten('F')))
        norm_line = "  |-|--------------"
        print('   1|2|3|4|5|6|7|')
        # print(norm_line)
        for row1, letter in list(zip(list(self.chunks(indices, 7)), "ABCDEFG")):
            print(letter + " |" + '|'.join([self.get_symbol(int(self.cells[x])) for x in row1]) + "|")

    def update_cells(self, row_value=None, column_value=None, piece_value=None):
        if piece_value is None:
            return self.cells

        self.cells[row_value][column_value] = piece_value
        return self.cells

    def startpositions(self):
        self.update_cells(0, 3, 1)
        self.update_cells(6, 3, 2)

    def moves(self, agent_piece):
        zero_list = []
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.cells[i][j] == agent_piece:
                    top = i - 1, j
                    topleft = i - 1, j - 1
                    topright = i - 1, j + 1
                    bottomleft = i + 1, j - 1
                    bottomright = i + 1, j + 1
                    bottom = i + 1, j
                    left = i, j - 1
                    right = i, j + 1
                    allMoves = (top, topleft, topright, topleft, topright, bottomleft, bottomright, bottom, left, right)
                    moves_position = (i for i in allMoves if i[0] >= 0 and i[1] >= 0 and i[0] < 7 and i[0] < 7)
                if self.cells[i][j] == 0:
                    zero_list.append((i, j))
        return tuple(set(moves_position).intersection(zero_list))

    def position(self, agent_piece):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.cells[i][j] == agent_piece:
                    return (i, j)

    def combinations(self,agent_player):
        a = self.moves(agent_player)
        b = self.blockmove_human()
        result = [(x, y) for x in a for y in b if x!=y]
        return result

    def blockmove_agent(self,agent_piece):
        zerolist = []
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.cells[i][j] == agent_piece:
                    top = i - 1, j
                    topleft = i - 1, j - 1
                    topright = i - 1, j + 1
                    bottomleft = i + 1, j - 1
                    bottomright = i + 1, j + 1
                    bottom = i + 1, j
                    left = i, j - 1
                    right = i, j + 1
                    allblocks = (top, topleft, topright, topleft, topright, bottomleft, bottomright, bottom, left, right)
                    blockPosition = (i for i in allblocks if i[0] >= 0 and i[1] >= 0 and i[0] < 7 and i[0] < 7)
                if self.cells[i][j] == 0:
                    zerolist.append((i, j))
        return tuple(set(blockPosition).intersection(zerolist))

    def blockmove_human(self):
        blockList = []
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.cells[i][j] == 0:
                    blockList.append((i,j))
        return blockList

    def win(self):
        p1_moves = self.moves(1,2)
        p2_moves = self.moves(2,1)

        if not p1_moves:
            self.is_game_end = True
            return 2
        if not p2_moves:
            self.is_game_end = True
            return 1
        return None

    def give_reward(self):
        result = self.win()
        if result is not None:
            if result == 1:
                self.p2.feed_reward(100)
                self.p1.feed_reward(-100)
            if result == 2:
                self.p1.feed_reward(100)
                self.p2.feed_reward(-100)

    def reset(self):
        self.cells = np.zeros((self.HEIGHT, self.WIDTH))
        self.startpositions()


    def get_hash(self):
        self.board_hash = str(self.cells.reshape(self.HEIGHT * self.WIDTH))
        return self.board_hash

    def play_ai(self,p1,p2,rounds):

        for i in range(rounds):
            if i == 0:
                p1_winner = 0
                p2_winner = 0
                self.reset()

            # agent 1
            moves = self.combinations(1)
            if moves:
                p1_moves = p1.choose_action(moves, self.cells, 1)
                mypos = self.position(1)
                self.update_cells(mypos[0], mypos[1], 0)
                self.update_cells(p1_moves[0][0], p1_moves[0][1], 1)
                self.update_cells(p1_moves[1][0], p1_moves[1][1], -1)
                board_hash = self.get_hash()
                p1.add_state(board_hash)

                # agent 2
                moves = self.combinations(2)
                if moves:
                    p2_moves = p2.choose_action(moves, self.cells, 2)
                    mypos = self.position(2)
                    self.update_cells(mypos[0], mypos[1], 0)
                    self.update_cells(p2_moves[0][0], p2_moves[0][1], 2)
                    self.update_cells(p2_moves[1][0], p2_moves[1][1], -1)
                    board_hash = self.get_hash()
                    p2.add_state(board_hash)


                else:
                    p1_winner += 1
                    p1.feed_reward(100)
                    p2.feed_reward(-100)

                    print()
                    self.print_board()
                    print('Winner: P1')
                    clear_output(wait=True)
                    self.reset()


            else:
                p2_winner += 1
                p1.feed_reward(-100)
                p2.feed_reward(100)
                print()
                self.print_board()
                print('Winner: P2')
                clear_output(wait=True)
                self.reset()

            p1.save_policy()
            p2.save_policy()

        print()
        print('Player 1 Wins: {}'.format(p1_winner))
        print('Player 2 Wins: {}'.format(p2_winner))

    def play_human(self,p1,p2):
        while not self.is_game_end:
            self.print_board()
            moves = self.combinations(1)
            if moves:
                p1_moves = p1.choose_action(moves, self.cells, 1)
                mypos = self.position(1)
                self.update_cells(mypos[0], mypos[1], 0)
                self.update_cells(p1_moves[0][0], p1_moves[0][1], 1)
                self.update_cells(p1_moves[1][0], p1_moves[1][1], -1)
                print('{} makes a move'.format(p1.name))
                print("from {} to {}".format((mypos[0], mypos[1]), (p1_moves[0][0], p1_moves[0][1])))
                print("Block move to {}".format((p1_moves[1][0], p1_moves[1][1])))
                self.print_board()

                # agent 2
                moves = self.combinations(2)
                if moves:
                    p2_moves = p2.choose_action(moves, self.cells, 2)
                    mypos = self.position(2)
                    self.update_cells(mypos[0], mypos[1], 0)
                    self.update_cells(p2_moves[0][0], p2_moves[0][1], 2)
                    self.update_cells(p2_moves[1][0], p2_moves[1][1], -1)
                    print('{} makes a move'.format(p2.name))
                    print("from {} to {}".format((mypos[0],mypos[1]),(p2_moves[0][0],p2_moves[0][1])))
                    print("Block move to {}".format((p2_moves[1][0],p2_moves[1][1])))
                    self.print_board()
                else:
                    print()
                    self.print_board()
                    print('Winner: P1')
                    self.is_game_end = True
                    clear_output(wait=True)

            else:
                print()
                self.print_board()
                print('Winner: P2')
                self.is_game_end = True
                clear_output(wait=True)
