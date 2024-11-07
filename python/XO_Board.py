class Board:
    def __init__(self):
        self.board = [[" " for i in range(3)] for j in range(3)]

    def print_board(self):
        print("  1 2 3")
        for y in range(3):
            line = f"{y+1} {self.board[y][0]}|{self.board[y][1]}|{self.board[y][2]}"
            print(line)
            if y != 2:
                print("  -----")
        print("")

    def set_point(self, point_type, x, y):
        if x < 1 or x > 3 or y < 1 or y > 3:
            return False
        if self.board[y-1][x-1] == " ":
            self.board[y-1][x-1] = point_type
            return True
        return False

    def is_winner(self):
        for current_player in ["x", "o"]:
            for y in range(3):
                counter = 0
                for x in range(3):
                    if self.board[y][x] == current_player:
                        counter += 1
                if counter == 3:
                    return current_player

            for x in range(3):
                counter = 0
                for y in range(3):
                    if self.board[y][x] == current_player:
                        counter += 1
                if counter == 3:
                    return current_player

            if self.board[0][0] == current_player and self.board[1][1] == current_player and self.board[2][2] == current_player:
                return current_player

            if self.board[0][2] == current_player and self.board[1][1] == current_player and self.board[2][0] == current_player:
                return current_player

        for y in range(3):
            for x in range(3):
                if self.board[y][x] == " ":
                    return None

        return "draw"

    def user_go(self):
        can_progress = False
        while not can_progress:
            y = int(input("Please enter y : "))
            x = int(input("Please enter x : "))
            can_progress = self.set_point("x", x, y)

    def _is_on_diagonal(self, x, y):
        diagonal_points = [[0,0], [1,1], [2,2], [2,0], [0,2]]
        if [x,y] in diagonal_points:
            return True
        return False

    def _get_available_option(self, player, x, y):
        count = 0
        if self.board[y][0] != player and self.board[y][1] != player and self.board[y][2] != player:
            count += 1

        if self.board[0][x] != player and self.board[1][x] != player and self.board[2][x] != player:
            count += 1

        if self._is_on_diagonal(x,y):
            if ( (x == 0 and y == 0) or (x == 2 and y == 2) or (x == 1 and y == 1) ) and self.board[0][0] != player and self.board[1][1] != player and self.board[2][2] != player:
                count += 1
            if ( (x == 2 and y == 0) or (x == 0 and y == 2) or (x == 1 and y == 1) ) and self.board[0][2] != player and self.board[1][1] != player and self.board[2][0] != player:
                count += 1

        return count

    def find_best_move(self, player):
        best_place = { "score": 0, "x": -1, "y": -1}

        # find place if can win
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == " ":
                    self.board[y][x] = player
                    if self.board[0][x] == player and self.board[1][x] == player and self.board[2][x] == player:
                        best_place = { "score": 1000, "x": x+1, "y": y+1}
                    if self.board[y][0] == player and self.board[y][1] == player and self.board[y][2] == player:
                        best_place = { "score": 1000, "x": x+1, "y": y+1}
                    if self._is_on_diagonal(x,y):
                        if ( (x == 0 and y == 0) or (x == 2 and y == 2) or (x == 1 and y == 1) ) and self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
                            best_place = { "score": 1000, "x": x+1, "y": y+1}
                        if ( (x == 2 and y == 0) or (x == 0 and y == 2) or (x == 1 and y == 1) ) and self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
                            best_place = { "score": 1000, "x": x+1, "y": y+1}
                    self.board[y][x] = " "
                    if best_place["score"] == 1000:
                        return best_place

        # find place to prevent win
        opposite_player = self._get_opposite_player(player)
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == " ":
                    self.board[y][x] = opposite_player
                    if self.board[0][x] == opposite_player and self.board[1][x] == opposite_player and self.board[2][x] == opposite_player:
                        best_place = { "score": 800, "x": x+1, "y": y+1}
                    if self.board[y][0] == opposite_player and self.board[y][1] == opposite_player and self.board[y][2] == opposite_player:
                        best_place = { "score": 800, "x": x+1, "y": y+1}
                    if self._is_on_diagonal(x,y):
                        if ( (x == 0 and y == 0) or (x == 2 and y == 2) or (x == 1 and y == 1) ) and self.board[0][0] == opposite_player and self.board[1][1] == opposite_player and self.board[2][2] == opposite_player:
                            best_place = { "score": 800, "x": x+1, "y": y+1}
                        if ( (x == 2 and y == 0) or (x == 0 and y == 2) or (x == 1 and y == 1) ) and self.board[0][2] == opposite_player and self.board[1][1] == opposite_player and self.board[2][0] == opposite_player:
                            best_place = { "score": 800, "x": x+1, "y": y+1}
                    self.board[y][x] = " "
                    if best_place["score"] == 800:
                        return best_place

        # calculate how many rows are still open
        count = 0
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == " ":
                    count = self._get_available_option(player,x,y)*10
                    if count > best_place["score"]:
                        best_place = { "score": count, "x": x+1, "y": y+1}

        # calculate how many rows will be close


        # first free place
        if best_place["score"] == 0:
            for y in range(3):
                for x in range(3):
                    if self.board[y][x] == " ":
                        best_place["x"] = x + 1
                        best_place["y"] = y + 1
                        return best_place

        return best_place

    def _get_opposite_player(self, player):
        if player == 'x':
            return 'o'
        return 'x'
