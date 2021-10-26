from abc import ABC, abstractmethod
from typing import List


class CellMachineSubscriber(ABC):
    cell_marker: str

    def __init__(self, cell_marker: str = '#'):
        self.cell_marker = cell_marker

    @abstractmethod
    def do_output(self, colors_list: List[str]):
        pass
