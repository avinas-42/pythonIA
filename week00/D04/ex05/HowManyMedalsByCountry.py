def howManyMedalsByCountry(data, countryname):
    ret = {}
    name_data = data.loc[data['Team'] == countryname]
    year_list = name_data['Year'].unique()

    for year in year_list:

        tmp_year_data = name_data.loc[name_data['Year'] == year]
        gold_data = tmp_year_data.loc[tmp_year_data['Medal'] == 'Gold']
        silver_data = tmp_year_data.loc[tmp_year_data['Medal'] == 'Silver']
        bronze_data = tmp_year_data.loc[tmp_year_data['Medal'] == 'Bronze']
        ret[year] = {'G': gold_data.shape[0],
                     'S': silver_data.shape[0], 'B': bronze_data.shape[0]}
    return ret
