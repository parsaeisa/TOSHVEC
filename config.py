import yaml
from yaml.loader import SafeLoader


class Config:

    def init(self):
        with open('config.yaml') as f:
            data = yaml.load(f, Loader=SafeLoader)

        self.DQN = DQNConfig()
        self.DQN.lr = data["dqn"]["learning_rate"]
        self.DQN.gamma = data["dqn"]["gamma"]

        self.vs = VehicleSelectionConfig()
        self.vs.alpha = data["vehicle_selection"]["alpha"]
        self.vs.betta = data["vehicle_selection"]["betta"]
        self.vs.w1 = data["vehicle_selection"]["w1"]
        self.vs.d_max = data["vehicle_selection"]["d_max"]

        self.betta_l = data["energy_consumption"]["local"]
        self.betta_r = data["energy_consumption"]["rsu"]
        self.betta_v = data["energy_consumption"]["vehicle"]


class DQNConfig:
    def __init__(self):
        self.lr = 0
        self.gamma = 0


class TransmissionConfig:
    def __init__(self):
        pass


class VehicleSelectionConfig:
    def __init__(self):
        self.alpha = 0
        self.betta = 0
        self.w1 = 0
        self.d_max = 0
