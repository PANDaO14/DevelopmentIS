from enum import Enum

class ElevatorState(Enum):
    IDLE = "idle"
    MOVING_UP = "moving_up"
    MOVING_DOWN = "moving_down"
    DOOR_OPEN = "door_open"
    DOOR_CLOSED = "door_closed"
