import numpy as np
from states import ActionSpace

class DeepQNetwork:
    def __init__(self):
        # Read this from config
        self.learning_rate = .9
        pass

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
        initial_state =
        converged = False

        actions = [
            ActionSpace(1,0,0),
            ActionSpace(0,1,0),
            ActionSpace(0,0,1)
        ]

        while not converged:
            for state in :
                values = []
                for action in actions :
                    next_state, reward = self.reward_function(action)
                    values.append(reward + gamma * )

                v[state] = np.array(values).max()

        pass

    def reward_function(self, action):
        u_comm_m_t = self.compute_transmission_utilization(action)
        u_comp_m_t = self.compute_calculation_utilization(action)

        r = u_comm_m_t + u_comp_m_t
        return n_state, r

    # Transmission utilization
    def compute_transmission_utilization(self, action):
        return self.compute_transmission_revenue(action) - self.compute_transmission_cost(action)

    # Calculation utilization
    def compute_calculation_utilization(self, action):
        return self.compute_calculation_revenue(action) - self.compute_calculation_cost(action)

    # Helper methods
    def compute_transmission_revenue(self, action):
        return a * ( action.lambda_R_m_t * + action.lambda_V_m_t * )

    def compute_transmission_cost(self, action):
        return action.lambda_R_m_t * * + action.lambda_V_m_t * *

    def compute_calculation_revenue(self, action):
        pass

    def compute_calculation_cost(self, action):
        pass


def jug(t1, t2):
    if t1 >= t2:
        return 1
    return 0
