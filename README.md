
# Kaooa Game

## Steps to Execute Code

1. Run the command `python3 src/kaooa.py` to start the game.

## Game Arena

- Upon running the game, you will see the initialized game arena with a star-like figure. The top right corner displays "Crows left: 7" and "Crows Killed: 0".
- The first turn is for the Crow, indicated by the yellow color.
- Deploy a new Crow by clicking on any unoccupied circle of the star.
- The next turn is for the Vulture, denoted by the blue color. Deploy the Vulture in a similar way.
- Deploy all seven crows one by one. Attempting to move a crow before deploying all crows will display errors.
- Alternating turns for the Vulture involve moving or jumping off a crow. Click on the circle occupied by the Vulture to see possible moves in red/green colors. Red indicates potential kills, while green indicates regular moves.
- Moving the Vulture to an invalid location will result in errors.
- After deploying all crows, move any crow to an adjacent unoccupied place (displayed in green).
- Move the Vulture and crows one by one.
- If the Vulture successfully jumps off 4 crows, it wins. The crow count increases with each successful jump.
- If the Vulture has no valid moves, the Crows win.
- After the game result, the screen automatically switches off.
- Note: If the Crows win, click on the Vulture once to display the victory message.

Enjoy the Crow vs Vulture game!
