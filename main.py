import numpy as np

from environment.environment import Environment
from environment.RSU import RSU
from environment.vehicle import MissionVehicle, CooperativeVehicle
from environment.location import Location

rsus = [
    RSU(1000, 100_000),
    RSU(2000, 50_000),
]
mission_vehicles = [
    MissionVehicle(location=Location(12), f=23000),
    MissionVehicle(location=Location(20), f=2000),
    MissionVehicle(location=Location(0), f=20000),
]
cooperative_vehicles = [
    CooperativeVehicle(location=Location(18), f=40000),
    CooperativeVehicle(location=Location(8), f=30000),
    CooperativeVehicle(location=Location(13), f=20000),
]
tasks = []
timeslots_count = 10

v2v_communication_links_available = np.array([[
    [[True, False, True]],
    [[False, True, True]],
    [[False, False, False]],
]])
v2v_communication_links_bandwidth = np.array([
    [[100, 50, 200]],
    [[100, 60, 500]],
    [[200, 70, 500]],
])
v2r_communication_links_available = np.array([
    [[True, False, True]],
    [[False, True, True]],
])
v2r_communication_links_bandwidth = np.array([
    [[100, 50, 400]],
    [[100, 200, 200]],
])

env = Environment(rsus, mission_vehicles, cooperative_vehicles, tasks,
                  v2v_communication_links_available,
                  v2v_communication_links_bandwidth,
                  v2r_communication_links_available,
                  v2r_communication_links_bandwidth,
                  timeslots_count)
