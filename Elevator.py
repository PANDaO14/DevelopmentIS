from ElevatorState import ElevatorState 

class Elevator:
    def __init__(self, elevator_id: int, current_floor: int) -> None:
        self.elevator_id = elevator_id
        self._current_floor = current_floor
        self.movements = 0
        self.state = ElevatorState.IDLE

    def get_current_floor(self) -> int:
        return self._current_floor
        
    def increment_floor(self, increment: int) -> None:
        self._current_floor += increment
        self.movements += 1
        print(f"Лифт №{self.elevator_id} переместился на этаж {self._current_floor}")

    def open_door(self) -> None:
        print(f"Лифт №{self.elevator_id} открыл двери на этаже {self._current_floor}")

    def close_door(self) -> None:
        print(f"Лифт №{self.elevator_id} закрыл двери на этаже {self._current_floor}")

    def stop(self) -> None:
        print(f"Лифт №{self.elevator_id} остановился на этаже {self._current_floor}")
