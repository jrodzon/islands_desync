class Immigrant:
    def __init__(self, iteration, state):
        self.iteration = iteration
        self.state = state

    def get_iteration(self):
        return self.iteration

    def increment_iteration(self):
        self.iteration += 1

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
