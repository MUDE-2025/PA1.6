from simulations.room_model import step_room

def test_heater_warms_room():
    T = 18.0
    T_out = 10.0
    R, C, P, dt = 0.5, 10000.0, 200.0, 1.0
    T1 = step_room(T, heater_on=0, T_out=T_out, R=R, C=C, P=P, dt=dt)
    T2 = step_room(T, heater_on=1, T_out=T_out, R=R, C=C, P=P, dt=dt)
    assert T2 > T1
