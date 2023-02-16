import numpy as np


def offloading_delay(task, r_mt_j):
    l_m = task.L

    t_comm = l_m / r_mt_j

    return t_comm


class Transitions:
    def __init__(self, v2v_communication_links_available,
                 v2v_communication_links_bandwidth,
                 v2r_communication_links_available,
                 v2r_communication_links_bandwidth,
                 tasks, cooperative_vehicles,
                 transmission_power, channel_gain):
        self.v2v_communication_links_available = v2v_communication_links_available
        self.v2v_communication_links_bandwidth = v2v_communication_links_bandwidth
        self.v2v_communication_links_trans_rate = np.zeros_like(v2v_communication_links_bandwidth.shape())

        self.v2r_communication_links_available = v2r_communication_links_available
        self.v2r_communication_links_bandwidth = v2r_communication_links_bandwidth
        self.v2r_communication_links_trans_rate = np.zeros_like(v2r_communication_links_bandwidth.shape())
        # Transmission rates are computed based on bandwidth
        # Transmission rates are being used in practice .

        self.P = transmission_power
        self.G = channel_gain

        self.tasks = tasks
        self.cooperative_vehicles = cooperative_vehicles
        mission_vehicles_count, cooperative_vehicles_count = self.v2v_communication_links_bandwidth.shape()

        self.v2v_comm_delay = np.zeros(
            (mission_vehicles_count, cooperative_vehicles_count, len(self.tasks))
        )

        mission_vehicles_count, rus_count = self.v2r_communication_links_bandwidth.shape()
        self.v2r_comm_delay = np.zeros(
            (mission_vehicles_count, cooperative_vehicles_count, len(self.tasks))
        )

    def compute_delays(self):
        self.compute_transmission_rates()

        self.offloading_to_rsu_delay()

        self.v2v_offloading_delays()

    # V2R
    def offloading_to_rsu_delay(self):
        self._offloading_delays(self.v2r_communication_links_bandwidth, self.v2r_comm_delay)

    def backhaul_link_delay(self):
        pass

    # V2V
    def v2v_offloading_delays(self):
        self._offloading_delays(self.v2v_communication_links_bandwidth, self.v2v_comm_delay)

    # Shared
    def _offloading_delays(self, bandwidths, delays):
        # don't forget to consider available links

        mission_vehicles_count, cooperative_vehicles_count = bandwidths.shape()

        for mission_vehicle_index in range(mission_vehicles_count):
            for cooperative_vehicle_index in range(cooperative_vehicles_count):

                for task_index in range(len(self.tasks)):
                    r_mt_j = self.v2v_communication_links_trans_rate[mission_vehicle_index, cooperative_vehicle_index]

                    delays[mission_vehicle_index, cooperative_vehicle_index, task_index] = \
                        offloading_delay(
                            self.tasks[task_index], r_mt_j
                        )

    def compute_transmission_rates(self):
        # self.v2v_communication_links_trans_rate should be made here
        # is v2v and v2r formulation the same ?

        interference = self.compute_interference_V2R()
        bandwidths = self.v2r_communication_links_bandwidth
        gaus_noise = 0

        # Equation 1 in the paper
        # P is transmission power
        # G is the channel gain to RSU 1
        r = bandwidths * np.log2(1 + np.divide(self.P * self.G, gaus_noise + interference))
        return r

    def compute_interference_V2R(self):
        pass
