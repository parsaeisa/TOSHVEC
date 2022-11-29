# Describing environment
"""
define environment
define transitions' bandwidths
define cooperative vehicles
define mission vehicles

"""
from environment.environment import Environment
from trajectory_prediction.model import VehicleSelection

# Constants
VS_ALPHA =
VS_BETTA =
VS_W1 =
D_max =

env = Environment(rsus,
                  mission_vehicles,
                  cooperative_vehicles,
                  tasks,
                  transmissions
                  )


# Cooperative vehicle selection
vehicle_selection = VehicleSelection(VS_ALPHA , VS_ALPHA , VS_BETTA,D_max)

# DQN
"""
Define a DQN model 
Call a method to choose the best action
Call a transition method to perform that action
Call a method to learn something ( I didn't get that )  
Call a method to store the transitions 

"""