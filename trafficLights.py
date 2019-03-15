from statemachine import StateMachine, State

class TrafficLightMachine(StateMachine):
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Red')

    slowdown = green.to(yellow)
    stop = yellow.to(red)
    go = red.to(green)
    
traffic_light = TrafficLightMachine()

#traffic_light.current_state