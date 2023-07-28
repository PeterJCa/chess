# Chess Project

This is a simple implementation of a chess game using Python and the Tkinter library for the graphical user interface.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

The Chess Project is a Python application that allows you to play a game of chess against another human player on your computer. It provides a simple graphical interface using the Tkinter library.

## Features

- Classic chess rules and movements.
- Interactive graphical interface to play the game.
- Highlighting available moves for each piece.
- Detecting and notifying when a player's king is in check.

## Yet-to-be-Implemented Features

- **En Passant**: Implement the special pawn capture move known as "en passant" when an opponent's pawn advances two squares from its starting position and lands next to your pawn.
- **Promotion**: Implement the ability for pawns to be promoted to other pieces when they reach the opposite end of the board.
- **Castling**: Implement the castling move, where the king and one of the rooks move in a single move.
- **Check and Checkmate**: Implement the logic to declare check and checkmate when a player's king is under threat and cannot escape capture.

## Requirements

- Python 3.x
- Tkinter (usually included in standard Python installations)

## Installation

1. Make sure you have Python 3.x installed on your computer.
2. Clone this repository to your local machine using `git clone`.
3. Install Tkinter library (if not already installed) using `pip install tk` command.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the command `python chess.py` to start the chess application.
4. The chessboard will be displayed on the screen, and you can start playing by clicking on the pieces and moving them according to the classic chess rules.
