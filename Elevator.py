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

    def up(self) -> None:
        actions = {
            True: lambda: self._move_up(),
            False: lambda: self._raise_error("Ошибка! Нельзя двигаться выше текущего этажа, так как он самый последний сверху!")
        }
        actions[self._current_floor >= 1]()

    def _move_up(self) -> None:
        self._current_floor += 1
        self._direction = ElevatorDirection.UP
        self._movements += 1
        print(f"Лифт #{self._elevator_id} поднялся на этаж {self._current_floor}")

    def down(self) -> None:
        actions = {
            True: lambda: self._move_down(),
            False: lambda: self._raise_error("Ошибка! Нельзя двигаться ниже текущего этажа, так как он самый последний снизу!")
        }
        actions[self._current_floor > 1]()

    def _move_down(self) -> None:
        self._current_floor -= 1
        self._direction = ElevatorDirection.DOWN
        self._movements += 1
        print(f"Лифт #{self._elevator_id} опустился на этаж {self._current_floor}")

    def _raise_error(self, message: str) -> None:
        raise ValueError(message)

    def stop(self) -> None:
        self._direction = ElevatorDirection.IDLE
        print(f"Elevator #{self._elevator_id} остановился на этаже {self._current_floor}")

    def open_door(self) -> None:
        print(f"Лифт #{self._elevator_id} открыл свои двери")

    def close_door(self) -> None:
        print(f"Лифт #{self._elevator_id} закрыл свои двери")

    def get_movements(self) -> int:
        return self._movements
