def on_received_number(receivedNumber):
    if receivedNumber == 0:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
    elif receivedNumber == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 10)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 40)
    elif receivedNumber == 2:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 40)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 10)
    elif receivedNumber == 3:
        suivre_ligne()
    else:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 0)
radio.on_received_number(on_received_number)

def suivre_ligne():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 30)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 10)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 10)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 30)
radio.set_group(0)
radio.set_transmit_power(7)
radio.set_frequency_band(0)