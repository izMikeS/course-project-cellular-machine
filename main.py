from ctypes import ArgumentError

from celling.models.cell import Cell
from celling.models.cell_machine import CellMachine
from terminal_subsriber import TerminalCellMachineSubscriber

if __name__ == "__main__":
    print("Cellular Machine")

    cell_state = int(input("Enter cell state limit (from 1 inclusive to 5 inclusive): "))

    if cell_state < 1 or cell_state > 5:
        raise ArgumentError("Invalid cell state limit")

    cell_touching = int(input("Enter cell touching count (from 0 inclusive): "))

    if cell_touching < 0:
        raise ArgumentError("Invalid cell touching value")

    timeout = float(input("Enter timeout between ticks (from 0): "))

    if timeout <= 0:
        raise ArgumentError("Invalid timeout")

    cells_count = int(input("Enter cells amount (from 0): "))

    if cells_count <= 0:
        raise ArgumentError("Invalid cells amount")

    machine = CellMachine(cell_state, cell_touching, timeout)

    for i in range(cells_count):
        machine.append_cell(Cell())

    subscriber = TerminalCellMachineSubscriber("○")

    machine.start(subscriber)
