import random
import pygame
from pacman import Pacman, Ghost, Maze

class MonteCarloPacman(Pacman):
    def choose_direction(self, ghosts, maze, n_distance):
        safe_directions = []
        for direction in self.available_directions(maze):
            if not self.is_ghost_nearby(direction, ghosts, n_distance):
                safe_directions.append(direction)

        if safe_directions:
            return random.choice(safe_directions)
        return random.choice(self.available_directions(maze))

    def is_ghost_nearby(self, direction, ghosts, n_distance):
        next_position = self.get_next_position(direction)
        for ghost in ghosts:
            if self.manhattan_distance(next_position, ghost.position) <= n_distance:
                return True
        return False

    def get_next_position(self, direction):
        x, y = self.position
        if direction == 'up':
            return (x, y - 1)
        elif direction == 'down':
            return (x, y + 1)
        elif direction == 'left':
            return (x - 1, y)
        elif direction == 'right':
            return (x + 1, y)

    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Використання класу в грі:
if __name__ == "__main__":
    maze = Maze("maze2.txt")
    pacman = MonteCarloPacman()
    ghosts = [Ghost("ghost1", maze), Ghost("ghost2", maze)]
    pacman.play_game(maze, ghosts)