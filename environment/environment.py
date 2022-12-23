import numpy

from trajectory_prediction import model
from offloading_env import OffloadingEnvironment
from transitions import Transitions

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

    def read_from_config(self):
        # This method reads environment variables from a config.yml file .
        pass

    def start_execution(self):
        for _ in range(self.timeslots_count):

            self.read_from_config()
            transitions = Transitions(
                v2v_communication_links_available,
                v2v_communication_links_bandwidth,
                v2r_communication_links_available,
                v2r_communication_links_bandwidth,
                self.tasks, self.cooperative_vehicles
            )
            # Read alpha, betta, w1, d_max from a config file or bash command
            # * Config file is preferred .
            vs = model.VehicleSelection(alpha, betta, w1, d_max,
                                        self.mission_vehicles,
                                        self.cooperative_vehicles,
                                        transitions)
            # Here you should call some of vs's methods
            vs.learn_trajectories()
            vs.compute_distances()
            vs.cooperative_vehicle_selection()
            vs.compute_delay()

            # now based on these distances we make an array
            # of candidate cooperative vehicles for each mission vehicle to offload
            # their tasks to . ( the distance must be lower than d_max )
            oe = OffloadingEnvironment()
