# Custom Agent Example: A Simple Goal-Based Agent

This document explains the provided `custom_agent_example.py` file, which demonstrates how to create a simple goal-based AI agent using Python.

## The Scenario: A Robotic Vacuum Cleaner

The example simulates a robotic vacuum cleaner whose goal is to clean a two-room apartment (Room A and Room B). This is a classic AI problem used to illustrate the concept of agents.

## How the Agent Works

The `custom_agent_example.py` file contains two main classes:

1.  `Environment`: This class represents the world in which the agent operates.
    *   It keeps track of the state of the rooms (whether they are 'Clean' or 'Dirty').
    *   It provides the agent with its perceptions (its current location and whether that location is clean or dirty).

2.  `Agent`: This class represents the vacuum cleaner itself.
    *   **Perception:** The agent can "see" its current location and the status of the room it is in.
    *   **Goal:** Its goal is to have both rooms clean. It constantly checks if this goal has been met.
    *   **Actions:** The agent can perform a limited set of actions:
        *   `suck_dirt`: Clean the current room.
        *   `go_to_A` / `go_to_B`: Move to the other room.
        *   `do_nothing`: Stop when the goal is achieved.
    *   **Logic (Decision Making):** The agent follows a simple set of rules to decide its next action:
        1.  If all rooms are clean, the goal is achieved, and it does nothing.
        2.  If the current room is dirty, it cleans it (`suck_dirt`).
        3.  If the current room is clean, it moves to the other room to check its status.

## How to Run the Example

You can run the simulation directly from your terminal:

```bash
python3 custom_agent_example.py
```

You will see the agent's thought process printed to the console as it perceives the environment, takes actions, and works towards its goal of cleaning both rooms.

## What This Example Teaches

This simple example illustrates the core principles of an AI agent:

*   **Autonomy:** The agent runs on its own without direct human control.
*   **Perception:** It uses sensors (in this case, simulated ones) to understand its environment.
*   **Action:** It uses actuators (a vacuum and wheels, simulated) to change the environment.
*   **Goal-Oriented Behavior:** Its actions are not random; they are driven by a clear objective.

This is a foundational example. Real-world agents are far more complex, often incorporating machine learning to learn from their environment, predict outcomes, and make more sophisticated decisions. However, the basic loop of "perceive -> think -> act" remains the same.
