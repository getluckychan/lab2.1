from pay import Pay


def read():
    earn = input("Введіть оклад: ")
    worked_days = input("Введіть відпрацьовані дні:")
    days_in = input("Введіть дні у місяці: ")
    working = Pay(earn, worked_days, days_in)
    display(working)


def display(working):
    print(working.summa())


read()