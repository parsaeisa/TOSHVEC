"""
Write this in Google colab and after you've tried it out ,
paste it here

this is a place for sequential model
"""


class VehicleSelection:

    def __init__(self, alpha, betta, w1, d_max):
        self.alpha = alpha
        self.betta = betta
        self.w1 = w1
        self.d_max = d_max

    # Implementing Algorithm 1
    # Cooperative vehicle selection
    def cooperative_vehicle_selection(self, t_j, d_j, c_j):
        # iterate through cooperative vehicles
        # compute the distances to each one of them
        # remove them if they are further than D_max
        # use trajectory prediction to remove them if they are leaving communication range

        # Now we have candidates
        # Choose the best one according to Eq 12
        pass

    def vehicle_selection_superiority_equation(self , t_j, d_j, c_j):
        alpha = self.alpha
        betta = self.betta
        w1 = self.w1

        return alpha*c_j - betta * d_j + w1 * t_j
