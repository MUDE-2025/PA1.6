from dataclasses import dataclass
from typing import Optional
from utils.rng import RNG

@dataclass
class TempSensor:
    sigma: float = 0.2
    bias: float = 0.3
    dropout_prob: float = 0.02
    rng: Optional[RNG] = None

    def read(self, true_temp: float) -> Optional[float]:
        ''' Simulate a temperature sensor reading with Gaussian noise, bias, and dropout.
            true_temp: The actual temperature to be measured.
            Returns the noisy temperature reading, or None if the sensor drops out.
        '''

        # --- Student code starts here ---
        # Hint: Use the functions self.rng.gauss and self.rng.bernoulli

        # --- Student code ends here ---
        
        return 0.0 # remove when code is added
