# `./tests/test_onoff.py`

```{custom_download_link} test_onoff.py
:text: ".py"
:replace_default: "True"
```

```python
from controllers.onoff import OnOffThermostat

def test_on_below_lower():
    t = OnOffThermostat(setpoint=21.0, deadband=1.0)
    t.state = 0
    assert t.update(20.4) == 1

def test_off_above_upper():
    t = OnOffThermostat(setpoint=21.0, deadband=1.0)
    t.state = 1
    assert t.update(21.6) == 0

def test_hold_inside_band():
    t = OnOffThermostat(setpoint=21.0, deadband=1.0)
    t.state = 1
    assert t.update(21.0) == 1
    t.state = 0
    assert t.update(21.0) == 0

def test_safety_cutoff():
    t = OnOffThermostat(setpoint=21.0, deadband=1.0, safety_high=25.0)
    t.state = 1
    assert t.update(25.0) == 0
```