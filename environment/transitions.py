
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
