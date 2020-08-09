from collections ______ deque


class SnakeGame(object

  ___ __init__(self, width, height, food
    """
    Initialize your data structure here.
    @param width - screen width
    @param height - screen height 
    @param food - A list of food positions
    E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
    :type width: int
    :type height: int
    :type food: List[List[int]]
    """
    self.snake = deque([(0, 0)])
    self.snakeSet = set([(0, 0)])
    self.width = width
    self.height = height
    self.food = deque(food)
    self.directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    self.score = 0

  ___ move(self, direction
    """
    Moves the snake.
    @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
    @return The game's score after the move. Return -1 if game over. 
    Game over when snake crosses the screen boundary or bites its body.
    :type direction: str
    :rtype: int
    """
    __ direction not in self.directions:
      r_ -1
    di, dj = self.directions[direction]
    ni, nj = self.snake[0][0] + di, self.snake[0][1] + dj

    __ ni < 0 or ni >= self.height or nj < 0 or nj >= self.width:
      r_ -1

    self.snake.appendleft((ni, nj))

    __ self.food and [ni, nj] __ self.food[0]:
      self.score += 1
      self.food.popleft()
    ____
      self.snakeSet.discard(self.snake.pop())

    __ (ni, nj) in self.snakeSet:
      r_ -1
    self.snakeSet |= {(ni, nj)}

    r_ self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
