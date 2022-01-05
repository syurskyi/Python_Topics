____ c.. _______ d..


c_ SnakeGame(object):

  ___ - , width, height, food):
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
    snake = d..([(0, 0)])
    snakeSet = set([(0, 0)])
    width = width
    height = height
    food = d..(food)
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    score = 0

  ___ move  direction):
    """
    Moves the snake.
    @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
    @return The game's score after the move. Return -1 if game over. 
    Game over when snake crosses the screen boundary or bites its body.
    :type direction: str
    :rtype: int
    """
    __ direction n.. __ directions:
      r.. -1
    di, dj = directions[direction]
    ni, nj = snake[0][0] + di, snake[0][1] + dj

    __ ni < 0 o. ni >= height o. nj < 0 o. nj >= width:
      r.. -1

    snake.appendleft((ni, nj))

    __ food a.. [ni, nj] __ food[0]:
      score += 1
      food.popleft()
    ____:
      snakeSet.discard(snake.pop())

    __ (ni, nj) __ snakeSet:
      r.. -1
    snakeSet |= {(ni, nj)}

    r.. score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
