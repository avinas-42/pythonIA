import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class MyPlotLib:
    @staticmethod
    def histogram(data, features):
        tmp_data = pd.DataFrame(data, columns=features)
        tmp_data.hist(column=features)
        plt.show()

    @staticmethod
    def density(data, features):
        tmp_data = pd.DataFrame(data, columns=features)
        sns.displot(data=tmp_data, kind="kde")
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        tmp_data = pd.DataFrame(data, columns=features)
        sns.pairplot(data=tmp_data)
        plt.show()

    @staticmethod
    def box_plot(data, features):
        tmp_data = pd.DataFrame(data, columns=features)
        sns.boxplot(data=tmp_data)
        plt.show()
