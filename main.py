from Elevator import Elevator
from ElevatorSystem import ElevatorSystem


elevator1 = Elevator(elevator_id=1, current_floor=3)
elevator2 = Elevator(elevator_id=2, current_floor=1)

system = ElevatorSystem([elevator1, elevator2], n_floor=9)
system.add_request(current_floor=5, direction="up", target_floor=9)
system.add_request(current_floor=4, direction="down", target_floor=1)
system.process_requests()
system.print_movements()