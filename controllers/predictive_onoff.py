from dataclasses import dataclass

@dataclass
class PredictiveOnOff:
    setpoint: float
    deadband: float
    tau: float = 10.0         # lookahead horizon (seconds)
    safety_high: float = 26.0
    state: int = 0            # 0=OFF, 1=ON

    # Exposed diagnostics for plotting/logging
    last_meas: float | None = None
    last_pred: float | None = None
    lower_threshold: float | None = None
    upper_threshold: float | None = None

    def update(self, meas_filtered: float, dt: float) -> int:
        ''' Update the thermostat state based on the measured temperature and a prediction.
            If the predicted temperature (based on current trend) is below the lower threshold
            (setpoint - deadband/2), the thermostat turns ON (state=1).
            If the predicted temperature is above the upper threshold (setpoint + deadband/2),
            the thermostat turns OFF (state=0).
            If the measured temperature exceeds the safety_high limit, the thermostat turns OFF.
            meas_filtered: The current filtered/measured temperature.
            dt: Time difference since last update (seconds).
            Returns the current state (0=OFF, 1=ON).
        '''
        # --- Student code starts here ---
        ## hint: Predict the temperature tau seconds into the future using a discrete derivative.

        # --- Student code ends here ---

        return self.state

    def _update_diag(self, meas: float, dt: float, T_pred: float, lower: float | None = None, upper: float | None = None):
        ''' Update diagnostic variables for logging/plotting. 
            This includes the last measured temperature, the last predicted temperature,
            and the current lower and upper thresholds based on setpoint and deadband.
        '''
        
        # --- Student code starts here ---

        # --- Student code ends here ---

        pass # remove when code is added
