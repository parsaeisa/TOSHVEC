class OffloadingEnvironment:
    def __init__(self):
        pass

    # solutions
    def cooperative_selection(self):
        # there is another vehicle selection ( class )
        # which is newer and we gonna use that .
        # This vehicle selection is performed in each timeslot
        pass

    def server_selection(self):
        pass

    # parameters
    def process_locally(self, task, mission_vehicle):
        """
        compute a task latency T1, if T1 is bigger than task deadline --> offload
        :return:
        """
        delay = self.processing_locally_delay(task,mission_vehicle)
        if delay > task.T:
            return False
        else:
            return True

    def processing_locally_delay(self, task, mission_vehicle):
        return task.C / mission_vehicle.f

    # metrics
    # We should decide what to do here . ( process locally , offload to RSU or to a cooperative vehicle )
    # I think this is the place that we should employ DQN .
