import numpy as np

"""
Write this in Google colab and after you've tried it out ,
paste it here

this is a place for sequential model
"""


class VehicleSelection:

    def __init__(self, alpha, betta, w1, d_max, mission_vehicles, cooperative_vehicles):
        # This class is created at each timeslot .
        self.alpha = alpha
        self.betta = betta
        self.w1 = w1
        self.d_max = d_max
        self.mission_vehicles = mission_vehicles
        self.cooperative_vehicles = cooperative_vehicles

        self.distances = np.zeros((len(mission_vehicles),
                                   len(mission_vehicles)))

        self.connections = np.zeros((len(mission_vehicles),
                                     len(mission_vehicles)))

    # Implementing Algorithm 1
    # Cooperative vehicle selection
    def cooperative_vehicle_selection(self, t_j, d_j, c_j):
        # iterate through cooperative vehicles
        # compute the distances to each one of them --> we have the distances now in self.distances
        # remove them if they are further than D_max --> we have candidates now in self.connections
        # use trajectory prediction to remove them if they are leaving communication range
        eq_12 = np.zeros((len(self.mission_vehicles),
                          len(self.cooperative_vehicles)))
        selected_vehicle = np.zeros((len(self.mission_vehicles)))

        for i in range(len(self.mission_vehicles)):
            for j in range(len(self.cooperative_vehicles)):
                # Decide for computational powers : c_j

                # Compute delay : t_j

                eq_12[i] = self.vehicle_selection_superiority_equation(t_j, d_j, c_j)
            selected_vehicle[i] = eq_12[i].max()

        return selected_vehicle

    def compute_distances(self):
        # We compute distances between all mission vehicles to cooperative vehicles
        # We consider the cooperative vehicles' locations in the next timeslot
        # We predict the locations in the next timeslot by a lightGBM .
        i = 0
        j = 0
        for cv in self.cooperative_vehicles:
            for mv in self.mission_vehicles:
                self.distances[i][j] = self._compute_distance(cv.location, mv.location)

                if self.distances[i][j] <= self.d_max:
                    # This matrix indicates candidate cvs for all msv .
                    self.connections[i][j] = 1

                i += 1
            j += 1

    def vehicle_selection_superiority_equation(self, t_j, d_j, c_j):
        alpha = self.alpha
        betta = self.betta
        w1 = self.w1

        return alpha * c_j - betta * d_j + w1 * t_j

    def learn_trajectories(self):
        # define the model
        # prepare dataset
        # start training the model

        pass

    def _compute_distance(self, cv_location, mv_location):
        return np.linalg.norm(cv_location, mv_location)
