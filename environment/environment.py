class Environment:
    def __init__(self, rsus, mission_vehicles, cooperative_vehicles, tasks):
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