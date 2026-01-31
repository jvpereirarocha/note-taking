# A simple example of a goal-based agent.
# This agent is a robotic vacuum cleaner in a two-room environment.

class Environment:
    """
    Represents the environment for the vacuum cleaner agent.
    It has two rooms, A and B, which can be 'Clean' or 'Dirty'.
    """
    def __init__(self):
        # Room status: 'Clean' or 'Dirty'
        self.rooms = {'A': 'Dirty', 'B': 'Dirty'}

    def get_percept(self, agent_location):
        """
        Returns the perception of the agent.
        It's a tuple: (location, room_status)
        """
        return (agent_location, self.rooms[agent_location])

    def clean_room(self, room):
        """Sets the status of a room to 'Clean'."""
        self.rooms[room] = 'Clean'
        print(f"Room {room} has been cleaned.")


class Agent:
    """
    Represents the goal-based vacuum cleaner agent.
    The agent's goal is to have both rooms clean.
    """
    def __init__(self, environment):
        self.environment = environment
        self.location = 'A'  # Start in Room A
        self.goal_achieved = False

    def act(self):
        """
        Determines the agent's action based on its perception.
        """
        location, status = self.environment.get_percept(self.location)
        print(f"Agent is in Room {location}. Room status is: {status}")

        if self.environment.rooms['A'] == 'Clean' and self.environment.rooms['B'] == 'Clean':
            self.goal_achieved = True
            print("Goal achieved! Both rooms are clean.")
            return 'do_nothing'

        if status == 'Dirty':
            return 'suck_dirt'
        elif location == 'A':
            return 'go_to_B'
        elif location == 'B':
            return 'go_to_A'

    def run(self):
        """
        Runs the agent until the goal is achieved.
        """
        while not self.goal_achieved:
            action = self.act()
            if action == 'suck_dirt':
                self.environment.clean_room(self.location)
            elif action == 'go_to_A':
                self.location = 'A'
                print("Agent moved to Room A.")
            elif action == 'go_to_B':
                self.location = 'B'
                print("Agent moved to Room B.")
            elif action == 'do_nothing':
                break
            print("-" * 20)


def main():
    """
    Main function to run the simulation.
    """
    print("Initializing simulation...")
    env = Environment()
    agent = Agent(env)
    
    print(f"Initial state: Room A is {env.rooms['A']}, Room B is {env.rooms['B']}")
    print("-" * 20)

    agent.run()

if __name__ == "__main__":
    main()
