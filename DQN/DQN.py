class DeepQNetwork:
    def __init__(self):
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

    def reward_function(self, action, new_s):
        u_comm_m_t = self.compute_transmission_utilization()
        u_comp_m_t = self.compute_calculation_utilization()

        r = u_comm_m_t + u_comp_m_t
        return r

    # Transmission utilization
    def compute_transmission_utilization(self, action):
        return self.compute_transmission_revenue(action) - self.compute_transmission_cost(action)

    def compute_transmission_revenue(self, action):
        pass

    def compute_transmission_cost(self, action):
        pass

    # Calculation utilization
    def compute_calculation_utilization(self, action):
        return self.compute_calculation_revenue(action) - self.compute_calculation_cost(action)

    def compute_calculation_revenue(self, action):
        pass

    def compute_calculation_cost(self, action):
        pass


def jug(t1, t2):
    if t1 >= t2:
        return 1
    return 0
