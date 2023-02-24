class State:
    def __init__(self, G_j_m_t, G_R_m_t,
                 freq_R_m_t, freq_l_m_t, freq_j_m_t):
        # task transmission
        self.G_j_m_t = G_j_m_t
        self.G_R_m_t = G_R_m_t

        # task calculation
        self.freq_R_m_t = freq_R_m_t
        self.freq_l_m_t = freq_l_m_t
        self.freq_j_m_t = freq_j_m_t


class ActionSpace:
    """
    action space is dedicated to each task (??)
    """

    def __init__(self, lambda_R_m_t, lambda_L_m_t, lambda_V_m_t):
        self.lambda_R_m_t = lambda_R_m_t
        self.lambda_L_m_t = lambda_L_m_t
        self.lambda_V_m_t = lambda_V_m_t
