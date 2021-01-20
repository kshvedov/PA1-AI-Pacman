# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # Import instructions for pacman and create a dict for translation
    from game import Directions
    dirc = {"North": Directions.NORTH, "East": Directions.EAST,
            "South": Directions.SOUTH, "West": Directions.WEST}

    # Prepare Variables for algorithm
    used = set()                            # Holds all used locations, Set used to avoid duplicates
    fringe = util.Stack()                   # Stack used for DFS as the fringe holder
    start_node = problem.getStartState()    # Get Start Node
    fringe.push((start_node, []))           # Push the start node as the fringe
    f_path = []                             # Final path holder

    while True:
        # Check to see if Fringe is empty, if it is empty, no solution found
        if fringe.isEmpty():
            print("No Solution found!")
            return []

        # For ease of use, item from fringe is dissected into two
        node = fringe.pop() # First item removed
        loc  = node[0]      # Location Extracted
        path = node[1]      # Path to current position extracted

        # If the current location is the Goal, Solution has been found
        if problem.isGoalState(loc):
            print("Solution Found!")
            f_path = path
            break

        # If the location has already been explored prevents from duplicate
        if loc not in used:
            used.add(loc) # Added to to used set
            # All possible next positions from current position are added to fringe
            # if they haven't been visited before
            for item in problem.getSuccessors(loc):
                if item[0] not in used:
                    fringe.push((item[0], path + [item[1]]))

    print("Path that was found of length {:}:".format(len(f_path)))
    print(f_path)
    return [dirc[s] for s in f_path]


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Import instructions for pacman and create a dict for translation
    from game import Directions
    dirc = {"North": Directions.NORTH, "East": Directions.EAST,
            "South": Directions.SOUTH, "West": Directions.WEST}

    # Prepare Variables for algorithm
    used = set()                            # Holds all used locations, Set used to avoid duplicates
    fringe = util.Queue()                   # Queue used for BFS as the fringe holder
    start_node = problem.getStartState()    # Get Start Node
    fringe.push((start_node, []))           # Push the start node as the fringe
    f_path = []                             # Final path holder

    while True:
        # Check to see if Fringe is empty, if it is empty, no solution found
        if fringe.isEmpty():
            print("No Solution found!")
            return []

        # For ease of use, item from fringe is dissected into two
        node = fringe.pop()     # First item removed
        loc = node[0]           # Location Extracted
        path = node[1]          # Path to current position extracted

        # If the current location is the Goal, Solution has been found
        if problem.isGoalState(loc):
            print("Solution Found!")
            f_path = path
            break

        # If the location has already been explored prevents from duplicate
        if loc not in used:
            used.add(loc)  # Added to to used set
            # All possible next positions from current position are added to fringe
            # if they haven't been visited before
            for item in problem.getSuccessors(loc):
                if item[0] not in used:
                    fringe.push((item[0], path + [item[1]]))

    print("Path that was found of length {:}:".format(len(f_path)))
    print(f_path)
    return [dirc[s] for s in f_path]

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Import instructions for pacman and create a dict for translation
    from game import Directions
    dirc = {"North": Directions.NORTH, "East": Directions.EAST,
            "South": Directions.SOUTH, "West": Directions.WEST}

    # Prepare Variables for algorithm
    used = set()                            # Holds all used locations, Set used to avoid duplicates
    fringe = util.PriorityQueue()           # Stack used for DFS as the fringe holder
    start_node = problem.getStartState()    # Get Start Node
    fringe.push((start_node, []), 0)           # Push the start node as the fringe

    while True:
        # Check to see if Fringe is empty, if it is empty, no solution found
        if fringe.isEmpty():
            print("No Solution found!")
            return []

        # For ease of use, item from fringe is dissected into two
        node = fringe.pop()  # First item removed
        loc = node[0]  # Location Extracted
        path = node[1]  # Path to current position extracted

        # If the current location is the Goal, Solution has been found
        if problem.isGoalState(loc):
            print("Solution Found!")
            f_path = path
            break

        # If the location has already been explored prevents from duplicate
        if loc not in used:
            used.add(loc)  # Added to to used set
            # All possible next positions from current position are added to fringe
            # if they haven't been visited before
            for item in problem.getSuccessors(loc):
                if item[0] not in used:
                    t_path = path + [dirc[item[1]]]
                    cost = problem.getCostOfActions(t_path)
                    fringe.push((item[0], t_path), cost)

    print("Path that was found of length {:}:".format(len(f_path)))
    return f_path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Import instructions for pacman and create a dict for translation
    from game import Directions
    dirc = {"North": Directions.NORTH, "East": Directions.EAST,
            "South": Directions.SOUTH, "West": Directions.WEST}
    print(dirc)
    input()

    # Prepare Variables for algorithm
    used = set()  # Holds all used locations, Set used to avoid duplicates
    fringe = util.PriorityQueue()  # Stack used for DFS as the fringe holder
    start_node = problem.getStartState()  # Get Start Node
    fringe.push((start_node, []), 0)  # Push the start node as the fringe

    while True:
        # Check to see if Fringe is empty, if it is empty, no solution found
        if fringe.isEmpty():
            print("No Solution found!")
            return []

        # For ease of use, item from fringe is dissected into two
        node = fringe.pop()  # First item removed
        loc = node[0]  # Location Extracted
        path = node[1]  # Path to current position extracted

        # If the current location is the Goal, Solution has been found
        if problem.isGoalState(loc):
            print("Solution Found!")
            f_path = path
            break

        # If the location has already been explored prevents from duplicate
        if loc not in used:
            used.add(loc)  # Added to to used set
            # All possible next positions from current position are added to fringe
            # if they haven't been visited before
            for item in problem.getSuccessors(loc):
                if item[0] not in used:
                    t_path = path + [dirc[item[1]]]
                    cost = problem.getCostOfActions(t_path)
                    fringe.push((item[0], t_path), cost + heuristic(item[0], problem))

    print("Path that was found of length {:}:".format(len(f_path)))
    print(f_path)
    input()
    return f_path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
