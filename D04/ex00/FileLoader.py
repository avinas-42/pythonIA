import pandas as pd


class FileLoader:
    def load(self, path):
        try:
            data_frame = pd.read_csv(path)
            shape = data_frame.shape
            if len(shape) > 1:
                large = shape[0]
                length = shape[1]
            print(f'Loading image of dimensions {large} x {length}')
            return data_frame
        except FileNotFoundError:
            print("Exception: FileNotFoundError --\
 strerror: No such file or directory")
            return None
        except (OSError, SyntaxError):
            print("Exception: OSError -- strerror: None")
            return None

    def display(self, df, n):
        nb_line = abs(n)
        if n < 0:
            print(df.tail(nb_line))
        elif n > 0:
            print(df.head(nb_line))
        else:
            return None
