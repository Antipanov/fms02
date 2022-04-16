import pandas as pd

def download_comp_result_func(FightsDB_df, FightersDB_df, RoundsDB_df, weightcategoriesDB_df):
  FightsDB_df = FightsDB_df
  FightersDB_df = FightersDB_df
  RoundsDB_df = RoundsDB_df
  weightcategoriesDB_df = weightcategoriesDB_df
  
  FightsDB_df = pd.merge(FightsDB_df, FightersDB_df, left_on='red_fighter_id',  right_on='fighter_id', how = 'left')
  FightsDB_df['red_fighter_name'] = FightsDB_df['name'] + FightsDB_df['last_name']
  FightsDB_df = FightsDB_df.drop(['name', 'last_name'], axis=1)

  FightsDB_df = pd.merge(FightsDB_df, FightersDB_df, left_on='blue_fighter_id',  right_on='fighter_id', how = 'left')
  FightsDB_df['blue_fighter_name'] = FightsDB_df['name'] + FightsDB_df['last_name']
  FightsDB_df = FightsDB_df.drop(['name', 'last_name'], axis=1)

  FightsDB_df = pd.merge(FightsDB_df, RoundsDB_df, left_on='round_number',  right_on='id', how = 'left')
  FightsDB_df = pd.merge(FightsDB_df, weightcategoriesDB_df, left_on='weight_category',  right_on='weight_cat_id', how = 'left')
  FightsDB_df = FightsDB_df.loc[:, ['weight_category_name', 'round_name', 'red_fighter_name', 'blue_fighter_name', 'fight_result']]
  FightsDB_df = FightsDB_df.rename(columns={"weight_category_name":"Весовая категория", "round_name": "Раунд", "red_fighter_name":"Красный боец","blue_fighter_name":"Белый боец","fight_result": "Результат боя"})

  return FightsDB_df
  
  
  
  
  