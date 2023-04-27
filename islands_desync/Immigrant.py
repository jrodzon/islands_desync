class Immigrant:
    def __init__(self, iteration, native_island, state):
        self.iteration = iteration
        self.state = state
        self.native_island = native_island

    def get_iteration(self):
        return self.iteration

    def increment_iteration(self):
        self.iteration += 1

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def __str__(self):
        return "Osobnik urodzony na wyspie %s o iteracji %s" % (
            self.native_island,
            self.iteration,
        )

    def __repr__(self):
        return "Osobnik urodzony na wyspie %s o iteracji %s" % (
            self.native_island,
            self.iteration,
        )
