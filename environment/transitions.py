import numpy as np


def offloading_delay_per_task(task, r_mt_j):
    l_m = task.L
    t_comm = l_m / r_mt_j

    return t_comm


def _offloading_delays(available, bandwidths, delays, trans_rates, tasks):

    # origins are always mission vehicles
    destinations_count, origins_count = bandwidths.shape()

    for destination_index in range(destinations_count):
        for origin_index in range(origins_count):

            if not available[destination_index, origin_index]:
                continue

            for task_index in range(len(tasks)):
                r_mt_j = trans_rates[destination_index, origin_index]

                delays[destination_index, origin_index, task_index] = \
                    offloading_delay_per_task(
                        tasks[task_index], r_mt_j
                    )
    return delays


class Transitions:
    def __init__(self, v2v_communication_links_available,
                 v2v_communication_links_bandwidth,
                 v2r_communication_links_available,
                 v2r_communication_links_bandwidth,
                 tasks,
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

        mission_vehicles_count, cooperative_vehicles_count = self.v2v_communication_links_bandwidth.shape()
        self.v2v_comm_delay = np.zeros(
            (mission_vehicles_count, cooperative_vehicles_count, len(self.tasks))
        )

        mission_vehicles_count, rsu_count = self.v2r_communication_links_bandwidth.shape()
        self.v2r_comm_delay = np.zeros(
            (mission_vehicles_count, rsu_count, len(self.tasks))
        )

        self.mission_vehicles_count = mission_vehicles_count

    def compute_delays(self):
        self.compute_transmission_rates()

        v2r_delays = self.offloading_to_rsu_delay()
        v2v_delays = self.v2v_offloading_delays()

        return v2r_delays, v2v_delays

    # V2R
    def offloading_to_rsu_delay(self):
        return _offloading_delays(self.v2r_communication_links_bandwidth, self.v2r_comm_delay, self.v2r_communication_links_trans_rate,
                                       self.tasks)

    def backhaul_link_delay(self):
        pass

    # V2V
    def v2v_offloading_delays(self):
        return _offloading_delays(self.v2v_communication_links_bandwidth, self.v2v_comm_delay, self.v2v_communication_links_trans_rate,
                                       self.tasks)

    def compute_transmission_rates(self):

        interference = self.compute_interference_V2R()
        gaus_noise = 0

        # Equation 1 in the paper
        # P is transmission power
        # G is the channel gain to RSU 1
        self.v2r_communication_links_trans_rate = self.v2r_communication_links_bandwidth *\
                                                  np.log2(1 + np.divide(self.P * self.G, gaus_noise + interference))
        self.v2v_communication_links_trans_rate = self.v2v_communication_links_bandwidth *\
                                                  np.log2(1 + np.divide(self.P * self.G, gaus_noise + interference))

    def compute_interference_V2R(self):
        """
        Interference is the sum of ( transmission power * channel gain ) in mission vehicles except the
        current mission vehicle
        """

        return (self.mission_vehicles_count - 1) * self.G * self.P
