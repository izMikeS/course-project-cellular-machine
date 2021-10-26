import time
from typing import List

from celling.models.cell import Cell
from celling.models.cell_machine_subscriber import CellMachineSubscriber


class CellMachine:
    __cells: List[Cell]
    __is_enabled: False
    _cell_states_count: int
    _cell_radius_count: int
    _tick_interval: float

    def __init__(self, cell_states_count: int = 2, cell_radius_count: int = 1, tick_interval: float = 1):
        self.__cells = []
        self._cell_states_count = cell_states_count
        self._cell_radius_count = cell_radius_count
        self._tick_interval = tick_interval

    def append_cell(self, cell: Cell):
        if self.__cells:
            cell.previous = self.__cells[-1]
            self.__cells[-1].next = cell

        self.__cells.append(cell)

    def start(self, subscriber: CellMachineSubscriber):
        self.__is_enabled = True

        while self.__is_enabled:
            subscriber.do_output(self.get_colors())

            for c in self.__cells:
                c.recount(self._cell_states_count, self._cell_radius_count)

            time.sleep(self._tick_interval)

    def stop(self):
        if self.__is_enabled:
            self.__is_enabled = False

    def get_colors(self) -> List[str]:
        return list(map(lambda c: c.get_color(), self.__cells))
