import chardet
import os
import pandas as pd
import sqlite3
import tempfile
from src.model import create_db


dir_path = os.path.dirname(__file__)
data_path = os.path.join(dir_path, 'data')
db_name = 'data.db'


def gather_data(filepath):
    with open(filepath, 'rb') as f:
        char_detect = chardet.detect(f.read(200))
        encoding = char_detect['encoding']
    try:
        df = pd.read_csv(filepath, encoding=encoding, skiprows=[0], header=None,
                         names=['entity', 'value', 'string'], index_col=False)
    except UnicodeDecodeError:
        temp_f = change_encoding(filepath, encoding if encoding else 'utf-8')
        df = gather_data(temp_f)
        os.remove(temp_f)
    return df


def change_encoding(filepath, encoding):
    with open(filepath, 'rb') as f:
        temp_f, temp_p = tempfile.mkstemp(suffix='.csv', dir=data_path)
        with open(temp_f, 'r+') as tf:
            tf.write(f.read().decode(encoding=encoding, errors='replace'))
    return temp_p


def merge_data(folder_path):
    dfs = [gather_data(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if f.endswith('csv')]
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df


def import_data_to_db(df, conn):
    df.to_sql(name='parsed_data', con=conn, index_label='id', if_exists='append')


if __name__ == "__main__":
    df = merge_data(data_path)
    create_db(os.getcwd(), db_name)
    sql_conn = sqlite3.connect(db_name)
    import_data_to_db(df, sql_conn)
