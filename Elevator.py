from ElevatorState import ElevatorState 

class Elevator:
    def __init__(self, elevator_id: int, current_floor: int) -> None:
        self._elevator_id = elevator_id
        self._current_floor = current_floor
        self._state = ElevatorState.STOPED

    def get_current_floor(self) -> int:
        return self._current_floor
    
    def get_state(self) -> ElevatorState:
        return self._state
    
    def set_state(self, state: ElevatorState) -> None:
        self._state = state

    def move_up(self) -> None:
        self.set_state(ElevatorState.MOVING_UP)
        self._current_floor += 1
        print(f'Лифт #{self._elevator_id} поднялся на этаж {self._current_floor}')
        self.set_state(ElevatorState.IDLE)
        
    def move_down(self) -> None:
        self.set_state(ElevatorState.MOVING_DOWN)
        self._current_floor -= 1
        print(f'Лифт #{self._elevator_id} спустился на этаж {self._current_floor}')
        self.set_state(ElevatorState.IDLE)
        
    def open_door(self) -> None:
        self.set_state(ElevatorState.DOOR_OPEN)
        print(f'Лифт #{self._elevator_id} открыл дверь')
        
    def close_door(self) -> None:
        self.set_state(ElevatorState.DOOR_CLOSED)
        print(f'Лифт #{self._elevator_id} закрыл дверь')

    def wait(self) -> None:
        self.open_door()
        self.close_door()