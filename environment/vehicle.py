class Vehicle:
    """
    computation power : in CPU cycle
    energy
    location : lat , lng
    transmission rate , should it be here ??
    """

    def __init__(self , location):
        self.location = location

class MissionVehicle(Vehicle):
    """
        System configs :
        bandwidth =
        cpu power ( frequency ) =
    """

    def __init__(self,f):
        super(MissionVehicle, self).__init__()
        # vehicles; CPU frequency
        self.f = f

    def process_task(self):
        """
        In this method , RSU's available resources is updated .
        A task's cpu cycles is subtracted from RSU's cpu cycles .
        :return:
        """
        pass

    def task_deallocate(self):
        pass


class CooperativeVehicle(Vehicle):
    def __init__(self):
        super(CooperativeVehicle, self).__init__()

    def generate_task_randomly(self):
        pass

    def offload(self):
        pass

    def _offload_to_RSU(self):
        pass

    def _offload_to_mission_vehicle(self):
        pass

    def _execute_locally(self):
        pass