from celling.models.cell import Cell
from celling.models.cell_machine import CellMachine
from terminal_subsriber import TerminalCellMachineSubscriber

if __name__ == "__main__":
    print("Cellular Machine")

    cell_state = int(input("Enter cell state limit (1..5): "))
    cell_touching = int(input("Enter cell touching count (0..stackoverflow): "))
    timeout = float(input("Enter timeout between ticks: "))
    cells_count = int(input("Enter cells count: "))

    machine = CellMachine(cell_state, cell_touching, timeout)

    for i in range(cells_count):
        machine.append_cell(Cell())

    subscriber = TerminalCellMachineSubscriber("○")

    machine.start(subscriber)
