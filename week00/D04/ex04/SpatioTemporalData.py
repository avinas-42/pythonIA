class SpatioTemporalData:
    def __init__(self, data):
        self.data = data

    def when(self, location):
        city_data = self.data.loc[self.data['City'] == location]
        year_list = city_data['Year'].unique()
        return list(year_list)

    def where(self, date):
        year_data = self.data.loc[self.data['Year'] == date]
        first = year_data.head(1)
        return first.iloc[0]['City']
