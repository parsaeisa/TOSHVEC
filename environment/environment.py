import numpy as np

from trajectory_prediction import model
# from offloading_env import OffloadingEnvironment
from .transitions import Transitions
from DQN import DQN
from config import Config


class Environment:
    """
        A singleton object
    """

    def __init__(self, rsus, mission_vehicles, cooperative_vehicles, tasks,
                 v2v_communication_links_available,
                 v2v_communication_links_bandwidth,
                 v2r_communication_links_available,
                 v2r_communication_links_bandwidth, timeslots_count):
        print(">>> Initiating environment")
        # timeslots
        self.timeslots_count = timeslots_count

        # Put a matrix for bandwidths - between each two RSUs
        self.RSUs = rsus

        # vehicles
        self.mission_vehicles = mission_vehicles
        self.cooperative_vehicles = cooperative_vehicles

        # tasks
        self.tasks = tasks

        # adjust numbers
        self.RSU_COUNT = len(self.RSUs)
        self.M = len(mission_vehicles)
        self.J = len(cooperative_vehicles)
        self.TASKS_COUNT = len(self.tasks)

        # coverage matrices
        self.RSU_vehicle_connected = np.zeros((self.M, self.RSU_COUNT), int)
        self.mission_cooperative_vehicle_connected = np.zeros((self.M, self.J), int)

        print(">>> Reading configurations")
        self.config = Config()
        self.config.init()

        print(">>> Creating transitions")
        self.transitions = Transitions(
            v2v_communication_links_available,
            v2v_communication_links_bandwidth,
            v2r_communication_links_available,
            v2r_communication_links_bandwidth,
            self.tasks,
            self.config.transition.transmission_power, self.config.transition.channel_gain
        )

    def start_execution(self):
        print(">>> Start execution")
        for _ in range(self.timeslots_count):
            print(">>> Computing delays")
            self.transitions.compute_delays()
            # Read alpha, betta, w1, d_max from a config file or bash command
            # * Config file is preferred .
            vs = model.VehicleSelection(self.config.vs.alpha,
                                        self.config.vs.betta,
                                        self.config.vs.w1,
                                        self.config.vs.d_max,
                                        self.mission_vehicles,
                                        self.cooperative_vehicles)

            print(">>> Selecting best vehicle")
            vs.learn_trajectories()
            vs.compute_distances()
            vs.cooperative_vehicle_selection()
            vs.compute_delay()

            # now based on these distances we make an array
            # of candidate cooperative vehicles for each mission vehicle to offload
            # their tasks to . ( the distance must be lower than d_max )
            # ** I think the class below is not necessary yet
            oe = OffloadingEnvironment()

            # Read lr and gamma from config
            print(">>> Making dqn environment and agent")
            dqn_env = DQN.DeepQEnvironment(self.config.DQN.lr,
                                           self.config.DQN.gamma)

            agent = DQN.DQNAgent(self.config.DQN.replay_buffer_capacity,
                                 self.config.DQN.batch_size,
                                 self.config.DQN.discount_factor)

            print(">>> Running iterations")
            for i in range(self.config.DQN.episodes):

                done = False
                current_state = dqn_env.reset()

                while not done:
                    if np.random.random() > self.config.DQN.epsilon:
                        action = np.argmax(agent.get_qs(current_state))
                    else:
                        action = np.random.randint(0, agent.action_size)

                    next_state, reward, done = dqn_env.step(current_state, action)

                    # episode_reward += reward

                    agent.add_to_replay_memory((current_state, action, reward, next_state, done))
                    agent.train(done)

                    current_state = next_state
                    # If buffer is full , empty it and backward

                # We need a decay epsilon
                # if epsilon > MIN_EPSILON:
                #     epsilon *= EPSILON_DECAY
                #     epsilon = max(MIN_EPSILON, epsilon)
