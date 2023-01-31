import numpy as np
from states import ActionSpace
from collections import deque
import random


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

class DeepQNetwork:
    def __init__(self, lr, gamma):
        self.learning_rate = lr
        self.gamma = gamma
        self.values = {}
        self.policy = {}

    def built_net(self):
        # ------------------ all inputs ------------------------
        # We should input state , next state (??) , reward and action to the deep learning model
        # I think only state is passed to neural network and action is retrieved .
        self.s = tf.placeholder(tf.float32, [None, self.n_features], name='s')  # input State
        self.s_ = tf.placeholder(tf.float32, [None, self.n_features], name='s_')  # input Next State
        self.r = tf.placeholder(tf.float32, [None, ], name='r')  # input Reward
        self.a = tf.placeholder(tf.int32, [None, ], name='a')  # input Action

        # ------------------ build target_net ------------------
        # Layers

        # Optimizer

    def compute_policy(self):
        # Buffer
        buffer = ReplayBuffer()

        # Environment

        # Net

        # Trainer

        # Loss function

        # Initial state
        initial_state =

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

            # If not done : move to the next_state

            # If buffer is full , empty it and backward



    def __reward_function(self, action):
        u_comm_m_t = self.__compute_transmission_utilization(action)
        u_comp_m_t = self.__compute_calculation_utilization(action)

        r = u_comm_m_t + u_comp_m_t
        return n_state, r

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


def jug(t1, t2):
    if t1 >= t2:
        return 1
    return 0
