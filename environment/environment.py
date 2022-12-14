import numpy

from trajectory_prediction import model
from offloading_env import OffloadingEnvironment
from transitions import Transitions
from DQN import DQN
from config import Config

class Environment:
    """
        A singleton object
    """

    def __init__(self, rsus, mission_vehicles, cooperative_vehicles, tasks, transmissions, timeslots_count):
        # timeslots
        self.timeslots_count = timeslots_count

        # Put a matrix for bandwidths - between each two RSUs
        self.RSUs = rsus

        # vehicles
        self.mission_vehicles = mission_vehicles
        self.cooperative_vehicles = cooperative_vehicles

        # tasks
        self.tasks = tasks

        # adjust numbers
        self.RSU_COUNT = len(self.RSUs)
        self.M = len(mission_vehicles)
        self.J = len(cooperative_vehicles)
        self.TASKS_COUNT = len(self.tasks)

        # coverage matrices
        self.RSU_vehicle_connected = numpy.zeros((self.M, self.RSU_COUNT), int)
        self.mission_cooperative_vehicle_connected = numpy.zeros((self.M, self.J), int)

        # transmissions
        self.transmissions = transmissions

        self.config = Config()

    def read_from_config(self):
        # This method reads environment variables from a config.yml file .
        pass

    def start_execution(self):
        for _ in range(self.timeslots_count):

            self.config.init()
            transitions = Transitions(
                v2v_communication_links_available,
                v2v_communication_links_bandwidth,
                v2r_communication_links_available,
                v2r_communication_links_bandwidth,
                self.tasks, self.cooperative_vehicles
            )
            transitions.compute_delays()
            # Read alpha, betta, w1, d_max from a config file or bash command
            # * Config file is preferred .
            vs = model.VehicleSelection(self.config.vs.alpha, self.config.vs.betta,
                                        self.config.vs.w1, self.config.vs.d_max,
                                        self.mission_vehicles,
                                        self.cooperative_vehicles,
                                        transitions)

            vs.learn_trajectories()
            vs.compute_distances()
            vs.cooperative_vehicle_selection()
            vs.compute_delay()

            # now based on these distances we make an array
            # of candidate cooperative vehicles for each mission vehicle to offload
            # their tasks to . ( the distance must be lower than d_max )
            oe = OffloadingEnvironment()

            # Read lr and gamma from config
            dqn = DQN.DeepQNetwork(self.config.DQN.lr, self.config.DQN.gamma)
            dqn.compute_policy()
