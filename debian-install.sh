#!/bin/bash
sudo apt update
sudo apt install python3
sudo apt install python3-pygame
sudo apt install git
mkdir ~/.sakitou-ware
cd ~/.sakitou-ware
git clone https://github.com/Sakitou/Snake
cd Snake
sudo cp run-cli.sh /usr/local/snake-kit
cp snake.desktop ~/.local/share/applications/