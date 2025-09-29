from numpy.random import default_rng

class RNG:
    def __init__(self, seed: int):
        self.rng = default_rng(seed)

    def gauss(self, mu: float, sigma: float) -> float:
        ''' Return a random float following a Gaussian distribution with mean mu and standard deviation sigma. '''
        # --- Student code starts here ---

        return 0.0 # remove when code is added
        # --- Student code ends here ---

    def uniform(self, a: float, b: float) -> float:
        ''' Return a random float in the range [a, b) following a uniform distribution. '''
        # --- Student code starts here ---

        return 0.0 # remove when code is added
        # --- Student code ends here ---

    def bernoulli(self, p: float) -> bool:
        ''' Return True with probability p, False with probability 1-p. '''

        # --- Student code starts here ---

        return False # remove when code is added
        # --- Student code ends here ---
