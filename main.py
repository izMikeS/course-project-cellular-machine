from celling.models.cell import Cell
from celling.models.cell_machine import CellMachine
from terminal_subsriber import TerminalCellMachineSubscriber

if __name__ == "__main__":
    print("Cellular Machine")
    # possible values:
    # k: 1..5
    # r: 0..stackoverflow
    machine = CellMachine(4, 2, 0.5)

    for i in range(10):
        machine.append_cell(Cell())

    subscriber = TerminalCellMachineSubscriber("○")

    machine.start(subscriber)
