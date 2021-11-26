import termcolor

from celling.models.cell import Cell
from celling.models.cell_machine import CellMachine
from terminal_subsriber import TerminalCellMachineSubscriber

if __name__ == "__main__":
    print(termcolor.colored("Лінійний клітинний автомат", 'red'))

    while True:
        cell_state = input("Введіть максимально можливий стан клітини від одного до п'яти включно: ")

        if not cell_state.isdigit():
            print("Максимальний стан клітини повинен бути цілим числом")
            continue

        cell_state = int(cell_state)

        if cell_state < 1 or cell_state > 5:
            print("Значення максимального стану клітини повинно бути від 1 до 5.")
            continue

        break

    while True:
        cell_touching = input("Введіть кількість клітин-сусідів, що повинні враховуватись при перерахунку стану клітини"
                              ", від нуля включно: ")

        if not cell_touching.isdigit():
            print("Кількість клітин-сусідів, що будуть враховуватись, повинна бути цілим числом.")
            continue

        cell_touching = int(cell_touching)

        if cell_touching < 0:
            print("Кількість клітин-сусідів, що будуть враховуватись, повинна бути більше або дорівнювати нулю.")
            continue

        break

    while True:
        timeout = input("Введіть інтервал у секундах, згідно з яким буде працювати клітинний автомат,"
                        " значення повинно бути більше нуля: ")

        if not timeout.replace('.', '', 1).isdigit():
            print("Інтервал повинен бути числом.")
            continue

        timeout = float(timeout)

        if timeout <= 0:
            print("Інтервал повинен бути більше нуля.")
            continue

        break

    while True:
        cells_count = input("Введіть кількість клітин у автоматі (мінімум 1): ")

        if not cells_count.isdigit():
            print("Кількість клітин повинна бути цілим числом.")
            continue
        cells_count = int(cells_count)

        if cells_count < 1:
            print('Кількість клітин не може бути менше одного.')
            continue

        break

    machine = CellMachine(cell_state, cell_touching, timeout)

    for i in range(cells_count):
        machine.append_cell(Cell())

    subscriber = TerminalCellMachineSubscriber("○")

    machine.start(subscriber)
