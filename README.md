# ReverseGame-IA

#### Game implementation using Python

**Creators**: [Felipe Teles](https://github.com/felipersteles), [Nerval Junior](https://github.com/nervaljunior), [Rodrigo Pontes](https://github.com/rodrigopontis), and [João Leonardo](https://github.com/joaoleopo)

![](https://img.shields.io/badge/Language-Python-blue) ![](https://img.shields.io/badge/IDE-Microsoft%20Visual%20Studio%202022-blue) ![](https://img.shields.io/badge/Environment-Windows-red) ![](https://img.shields.io/badge/User%20Interface-GUI%20%2B%20CLI-yellowgreen)

---

## Objective

### The goal is to create an AI with good heuristics

To win, you need to have more pieces on the board than your opponent by the end of the game. Like checkers or chess, the game pieces are black or white. When the game ends, each player counts their remaining pieces on the board to determine the winner.

### The board is 8x8

![image](https://github.com/nervaljunior/ReverseGame-IA/assets/108685222/0595d500-3604-4c48-a6c9-848eb06eba05)

### In the game, the pieces have a black side and a white side

### If a piece of a different color traps the piece of a different color, the middle pieces change color.

### They can be trapped diagonally, vertically, and horizontally

## Implementing the Heuristic

![image](https://github.com/nervaljunior/ReverseGame-IA/assets/108685222/2e885141-9983-4b27-b46a-0b9695196bd3)

To implement the heuristic, just apply the conditions created and studied in the function that checks the computer's moves, which is present in **line 185** of the file [reversi.py](./reversi.py).

## Tips:

- Be the last to deliver the sides and the corners and their adjacents.
- Make the opponent move away from the middle first.
- Pay attention to the edges.

![image](https://github.com/nervaljunior/ReverseGame-IA/assets/108685222/ee80b913-5e92-4796-ac78-c9933f3781c5)

## "Games are to AI as races are to car projects" (S.Russel)

# Artificial Intelligence 28/03/2023

Agent-oriented language

## Concepts

### Perception
Information that the agent can gather from the environment.
- Example: neighborhood

### Actions
What the agent does
- Example: walk, collect, release

### Performance
Based on runtime

## Basic types of agents
- Simple reactive agents
- Model-based reactive agents
- Goal-based agents
- Utility-based agents

### Simple reactive agent
- Makes decisions based only on the current perceptions of the environment.
- Does not take into account the history of actions or the future state of the environment.
- They automatically respond to stimuli from the environment without having an internal representation of the world.

### Model-based reactive agent
- Keeps histories
- These agents also make decisions based on current perceptions of the environment.
- They have an internal representation of the environment that allows them to build internal models of the world.
- They use these models to predict the effect of their actions before acting, allowing them to make more informed choices.

### Goal-based agent
- Starts execution with a list of goals.
- They use information about the environment.
- Their internal state and their goals to plan and execute actions that bring them closer to their goals.

### Utility-based agent
- Has happiness
- These agents assign utility values to different actions and choose the action that maximizes the expected utility. They may take into account not only immediate goals but also the long-term consequences of their actions.
- Example: items that are worth more points, etc...
