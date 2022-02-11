# A* algorithm visualisation

## Overview

The app displays the visualisation of finding the shortest path between two points using A* algorithm and choosen heuristic of calculating distance.
You can learn more about the algorithm here: https://en.wikipedia.org/wiki/A*_search_algorithm

The user can set start and end points as well as create barriers by themselves by clicking on choosen spots on the grid.

## Requirements
- python 

## How to run
1. Clone the repository inside empty folder
    ``` bash
    cd ${project folder}
    git clone https://github.com/PaulinaGacek/A-.git
    ```
2. Create virtual environment in the project directory
    ``` bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. Install `pygame`
    ``` bash
    pip install pygame
    ```
4. Run the app
    ``` bash
    python .\scripts\main.py
    ```

## How it works

After running the programme as explained above you can choose the heuristic from listed below:

:star: manhattan

:star: euclidean

:star: diagonal

by clicking on the button with proper name. Currently pushed button is displayed as the orange one, whereas others are violet.

The next step is to set start point, end point and barriers. By clicking the left mouse button on certain spot becomes selected. First selected point becomes start point (auburn color), second becomes end point (mint color) and all further point are barriers (black color). 
Point can be unselected by clicking on it right mouse button.

When start and end point are selected and you are satisfied with barrier's appearence algorithm can be started by clicking _SPACE_ on keyboard. During the visualisations all spots are not-clickable.

When the visualisation ends user can change the heuristic, clear the grid by clicking _CTRL-C_, run the algorithm again with _SPACE_ or make changes in the grid appearence by clicking on the spot.