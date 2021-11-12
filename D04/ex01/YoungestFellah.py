def youngestfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
    df: pandas.DataFrame object containing the dataset.
    year: integer corresponding to a year.
    Returns:
    dct: dictionary with 2 keys for female and male athlete.
    """
    ret = {'f': 'nan', 'm': 'nan'}
    year_data = df.loc[df['Year'] == year]
    men_data = year_data.loc[year_data['Sex'] == 'M']
    women_data = year_data.loc[year_data['Sex'] == 'F']
    if men_data.size > 0:
        youngest_age_m = men_data.Age.min()
        ret['m'] = str(youngest_age_m)

    if women_data.size > 0:
        youngest_age_w = women_data.Age.min()
        ret['f'] = str(youngest_age_w)

    return ret
