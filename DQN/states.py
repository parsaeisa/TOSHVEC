class State:
    def __init__(self):
        self.G_j_m_t = 0
        self.G_R_m_t = 0

        self.freq_R_m_t = 0
        self.freq_l_m_t = 0
        self.freq_j_m_t = 0


class ActionSpace:
    """
    action space is dedicated to each task (??)
    """

    def __init__(self, lambda_R_m_t, lambda_L_m_t, lambda_V_m_t):
        self.lambda_R_m_t = lambda_R_m_t
        self.lambda_L_m_t = lambda_L_m_t
        self.lambda_V_m_t = lambda_V_m_t
