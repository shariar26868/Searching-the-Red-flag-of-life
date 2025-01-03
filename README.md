# Searching the Red Flag of Life - Maze Game

## Overview

"Searching the Red Flag of Life" is a maze navigation game where the player controls a character navigating through a maze to reach the end while collecting power-ups along the way. The game features a simple grid-based maze, a player character that moves with keyboard controls, and various interactive elements like walls, power-ups, and a goal (the red flag).

The game ends when the player reaches the red flag or hits the "Game Over" condition. The player earns points for every step they take and additional points for collecting power-ups. The game also includes an option to restart or quit at the end.

## Features

- **Maze Navigation**: Navigate through a maze using WASD keys.
- **Power-ups**: Collect power-ups scattered throughout the maze for bonus points.
- **Goal**: Reach the red flag at the end of the maze to win.
- **Game Over Screen**: The game shows a "Game Over" message when the player reaches the end.
- **Game Restart**: You can restart the game after completing it.
- **Simple Graphics**: The game is rendered using OpenGL with basic shapes and textures.

## How to Play

1. **Start the Game**: Launch the game using the Python environment.
2. **Navigate**: Use the following keys to navigate through the maze:
   - **W**: Move Up
   - **S**: Move Down
   - **A**: Move Left
   - **D**: Move Right
3. **Collect Power-ups**: Power-ups are scattered throughout the maze. Move over them to collect them for bonus points.
4. **Reach the Red Flag**: The red flag marks the end of the maze. Once you reach it, the game ends, and you will see your score.
5. **Restart or Quit**: After completing the maze:
   - Press **R** to restart the game.
   - Press **Q** to quit.

## Requirements

To run the game, you need the following:

- Python 3.x
- OpenGL
- PyOpenGL
- GLUT (OpenGL Utility Toolkit)

### Installing Dependencies

1. Install Python (if you haven't already) from [python.org](https://www.python.org/downloads/).
2. Install the necessary libraries using pip:

```bash
pip install PyOpenGL PyOpenGL_accelerate
