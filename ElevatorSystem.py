from typing import Callable, Dict, List, Tuple
from Elevator import Elevator
from ElevatorDirection import ElevatorDirection

class ElevatorSystem:
    def __init__(self, n_floor: int) -> None:
        self._elevators: List[Elevator] = []
        self._n_floor = n_floor
        self._requests: List[Tuple[int, str, int]] = []
        self.table = self._generate_table()

    def _validate_floor(self, floor: int) -> None:
        validation = {
            True: lambda: None,
            False: lambda: (_ for _ in ()).throw(
                ValueError(f"Ошибка! Этаж {floor} вне диапазона (1-{self._n_floor} этажей).")
            )
        }
        validation[1 <= floor <= self._n_floor]()

    def _generate_table(self) -> Dict[Tuple[str, str], Callable[[Elevator], None]]:
        actions = {
            "open": lambda e: e.open_door(),
            "close": lambda e: e.close_door(),
            "moveUp": lambda e: e.move(ElevatorDirection.UP),
            "moveDown": lambda e: e.move(ElevatorDirection.DOWN),
            "stop": lambda e: e.stop(),
            "sameFloor": lambda e: self._handle_same_floor(e),
        }

        return {
            (direction, action): func
            for direction in ["idle", "up", "down"]
            for action, func in actions.items()
        }

    def _handle_same_floor(self, elevator: Elevator) -> None:
        print(f"Лифт #{elevator._elevator_id} уже на нужном этаже {elevator.get_current_floor()}.")
        elevator.open_door()
        elevator.close_door()

    def add_elevator(self, elevator: Elevator) -> None:
        self._validate_floor(elevator.get_current_floor())
        self._elevators.append(elevator)

    def add_request(self, current_floor: int, direction: str, target_floor: int) -> None:
        self._validate_floor(current_floor)
        self._validate_floor(target_floor)
        self._requests.append((current_floor, direction, target_floor))

    def process_requests(self) -> None:
        for request in self._requests:
            current_floor, direction, target_floor = request
            elevator = self._find_nearest_elevator(current_floor)
            print(f"Запрос (с {current_floor} по {target_floor})")
            self._execute_actions(elevator, current_floor, target_floor)

    def _find_nearest_elevator(self, current_floor: int) -> Elevator:
        return min(
            self._elevators,
            key=lambda e: abs(current_floor - e.get_current_floor())
        )

    def _execute_actions(self, elevator: Elevator, current_floor: int, target_floor: int) -> None:
        path = [current_floor, target_floor]

        action_map = {
            True: ["stop", "open", "close"],
            False: ["sameFloor"]
        }

        for floor in path:
            while elevator.get_current_floor() != floor:
                action = {
                    True: "moveUp",
                    False: "moveDown"
                }[floor > elevator.get_current_floor()]
                self.table[(elevator.get_direction().value, action)](elevator)

            for action in action_map[current_floor != target_floor]:
                self.table[(elevator.get_direction().value, action)](elevator)


    def print_movements(self) -> None:
        for elevator in self._elevators:
            print(f"Лифт #{elevator._elevator_id} сделал {elevator.get_movements()} движений")
