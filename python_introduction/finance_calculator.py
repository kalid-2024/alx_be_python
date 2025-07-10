income = float(input('Enter your monthly income: '))
expenses = float(input('Enter your total monthly expenses: '))
savings = income - expenses
i = 0.05
projected_savings = (savings) * 12 + (savings * 12 * i)
print(f'Your monthly savings are, ${savings}')
print(f'Projected savings after one year, with interest, is: ${projected_savings}')