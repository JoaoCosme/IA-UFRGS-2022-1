# valueIterationAgents.py
# -----------------------
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


import math
from os import stat
import pdb
from re import I
from sre_parse import State
from turtle import st

from numpy import Infinity
import mdp
import util
from learningAgents import ValueEstimationAgent


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """

    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        self.iterValue()

    def iterValue(self):
        states = self.mdp.getStates()
        for i in range(self.iterations):
            newValues = util.Counter()
            for state in states:
                newValues[state] = self.computeValue(state)
            self.values = newValues

    def computeValue(self, state):
        bestQ = 0
        for action in self.mdp.getPossibleActions(state):
            qForAction = self.getQValue(state, action)
            bestQ = qForAction if qForAction > bestQ else bestQ
        return self.getReward(state) + bestQ

    def getReward(self, state):
        return self.mdp.getReward(state, None, None)

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        value = 0

        if action == 'exit':
            return self.getReward(state)

        states_probs = self.mdp.getTransitionStatesAndProbs(state, action)

        for state_prob in states_probs:
            value += state_prob[1] * self.discount * \
                self.getValue(state_prob[0])

        return value

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        actions = self.mdp.getPossibleActions(state)
        if actions:
            next_states = {action: self.doAction(
                action, state) for action in actions}
            max_value = -Infinity
            best_action = None
            for action in actions:
                next_state_value = self.getValue(next_states[action])
                if next_state_value > max_value:
                    max_value = next_state_value
                    best_action = action
            return best_action
        else:
            return None

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

    def doAction(self, action, state):
        if action == 'north':
            return (state[0], state[1]+1)
        elif action == 'south':
            return (state[0], state[1]-1)
        elif action == 'west':
            return (state[0]-1, state[1])
        else:
            return (state[0]+1, state[1])
