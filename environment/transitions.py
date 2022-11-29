import numpy as np


class Transitions:
    def __init__(self, v2v_communication_links_available,
                 v2v_communication_links_bandwidth,
                 v2v_communication_links_trans_rate,
                 v2r_communication_links_available,
                 v2r_communication_links_bandwidth,
                 v2r_communication_links_trans_rate):
        self.V2V0_communication_links_available = v2v_communication_links_available
        self.V2V0_communication_links_bandwidth = v2v_communication_links_bandwidth
        self.v2v_communication_links_trans_rate = v2v_communication_links_trans_rate

        self.V2R_communication_links_available = v2r_communication_links_available
        self.V2R_communication_links_bandwidth = v2r_communication_links_bandwidth
        self.v2r_communication_links_trans_rate = v2r_communication_links_trans_rate

    def compute_transmission_rates(self):
        interference = compute_interference_V2R()
        bandwidths = self.V2R_communication_links_bandwidth

        # Equation 1 in the paper
        r = np.power(bandwidths, R) + np.log2(1 + np.divide(P * G, gaus_noise + interference))
        return r

    def offloading_to_rsu_delay(self):
        pass

    def offloading_to_cooperative_vehicle_delay(self,task, cooperative_vehicle):
        L_m =
        r_mt_j =

        T_comm = L_m / r_mt_j
        T_comp = task.C / cooperative_vehicle.f

        T_total = T_comm + T_comp
        return T_total

    def processing_locally_delay(self,task, mission_vehicle):
        return task.C / mission_vehicle.f


def compute_interference_V2R():
    pass
