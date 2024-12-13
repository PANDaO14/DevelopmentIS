from typing import Callable, Dict, List, Tuple
from Elevator import Elevator

class ElevatorSystem:
    def __init__(self, elevators: List[Elevator], n_floor: int) -> None:
        self._elevators = elevators
        self._n_floor = n_floor
        self._requests: List[Tuple[int, str, int]] = []
        self.table = self.generate_table()

    def generate_table(self) -> Dict[Tuple[str, str], Callable[[Elevator], None]]:
        table = {}
        actions = {
            "open": lambda e: e.open_door(),
            "close": lambda e: e.close_door(),
            "moveUp": lambda e: e.moveUp(),
            "moveDown": lambda e: e.moveDown(),
            "stop": lambda e: e.stop(),
        }

        for direction in ["idle", "up", "down"]:
            for action, func in actions.items():
                table[(direction, action)] = func
        
        return table

    def add_request(self, current_floor: int, direction: str, target_floor: int) -> None:
        floor_validation = {
            True: lambda: self._requests.append((current_floor, direction, target_floor)),
            False: lambda: (_ for _ in ()).throw(ValueError("Ошибка! Данный этаж не существует"))
        }
        floor_validation[1 <= current_floor <= self._n_floor and 1 <= target_floor <= self._n_floor]()

    def process_requests(self) -> None:
        for request in self._requests:
            current_floor, direction, target_floor = request
            elevator = self._find_nearest_elevator(current_floor, direction)
            print(f"\nЗапрос (с {current_floor} этажа по {target_floor} этаж):")
            self._execute_actions(elevator, current_floor, target_floor)

    def _find_nearest_elevator(self, current_floor: int, direction: str) -> Elevator:
        return min(
            self._elevators,
            key=lambda e: abs(current_floor - e.get_current_floor()) + (e.get_direction().value != direction)
        )

    def _execute_actions(self, elevator: Elevator, current_floor: int, target_floor: int) -> None:
        path = [current_floor, target_floor]
        for floor in path:
            while elevator.get_current_floor() != floor:
                action_dict = {
                    True: "moveUp",
                    False: "moveDown"
                }
                action_key =  action_dict[floor > elevator.get_current_floor()]
                self.table[(elevator.get_direction().value, action_key)](elevator)
            self.table[(elevator.get_direction().value, "stop")](elevator)
            self.table[(elevator.get_direction().value, "open")](elevator)
            self.table[(elevator.get_direction().value, "close")](elevator)

    def print_movements(self) -> None:
        for elevator in self._elevators:
            print(f"\nЛифт #{elevator._elevator_id} сделал {elevator.get_movements()} движений")