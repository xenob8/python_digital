salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

increase_mult = 1 + increase
TEN_MONTHS_SPENDS = sum(spend * increase_mult ** i for i in range(0, months))
TEN_MONTHS_SALARY = salary * months


#Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(TEN_MONTHS_SPENDS - TEN_MONTHS_SALARY))
