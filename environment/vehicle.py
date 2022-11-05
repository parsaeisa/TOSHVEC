class Vehicle:
    """
    computation power : in CPU cycle
    energy
    location : lat , lng
    transmission rate , should it be here ??
    """

    def __init__(self , location):
        self.location = location

    def generate_task_randomly(self):
        pass

    def offload(self):
        pass


class MissionVehicle(Vehicle):
    def __init__(self):
        super(MissionVehicle, self).__init__()


class CooperativeVehicle(Vehicle):
    def __init__(self):
        super(CooperativeVehicle, self).__init__()
