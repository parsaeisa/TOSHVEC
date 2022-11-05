class State:
    def __init__(self):
        self.G_j_m_t = 0
        self.G_R_m_t = 0

        self.f_R_m_t = 0
        self.f_l_m_t = 0
        self.f_j_m_t = 0


class ActionSpace:
    """
    action space is dedicated to each task (??)
    """

    def __init__(self):
        self.lambda_R_m_t = 0
        self.lambda_L_m_t = 0
        self.lambda_V_m_t = 0


def reward_function(s, action, new_s):
    u_comm_m_t = 0  # add expression
    u_comp_m_t = 0  # add expression

    r = u_comm_m_t + u_comp_m_t
    return r
