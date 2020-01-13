import chardet
import csv
import os
import pandas as pd


dir_path = os.path.dirname(__file__)
data_path = os.path.join(dir_path, 'data')


def gather_data(filepath):
    with open(filepath, 'rb') as f:
        char_detect = chardet.detect(f.read(200))
        encoding = char_detect['encoding']
    df = pd.read_csv(filepath, encoding=encoding, skiprows=[0], header=None, names=['entity', 'value', 'string'])
    return df


def merge_data(folder_path):
    dfs = [gather_data(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if f.endswith('csv')]
    merged_df = pd.concat(dfs)
    return merged_df


if __name__ == "__main__":
    df = merge_data(data_path)
    df.head(20)