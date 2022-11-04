class RSU:
    def __init__(self, radius):
        self.radius = radius

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
