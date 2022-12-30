import yaml
from yaml.loader import SafeLoader


class Config:
    def __init__(self):
        with open('config.yaml') as f:
            data = yaml.load(f, Loader=SafeLoader)

        self.DQN = DQNConfig()
        self.DQN.lr = data["dqn"]["learning_rate"]
        self.DQN.gamma = data["dqn"]["gamma"]

    def init(self):
        pass


class DQNConfig:
    def __init__(self):
        self.lr = 0
        self.gamma = 0


class TransmissionConfig:
    def __init__(self):
        pass


c = Config()
