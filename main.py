from environment.environment import Environment
from environment.RSU import RSU
from environment.vehicle import MissionVehicle, CooperativeVehicle
from environment.location import Location

rsus = [RSU(1000, 100_000)]
mission_vehicles = [MissionVehicle(location=Location(12), f=23000)]
cooperative_vehicles = [CooperativeVehicle(location=Location(18), f=40000)]
tasks = []
transmissions = []
timeslots_count = 10

env = Environment(rsus, mission_vehicles, cooperative_vehicles, tasks, transmissions,
                  timeslots_count)