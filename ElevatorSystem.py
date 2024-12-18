from typing import Callable, Dict, List, Tuple
from Elevator import Elevator
from ElevatorState import ElevatorState

class ElevatorSystem:
    def __init__(self, n_floor: int) -> None:
        self._n_floor = n_floor
        self.elevators: List[Elevator] = []
        self.requests: List[Tuple[int, int]] = []
        self.state_table = self._generate_state_table()

    def _validate_floor(self, floor: int) -> None:
        validation = {
            True: lambda: None,
            False: lambda: (_ for _ in ()).throw(
                ValueError(f"Ошибка! Этаж {floor} вне диапазона (1-{self._n_floor} этажей).")
            )
        }
        validation[1 <= floor <= self._n_floor]()

    def _generate_state_table(self) -> Dict[Tuple[ElevatorState, str], Callable[[Elevator], None]]:
        return {
            (ElevatorState.IDLE, "move_up"): lambda e: self._move(e, 1, ElevatorState.MOVING_UP),
            (ElevatorState.IDLE, "move_down"): lambda e: self._move(e, -1, ElevatorState.MOVING_DOWN),
            (ElevatorState.MOVING_UP, "move_up"): lambda e: self._move(e, 1, ElevatorState.MOVING_UP),
            (ElevatorState.MOVING_DOWN, "move_down"): lambda e: self._move(e, -1, ElevatorState.MOVING_DOWN),
            (ElevatorState.MOVING_UP, "stop"): lambda e: self._stop(e, ElevatorState.IDLE),
            (ElevatorState.MOVING_DOWN, "stop"): lambda e: self._stop(e, ElevatorState.IDLE),
            (ElevatorState.IDLE, "open_door"): lambda e: self._open_door(e),
            (ElevatorState.DOOR_OPEN, "close_door"): lambda e: self._close_door(e),
            (ElevatorState.IDLE, "stop"): lambda e: self._handle_same_floor(e),
        }

    def _handle_same_floor(self, elevator: Elevator) -> None:
        print(f"Лифт #{elevator.elevator_id} уже на нужном этаже {elevator.get_current_floor()}.")
        elevator.state = ElevatorState.IDLE

    def _move(self, elevator: Elevator, increment: int, next_state: ElevatorState) -> None:
        self._validate_floor(elevator.get_current_floor() + increment)
        elevator.increment_floor(increment)
        elevator.state = next_state

    def _stop(self, elevator: Elevator, next_state: ElevatorState) -> None:
        elevator.stop()
        elevator.state = next_state

    def _open_door(self, elevator: Elevator) -> None:
        elevator.open_door()
        elevator.state = ElevatorState.DOOR_OPEN

    def _close_door(self, elevator: Elevator) -> None:
        elevator.close_door()
        elevator.state = ElevatorState.IDLE

    def add_elevator(self, elevator: Elevator) -> None:
        self._validate_floor(elevator.get_current_floor())
        self.elevators.append(elevator)

    def add_request(self, current_floor: int, target_floor: int) -> None:
        self._validate_floor(current_floor)
        self._validate_floor(target_floor)
        self.requests.append((current_floor, target_floor))

    def process_requests(self) -> None:
        for current_floor, target_floor in self.requests:
            elevator = self._find_nearest_elevator(current_floor)
            print(f"\n(Запрос с этажа {current_floor} на этаж {target_floor})")

            while elevator.get_current_floor() != current_floor:
                action = {
                    True: "move_up",
                    False: "move_down"
                }[current_floor > elevator.get_current_floor()]
                self._execute_action(elevator, action)
            self._execute_action(elevator, "stop")
            self._execute_action(elevator, "open_door")
            self._execute_action(elevator, "close_door")

            while elevator.get_current_floor() != target_floor:
                action = {
                    True: "move_up",
                    False: "move_down"
                }[target_floor > elevator.get_current_floor()]
                self._execute_action(elevator, action)
            self._execute_action(elevator, "stop")
            self._execute_action(elevator, "open_door")
            self._execute_action(elevator, "close_door")

    def _execute_action(self, elevator: Elevator, action: str) -> None:
        key = (elevator.state, action)
        try:
            self.state_table[key](elevator)
        except:
            raise KeyError(f"Неверное действие {action} для состояния {elevator.state}")

    def _find_nearest_elevator(self, current_floor: int) -> Elevator:
        return min(self.elevators, key=lambda e: abs(e.get_current_floor() - current_floor))

    def print_movements(self) -> None:
        for elevator in self.elevators:
            print(f"Лифт №{elevator.elevator_id} совершил {elevator.movements} перемещений")
