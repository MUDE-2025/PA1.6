# `./scenarios/door_open.yaml`

```{custom_download_link} door_open.yaml
:text: ".yaml"
:replace_default: "True"
```

```yaml
env:
  base: 8.0
  amplitude: 1.0
  period_s: 5400
  door_drop_C: 25.0
  door_start_s: 900
  door_duration_s: 400

sensor:
  sigma: 0.25
  bias: 0.2
  dropout_prob: 0.03

controller:
  type: predictive_onoff
  setpoint: 21.0
  deadband: 1.0
  tau: 15.0
  safety_high: 26.0

model:
  R: 0.5
  C: 10000.0
  P: 50.0
  process_sigma: 0.0

sim:
  dt: 1.0
  duration_s: 3000.0
  seed: 321
  init_T: 19.0
```