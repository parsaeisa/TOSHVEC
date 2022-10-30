class Task:
    """
        L : size of task
        C : CPU cycles
        x : location of vehicle when task is generated .
        T : deadline
    """

    def __init__(self, L, C, x, T):
        self.L = L
        self.C = C
        self.x = x
        self.T = T
