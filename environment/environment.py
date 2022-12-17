import numpy

from trajectory_prediction import model

class Environment:
    """
        A singleton object
    """

    def __init__(self, rsus, mission_vehicles, cooperative_vehicles, tasks, transmissions, timeslots_count):

        #timelots
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

    def start_execution(self):
        for _ in range(self.timeslots_count):
            # Read alpha, betta, w1, d_max from a config file or bash command
            # * Config file is preferred .
            vs = model.VehicleSelection(alpha, betta, w1, d_max,
                                        self.mission_vehicles,
                                        self.cooperative_vehicles)

            # now based on these distances we make an array
            # of candidate cooperative vehilces for each mission vehicle to offload
            # their tasks to . ( the distance must be lower than d_max )