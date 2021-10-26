from typing import Optional

from celling.cell_utils import get_cell_color


class Cell:
    previous: Optional['Cell']
    next: Optional['Cell']
    current_state: int

    def __init__(self):
        self.previous = None
        self.next = None
        self.current_state = 0

    def __get_previous_sum(self, iter_count: int) -> int:
        if not self.previous or iter_count == 0:
            return 0

        return self.previous.current_state + self.previous.__get_previous_sum(iter_count - 1)

    def __get_next_sum(self, iter_count: int) -> int:
        if not self.next or iter_count == 0:
            return 0

        return self.next.current_state + self.next.__get_next_sum(iter_count - 1)

    def _get_neighbours_sum(self, iter_count: int) -> int:
        return self.__get_previous_sum(iter_count) + self.__get_next_sum(iter_count)

    def recount(self, max_state: int, take_cells_count: int):
        self.current_state += 1 + self._get_neighbours_sum(take_cells_count)

        self.current_state %= max_state

    def get_color(self):
        return get_cell_color(self.current_state)
