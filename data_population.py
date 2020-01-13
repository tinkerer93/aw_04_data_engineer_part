import os
import pandas as pd


dir_path = os.path.dirname(__file__)
data_path = os.path.join(dir_path, 'data')


def gather_data(filepath):
    try:
        encode_data = pd.read_csv(filepath, dtype=str, nrows=1)
    except UnicodeDecodeError:
        raise UnicodeDecodeError
    encoding_type = encode_data.split('=')[1]
    df = pd.read_csv(filepath, delimiter=',')
    df = df.transpose()
    return df


def merge_data(folder_path):
    dfs = [gather_data(f) for f in os.listdir(folder_path) if f.endswith('csv')]
    merged_df = pd.concat(dfs)
    return merged_df


if __name__ == "__main__":
    test_file = os.path.join(data_path, 'test-0.csv')
    df = gather_data(test_file)
    print(df)