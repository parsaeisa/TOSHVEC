class Vehicle:
    """
    computation power : in CPU cycle
    energy
    location : lat , lng
    transmission rate , should it be here ??
    """

    def __init__(self, location, f):
        self.location = location

        # vehicles; CPU frequency
        self.f = f

    def task_allocation(self, task):
        """
        In this method , RSU's available resources is updated .
        A task's cpu cycles is subtracted from RSU's cpu cycles .
        :return:
        """
        self.f -= task.C

    def task_deallocate(self, task):
        self.f += task.C

    def task_process_delay(self, task):
        return task.C / self.f


class MissionVehicle(Vehicle):
    """
        System configs :
        bandwidth =
        cpu power ( frequency ) =
    """

    def __init__(self):
        super(MissionVehicle, self).__init__()


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

    def _execute_locally(self, task):
        self.task_allocation(task)
