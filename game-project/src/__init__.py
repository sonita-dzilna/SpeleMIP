

class GameNode:
    def init(self, board, player, depth):
        self.board = board
        self.player = player
        self.children = []
        self.value = None
        self.depth = depth

    

    