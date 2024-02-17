# Snake Game

This project involves the implementation of a simple Snake game using Python's Pygame library.

## Prerequisites

Make sure you have Python installed on your system. You can install Pygame by running the following command:

```
pip install pygame
```
## Installation
You can install the game via this command:

```bash
sudo mkdir ~/.sk-ware && cd ~/.sk-ware && git clone https://github.com/Sakitou/Snake && cd Snake && touch run-cli.sh && echo "#!/bin/bash
python3 ~/.sk-ware/Snake/snake.py" > run-cli.sh && sudo chmod +x run-cli.sh && sudo cp run-cli.sh /usr/local/bin/snakit && touch snake.desktop && echo "[Desktop Entry]
Type=Application
Name=Snake
Exec=~/.sk-ware/Snake/run-cli.sh
Icon=~/.sk-ware/Snake/icon.png" >> snake.desktop && cp snake.desktop ~/.local/share/applications/ && echo "Finish !"
```
## How to Play

Run the `snake.py` script to start the game.

Controls:
- Use the arrow keys to move the snake.
- Press 'Q' to quit the game at any time.
- Upon losing, you can press 'C' to replay.

## Features

- The snake grows each time it eats food.
- The game ends if the snake hits the edges of the screen or if it bites its own tail.

## Code Structure

- The `game()` function contains the main logic of the game.
- The `message()` function displays messages on the screen.
- Game parameters are configured at the beginning of the script.
- Pygame events are handled to detect snake movements and player actions.
- The position of the food is randomized upon each appearance.

## Credits

This game was developed by Sakitou.

Have fun playing!
