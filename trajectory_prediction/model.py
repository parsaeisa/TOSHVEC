import numpy as np
import lightgbm as lgb

"""
Write this in Google colab and after you've tried it out ,
paste it here

this is a place for sequential model
"""


def _compute_distance(cv_location, mv_location):
    return np.linalg.norm(cv_location, mv_location)


class VehicleSelection:

    def __init__(self, alpha, betta, w1, d_max, mission_vehicles, cooperative_vehicles, transitions):
        # This class is created at each timeslot .
        self.location_next_ts = None
        self.alpha = alpha
        self.betta = betta
        self.w1 = w1
        self.d_max = d_max
        self.mission_vehicles = mission_vehicles
        self.cooperative_vehicles = cooperative_vehicles

        self.distances = np.zeros((len(mission_vehicles),
                                   len(cooperative_vehicles)))

        # This shows candidate cooperative vehicles for each mission vehicle
        self.connections = np.zeros((len(mission_vehicles),
                                     len(cooperative_vehicles)))

        self.transitions = transitions

    # Implementing Algorithm 1
    # Cooperative vehicle selection
    def cooperative_vehicle_selection(self):
        # use trajectory prediction to remove them if they are leaving communication range
        eq_12 = np.zeros((len(self.mission_vehicles),
                          len(self.cooperative_vehicles)))
        selected_vehicle = np.zeros((len(self.mission_vehicles)))

        for i in range(len(self.mission_vehicles)):
            for j in range(len(self.cooperative_vehicles)):

                if self.connections[i, j] != 1:
                    # means that this cv is not a candidate for the specific mv
                    continue

                c_j = self.mission_vehicles[i].f
                t_j = self.transitions.v2v_comm_delay[i, j, ]
                d_j = self.distances[i, j]

                eq_12[i] = self.vehicle_selection_superiority_equation(t_j, d_j, c_j)
            selected_vehicle[i] = eq_12[i].max()

        return selected_vehicle

    def vehicle_selection_superiority_equation(self, t_j, d_j, c_j):
        alpha = self.alpha
        betta = self.betta
        w1 = self.w1

        return alpha * c_j - betta * d_j + w1 * t_j

    def compute_distances(self):
        # We compute distances between all mission vehicles to cooperative vehicles
        # We consider the cooperative vehicles' locations in the next timeslot
        # We predict the locations in the next timeslot by a lightGBM .
        i = 0
        j = 0
        for cv in self.cooperative_vehicles:
            for mv in self.mission_vehicles:
                # The location below is actually their location in the next timeslot.
                self.distances[i][j] = _compute_distance(cv.location, mv.location)

                if self.distances[i][j] <= self.d_max:
                    # This matrix indicates candidate cvs for all msv .
                    self.connections[i][j] = 1

                i += 1
            j += 1

    def compute_delay(self):
        # The delay is computed inside of vehicles .
        # Here we just call the method
        pass

    def learn_trajectories(self):
        model = lgb.LGBMClassifier()

        # import dataset
        # The input is current location and the output is next location

        # start training the model
        model.fit(x_train, y_train)

        self.location_next_ts = model.predict(current_locations)
