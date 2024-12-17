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

    def move(self, direction: ElevatorDirection) -> None:
        actions = {
            ElevatorDirection.UP: lambda: self._increment_floor(ElevatorDirection.UP),
            ElevatorDirection.DOWN: lambda: self._increment_floor(ElevatorDirection.DOWN, -1)
        }
        actions[direction]()

    def stop(self) -> None:
        self._direction = ElevatorDirection.IDLE
        print(f"Лифт #{self._elevator_id} остановился на этаже {self._current_floor}")

    def open_door(self) -> None:
        print(f"Лифт #{self._elevator_id} открывает двери на этаже {self._current_floor}")

    def close_door(self) -> None:
        print(f"Лифт #{self._elevator_id} закрывает двери на этаже {self._current_floor}")

    def get_movements(self) -> int:
        return self._movements

    def _increment_floor(self, direction: ElevatorDirection, increment: int = 1) -> None:
        direction_description = {
            ElevatorDirection.UP: "поднялся",
            ElevatorDirection.DOWN: "опустился"
        }
        self._current_floor += increment
        self._direction = direction
        self._movements += 1
        print(f"Лифт #{self._elevator_id} {direction_description[direction]} на этаж {self._current_floor}")