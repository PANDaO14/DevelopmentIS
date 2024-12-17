from Elevator import Elevator
from ElevatorSystem import ElevatorSystem


elevator1 = Elevator(elevator_id=1, current_floor=3)
elevator2 = Elevator(elevator_id=2, current_floor=5)

system = ElevatorSystem(n_floor=9)
system.add_elevator(elevator1)
system.add_elevator(elevator2)

system.add_request(current_floor=6, direction="up", target_floor=9)
system.add_request(current_floor=2, direction="up", target_floor=2)
system.add_request(current_floor=4, direction="down", target_floor=1)

system.process_requests()
system.print_movements()
