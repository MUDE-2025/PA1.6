from typing import Optional

def hold_last(value: Optional[float], last: Optional[float]) -> Optional[float]:
    return last if value is None else value

class MovingAverageFilter:
    def __init__(self, window: int = 5):
        assert window >= 1
        self.window = window
        self.buf = []
        self.sum = 0.0

    def update(self, x: float) -> float:
        ''' Update the moving average filter with a new value x.
            Returns the current filtered value.
        '''
        # --- Student code starts here ---

        # --- Student code ends here ---
        return 0.0 # remove when code is added
