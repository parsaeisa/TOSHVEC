class RSU:
    """
    System configs :
    bandwidth =
    cpu power ( frequency ) =
    """
    def __init__(self, radius, cpu_cycles):
        self.radius = radius
        self.cpu_cycles = cpu_cycles

    def process_task(self,  task):
        """
        In this method , RSU's available resources is updated .
        A task's cpu cycles is subtracted from RSU's cpu cycles .
        :return:
        """
        self.cpu_cycles -= task.C

    def task_deallocate(self, task):
        self.cpu_cycles += task.C

    # Computation costs
    # this is used when deciding about offloading scheme
    # execute locally or offload ??
    def locally_execution_cost(self, data):
        return self._computation_cost(data, self.mobile_process_capable)

    def mec_execution_cost(self, data):
        return self._computation_cost(data, self.mec_process_capble)

    def _computation_cost(self, data, processing_power):
        computation_time = data / processing_power

        return computation_time

    # Transmission cost
    # the transmission cost is used to decide whether offload or not ?
    # The offloading time may exceed the task deadline .
    # And if scheme is offloading , offload it to RSU or cooperative vehicles ?
    def up_transmission_cost(self, data, distance=0.0):
        #PLDbm = 128.1 + 37.6 * np.log10(distance / 1000.0)
        #PLw = 10.0 ** ((PLDbm) / 10.0)

        #rate = self.bandwith_up * np.log2( 1 + self.Pap * PLw / (self.bandwith_up * self.omega0))

        # rate = 7.0 * (1024.0 * 1024.0 / 8.0)
        rate = self.bandwith_up * (1024.0 * 1024.0 / 8.0)

        transmission_time = data / rate

        return transmission_time

    def reset(self):
        self.mec_process_avaliable_time = 0.0
        self.mobile_process_avaliable_time = 0.0

    def dl_transmission_cost(self, data, distance=0.0):
        #PLDbm = 128.1 + 37.6 * np.log10( distance / 1000.0)
        #PLw = 10.0 ** ((PLDbm) / 10.0)

        #rate = self.bandwith_dl * np.log2(1 + self.Pap * PLw / (self.bandwith_dl * self.omega0))

        rate = self.bandwith_dl * (1024.0 * 1024.0 / 8.0)
        transmission_time = data / rate

        return transmission_time
