import pandas as pd



# расчет производим от стратегии. Стратегия напрямую зависит от количества бойцов в категории.
# первая стратегия - в категории три человека. Каждый дерется с каждым. Победитель определяется по количеству побед. Если кол-во побед равное, то по количеству набранных во всех боях очков. Если кол-во очков равное, то там уже как-то судья определит вне системы. 
# для реализации стратегии. 1. Мы можем расставить и бои и заполнить их бойцами.
# результатом расчета у нас будет json, который будет содержать данные как о квадратиках с кругами, так и бойцами, которые их заполняют.
# квадратики заполняем насколько можем вперед. Участников заполняем насколько можем вперед
comp_strategy_id = 1
number_of_regs_in_category = 5
# каждый круг - это дикт. все круги - это лист диктов
weight_category_rounds_data = []

# рассчитываем первый круг
# round_counter - счетчик-итератор кругов в категории
round_counter = 0
# все бои заканчиваются, когда в категории количество боев равно 1 и количество активных бойцов = 2
# боец получает статус "активный" = 1 при регистрации и получает  "активный" = 0
# начальное значение кол-ва боев в категории определяется на старте. Потому что мы знаем кол-во людей в категории

# стретегией мы определяем сколько боев должен провести участники
group_phase_qty_of_fights_of_each_fighter = 2
# что это значит. Это значит что можно ввести индикатор. кол-во боев обчзательное умножить на кол-во
# участников. когда это значение станет ноль, значит групповой турнир завершен
group_phase_index = group_phase_qty_of_fights_of_each_fighter * number_of_regs_in_category

fights_qty_in_round = number_of_regs_in_category // 2

regs_df = pd.read_csv('temp_files/regs_strategy_1.csv')
active_fighters_qty = len(regs_df.loc[regs_df['reg_activity_status']==1])

# рассчитываем раунды группового турнира. 
while fights_qty_in_round >= 1 and active_fighters_qty > 2 and group_phase_index >0:
  round_data = {}
  round_counter = round_counter +1 # счетчик раундов 
  round_data['round_no'] = round_counter # порядковый номер раунда в категории
  round_data['fights_qty_in_round'] = fights_qty_in_round
  round_data['group_phase_index'] = group_phase_index

  weight_category_rounds_data.append(round_data)
  group_phase_index = group_phase_index - 2* fights_qty_in_round
  print("group_phase_index: ", group_phase_index)

print(weight_category_rounds_data)
print("кол-во раундов: ", len(weight_category_rounds_data))