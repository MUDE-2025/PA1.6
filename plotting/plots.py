import os
from typing import Dict, List
import matplotlib.pyplot as plt

def _ensure_dir(path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def plot_timeseries(log: Dict[str, List[float]], out_path: str):
    ''' Plot the time series of temperatures and thresholds. 
        log: A dictionary containing time series data with keys:
            - "t": time points
            - "T_true": true temperature
            - "T_meas": measured/filtered temperature
            - "T_out": outdoor temperature
            - "lower": lower threshold (optional value)
            - "upper": upper threshold (optional value)
            - "setpoint": setpoint temperature
        out_path: Path to save the output plot image.
    '''
    _ensure_dir(out_path) # ensure output directory exists
    
    # --- Student code starts here ---

    # --- Student code ends here ---


def plot_heater(log: Dict[str, List[float]], out_path: str):
    ''' Plot the heater state over time.
        log: A dictionary containing time series data with keys:
            - "t": time points
            - "heater": heater state (0=OFF, 1=ON)
        out_path: Path to save the output plot image.
    '''
    
    _ensure_dir(out_path) # ensure output directory exists
    
    # --- Student code starts here ---

    # --- Student code ends here ---

def plot_error(log: Dict[str, List[float]], out_path: str):
    ''' Plot the tracking error (setpoint - measured temperature) over time.
        log: A dictionary containing time series data with keys:
            - "t": time points
            - "error": tracking error (setpoint - measured temperature)
        out_path: Path to save the output plot image.
    '''
    _ensure_dir(out_path) # ensure output directory exists

    # --- Student code starts here ---

    # --- Student code ends here ---
    

def plot_duty(log: Dict[str, List[float]], out_path: str, window:int=60):
    ''' Plot the rolling duty cycle of the heater over time.
        log: A dictionary containing time series data with keys:
            - "t": time points
            - "heater": heater state (0=OFF, 1=ON)
        out_path: Path to save the output plot image.
        window: Size of the rolling window in seconds for duty cycle calculation.
    '''
    _ensure_dir(out_path) # ensure output directory exists
    
    # --- Student code starts here ---
    ## hint: Use a rolling window to compute the duty cycle.

    # --- Student code ends here ---

def plot_predictive(log: Dict[str, List[float]], out_path: str):
    ''' Plot the predictive control diagnostics including measured temperature,
        predicted temperature, and thresholds over time.
        log: A dictionary containing time series data with keys:
            - "t": time points
            - "T_meas": measured/filtered temperature
            - "T_pred": predicted temperature (optional)
            - "lower": lower threshold (optional)
            - "upper": upper threshold (optional)
        out_path: Path to save the output plot image.
    '''
    _ensure_dir(out_path) # ensure output directory exists
    
    # --- Student code starts here ---

    # --- Student code ends here ---
