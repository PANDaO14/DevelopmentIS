from enum import Enum

class ElevatorState(Enum):
    STOPED = 0
    MOVING_UP = 1
    MOVING_DOWN = 2
    DOOR_OPEN = 3
    DOOR_CLOSED = 4