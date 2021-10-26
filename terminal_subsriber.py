from typing import List
import termcolor
from celling.models.cell_machine_subscriber import CellMachineSubscriber


class TerminalCellMachineSubscriber(CellMachineSubscriber):
    def do_output(self, colors_list: List[str]):
        print(" ".join(map(lambda c: termcolor.colored(self.cell_marker, c), colors_list)))