import numpy as np
from states import ActionSpace
import main

class DeepQNetwork:
    def __init__(self, lr, gamma):
        self.learning_rate = lr
        self.gamma = gamma
        self.values = {}
        self.policy = {}

    def built_net(self):
        # ------------------ all inputs ------------------------
        # We should input state , next state (??) , reward and action to the deep learning model
        self.s = tf.placeholder(tf.float32, [None, self.n_features], name='s')  # input State
        self.s_ = tf.placeholder(tf.float32, [None, self.n_features], name='s_')  # input Next State
        self.r = tf.placeholder(tf.float32, [None, ], name='r')  # input Reward
        self.a = tf.placeholder(tf.int32, [None, ], name='a')  # input Action

        # ------------------ build target_net ------------------
        # Layers

        # Optimizer

    def compute_policy(self):
        # You also should bring tasks into it .
        initial_state =
        converged = False

        actions = [
            ActionSpace(1,0,0),
            ActionSpace(0,1,0),
            ActionSpace(0,0,1)
        ]

        # Finding value of each state
        while not converged:
            for state in :
                values = []
                for action in actions :
                    next_state, reward = self.__reward_function(action)
                    values.append(reward + self.gamma * )

                self.values[state] = np.array(values).max()

        # Finding actions in each state based on values
        for state in :
            new_v = []
            for action in actions:
                (next_state, reward) = info[(state, action)]
                new_v.append(reward + self.gamma * self.values[next_state])

            new_v = np.array(new_v)
            best_value = new_v.max()
            best_action_idx = np.where(new_v == best_value)[0]
            best_action = actions[best_action_idx[0]]
            self.policy[state] = best_action

        # Self.policy is ready .


    def __reward_function(self, action, task):
        u_comm_m_t = self.__compute_transmission_utilization(action)
        u_comp_m_t = self.__compute_calculation_utilization(action, task)

        r = u_comm_m_t + u_comp_m_t
        return n_state, r

    # Transmission utilization
    def __compute_transmission_utilization(self, action):
        return self.__compute_transmission_revenue(action) - self.__compute_transmission_cost(action)

    # Calculation utilization
    def __compute_calculation_utilization(self, action, task):
        return self.__compute_calculation_revenue(action) - self.__compute_calculation_cost(action, task)

    # Helper methods
    def __compute_transmission_revenue(self, action):
        return a * ( action.lambda_R_m_t * + action.lambda_V_m_t * )

    def __compute_transmission_cost(self, action):
        return action.lambda_R_m_t * * + action.lambda_V_m_t * *

    def __compute_calculation_revenue(self, action):
        pass

    def __compute_calculation_cost(self, action, task):
        cost = action.lambda_V_m_t * main.env.config.betta_v * task.C \
               + action.lambda_R_m_t * main.env.config.betta_r * task.C \
               + action.lambda_L_m_t * main.env.config.betta_l * task.C

        return cost


def jug(t1, t2):
    if t1 >= t2:
        return 1
    return 0
