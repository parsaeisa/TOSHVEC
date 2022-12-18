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
    def compute_task_latency(self, task):
        """
        compute a task latency T1, if T1 is bigger than task deadline --> offload
        :return:
        """
        pass

    # metrics
    # We should decide what to do here . ( process locally , offload to RSU or to a cooperative vehicle )
