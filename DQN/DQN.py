import numpy as np
from states import ActionSpace, State
from collections import deque
import random

from mxnet import nd, autograd, gluon, init
from mxnet.gluon import nn, loss as gloss


class playground:
    def __init__(self):
        pass

    def init_state(self):
        pass

    def transition_function(self) -> (State, float, bool) :
        pass

class ReplayBuffer(object):
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        state = np.expand_dims(state, 0)
        next_state = np.expand_dims(next_state, 0)
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        state, action, reward, next_state, done = zip(*random.sample(self.buffer, batch_size))
        return np.concatenate(state), action, reward, np.concatenate(next_state), done

    def __len__(self):
        return len(self.buffer)

class DeepQEnvironment:
    def __init__(self, lr, gamma, capacity):
        self.action_size = 3 # read from config
        self.learning_rate = lr
        self.gamma = gamma
        self.values = {}
        self.policy = {}
        self.capacity = capacity

    def compute_policy(self, init_state):
        # Buffer
        replay_buffer = ReplayBuffer(self.capacity)

        # Environment --> it must return the init_state and step

        # Net
        net = self.build_model()

        # Trainer

        # Loss function

        # Initial state
        initial_state = init_state

        # The loop
        converged = False

        actions = [
            ActionSpace(1,0,0),
            ActionSpace(0,1,0),
            ActionSpace(0,0,1)
        ]

        # Finding value of each state
        while not converged:

            # Extract action
            action =

            # Extract reward, next_state, and done from that action
            next_state, reward = self.__reward_function(action)

            # If done: move to initial state
            if :
                # ra is for resource allocation
                initial_state = init_state
                replay_buffer.push(state, (action_ra, action_rf), reward, next_state, done)

            # If not done : move to the next_state
            if :
                replay_buffer.push(state, (action_ra, action_rf), reward, next_state, done)

            # If buffer is full , empty it and backward



    def __reward_function(self, state, action):
        n_state = self.step(state, action)

        u_comm_m_t = self.__compute_transmission_utilization(action)
        u_comp_m_t = self.__compute_calculation_utilization(action)

        r = u_comm_m_t + u_comp_m_t
        return n_state, r

    def step(self, state, action):
        # Offloading to RSU
        if action.lambda_R_m_t == 1 :
            # update G_R_m_t & freq_R_m_t
            pass

        # Offloading to co-operative vehicle
        if action.lambda_V_m_t == 1 :
            # update G_V_m_t & freq_V_m_t
            pass

        # processing locally
        if action.lambda_L_m_t == 1 :
            # update freq_l_m_t
            pass

    # Transmission utilization
    def __compute_transmission_utilization(self, action):
        return self.__compute_transmission_revenue(action) - self.__compute_transmission_cost(action)

    # Calculation utilization
    def __compute_calculation_utilization(self, action):
        return self.__compute_calculation_revenue(action) - self.__compute_calculation_cost(action)

    # Helper methods
    def __compute_transmission_revenue(self, action):
        return a * ( action.lambda_R_m_t * + action.lambda_V_m_t * )

    def __compute_transmission_cost(self, action):
        return action.lambda_R_m_t * * + action.lambda_V_m_t * *

    def __compute_calculation_revenue(self, action):
        pass

    def __compute_calculation_cost(self, action):
        pass

    def build_model(self):
        net = nn.Sequential()
        # The input is the state , neurons count equals state_size
        # The output is the q-value for each action , so the neurons count in the last layer
        # equals to number of actions
        net.add(nn.Dense(256, activation='relu'),
                nn.Dense(self.action_size, activations="relu"))

        net.initialize(init.Normal(sigma=0.001))

        return net


class DQNAgent:


def jug(t1, t2):
    if t1 >= t2:
        return 1
    return 0
