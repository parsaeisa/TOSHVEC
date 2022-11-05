class OffloadingEnvironment:
    def __init__(self):
        pass

    # solutions
    def cooperative_selection(self):
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

    def transmission_time(self, rsu, m, bw):
        """
        :param rsu:
        :param m: the task which is transmitted
        :param bw: bandwidth between RSU and vehicle
        :return: transmission time
        """
        tt = m.L / bw
        return tt

    def computation_time(self, task, rsu):
        ct = task.C / rsu.f
        return ct

    def transmission_rate(self, bR, I_V2R):
        # equation 1 in paper
        pass

