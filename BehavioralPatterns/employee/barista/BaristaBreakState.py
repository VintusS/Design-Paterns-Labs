from employee.EmployeeState import EmployeeState
import time
from tqdm import tqdm


class BaristaBreakState(EmployeeState):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Break"
        self.ascii_art = """
⣿⣿⣿⣿⣿⣿⣿⠿⠿⢛⣋⣙⣋⣩⣭⣭⣭⣭⣍⣉⡛⠻⢿⣿⣿⣿⣿
⣿⣿⣿⠟⣋⣥⣴⣾⣿⣿⣿⡆⣿⣿⣿⣿⣿⣿⡿⠟⠛⠗⢦⡙⢿⣿⣿
⣿⡟⡡⠾⠛⠻⢿⣿⣿⣿⡿⠃⣿⡿⣿⠿⠛⠉⠠⠴⢶⡜⣦⡀⡈⢿⣿
⡿⢀⣰⡏⣼⠋⠁⢲⡌⢤⣠⣾⣷⡄⢄⠠⡶⣾⡀⠀⣸⡷⢸⡷⢹⠈⣿
⡇⢘⢿⣇⢻⣤⣠⡼⢃⣤⣾⣿⣿⣿⢌⣷⣅⡘⠻⠿⢛⣡⣿⠀⣾⢠⣿
⣷⠸⣮⣿⣷⣨⣥⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢁⡼⠃⣼⣿  BRO GIMME A BREAK
⣿⡆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⡞⣱⠆⣿⣿
⣿⣿⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼⢸⡿⢸⣿⣿
⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢿⡌⠃⣿⣿⣿
⣿⣿⣿⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣷⢸⣷⠀⣿⣿⣿
⣿⣿⣿⡇⢻⣿⣿⣿⡿⠿⠿⣿⣿⣿⠿⠟⣡⡈⠻⣿⣿⣿⣿⢠⣿⣿⣿
⣿⣿⣿⣿⠘⣿⣿⣿⣿⣦⣙⣛⣛⣛⣋⠷⠙⢿⣷⣌⠛⢿⡇⣼⣿⣿⣿
⣿⣿⣿⡿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡙⢿⢗⣀⣁⠈⢻⣿⣿
⣿⡿⢋⣴⣿⣎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⣯⣿⣷⠆⠙⢿
⣏⠀⠈⠧⢡⠉⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠉⢉⣁⣀⣀⣾          
     """

    def handle_request(self, request: dict):
        print(self.ascii_art)
        iterations = 100
        duration = 2
        interval = duration / iterations

        for _ in tqdm(
            range(iterations),
            desc="Taking a Break",
            ncols=50,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
        ):
            time.sleep(interval)

    def __str__(self) -> str:
        return f"Barista state: {self.name}"

    def __repr__(self) -> str:
        return self.__str__()
