from ElevatorDirection import ElevatorDirection 

class Elevator:
    def __init__(self, elevator_id: int, current_floor: int) -> None:
        self._elevator_id = elevator_id
        self._current_floor = current_floor
        self._direction = ElevatorDirection.IDLE
        self._movements = 0

    def get_current_floor(self) -> int:
        return self._current_floor

    def get_direction(self) -> ElevatorDirection:
        return self._direction

    def moveUp(self) -> None:
        self._current_floor += 1
        self._direction = ElevatorDirection.UP
        self._movements += 1
        print(f"Лифт #{self._elevator_id} поднялся на этаж {self._current_floor}")

    def moveDown(self) -> None:
        self._current_floor -= 1
        self._direction = ElevatorDirection.DOWN
        self._movements += 1
        print(f"Лифт #{self._elevator_id} опустился на этаж {self._current_floor}")

    def stop(self) -> None:
        self._direction = ElevatorDirection.IDLE
        print(f"Лифт #{self._elevator_id} остановился на этаже {self._current_floor}")

    def open_door(self) -> None:
        print(f"Лифт #{self._elevator_id} открывает свои двери")

    def close_door(self) -> None:
        print(f"Лифт #{self._elevator_id} закрывает свои двери")

    def get_movements(self) -> int:
        return self._movements