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
        self.state = None

    def reset(self):
        # This method leads us to the initial state
        self.state = State() # Fill inputs
        return self.state

    def compute_policy(self, init_state):

        # Environment --> it must return the init_state and step

        # Net
        net = self.build_model()

        # Trainer

        # Loss function

        # Finding value of each state
        while not converged:




    def __reward_function(self, state, action):
        n_state = self.step(state, action)

        u_comm_m_t = self.__compute_transmission_utilization(action)
        u_comp_m_t = self.__compute_calculation_utilization(action)

        r = u_comm_m_t + u_comp_m_t
        return n_state, r

    def step(self, state, action) : # returns reward, next_state, state, action, done
        # These parameters are updated to direct us to the next state
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

        next_state = State()
        reward = self.__reward_function(state, action)

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

    def __init__(self, capacity):
        # Buffer
        self.replay_buffer = ReplayBuffer(capacity)

    def add_to_replay_memory(self, transition):
        self.replay_buffer.push(transition)

    def get_qs(self, current_state):
        pass

    def train(self, done, step):
        pass


def jug(t1, t2):
    if t1 >= t2:
        return 1
    return 0
