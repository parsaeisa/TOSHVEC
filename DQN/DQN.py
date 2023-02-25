import numpy as np
from states import ActionSpace, State
from collections import deque
import random

# from mxnet import nd, autograd, gluon, init
# from mxnet.gluon import nn, loss as gloss
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Activation, Flatten

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

    def step(self, state, action) : # returns reward, next_state, done
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

        # I think the done is false when at least one of the resources value is zero
        done = False

        next_state = State()
        reward = self.__reward_function(state, action)

        return  next_state, reward, done

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


class DQNAgent:

    def __init__(self, capacity, batch_size, discount_factor):
        # Buffer
        self.replay_buffer = ReplayBuffer(capacity)

        # Net
        self.net = self.build_model()

        # Parameters
        self.action_size = 3  # read from config
        self.batch_size = batch_size
        self.discount_factor = discount_factor


    def add_to_replay_memory(self, transition):
        self.replay_buffer.push(transition)

    def get_qs(self, current_state):
        # Here we call the predict method in our model
        pass

    def train(self, done, step):
        # sampling random data from replay_memory
        states, actions, rewards, next_states, done = self.replay_buffer.sample(self.batch_size)


        # pre-process them
        input_data = []
        label = []

        current_q_values = self.net.predict(states)
        future_q_values = self.net.predict(next_states)

        for index in range(self.batch_size):
            max_future_q_value = np.max(future_q_values)
            taken_action_q_value = rewards[index] + self.discount_factor * max_future_q_value

            q_values = current_q_values[index]
            q_values[actions[index]] = taken_action_q_value

            input_data.append(states[index])
            label.append(q_values)

        # model.fit
        pass

    def build_model(self):
        net = Sequential()
        # The input is the state , neurons count equals state_size
        # The output is the q-value for each action , so the neurons count in the last layer
        # equals to number of actions
        net.add(Dense(256, activation='relu'),
                Dense(self.action_size, activations="relu"))

        # net.initialize(init.Normal(sigma=0.001)) # What is it ???

        return net

def jug(t1, t2):
    if t1 >= t2:
        return 1
    return 0
