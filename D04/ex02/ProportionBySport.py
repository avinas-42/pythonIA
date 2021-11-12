def proportionBySport(data, year, sport, sex):
    year_data = data.loc[data['Year'] == year]
    sex_data = year_data.loc[year_data['Sex'] == sex]
    sport_data = sex_data.loc[sex_data['Sport'] == sport]
    if sex_data.size == 0:
        return None
    return sport_data.size / sex_data.size
