class Config:
    def __init__(self):
        self.DQN = DQNConfig()

    def init(self):
        pass


class DQNConfig:
    def __init__(self):
        self.lr = 0
        self.gamma = 0

class TransmissionConfig:
    def __init__(self):
        pass