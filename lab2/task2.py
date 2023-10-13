money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
increase_mult = 1 + increase


def calc_survival_months(money_capital, salary, spend, increase_mult):
    total_costs = 0
    total_money = money_capital
    month = 0

    while True:
        total_costs += spend * increase_mult ** month
        total_money += salary
        month += 1
        yield (month, total_costs, total_money)


# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
gen = calc_survival_months(money_capital, salary, spend, increase_mult)

for (month, total_costs, total_money) in gen:
    if total_costs > total_money:
        #gen return state of money after n month so we can survive n-1 months
        print("Количество месяцев, которое можно протянуть без долгов:", month - 1)
        exit()