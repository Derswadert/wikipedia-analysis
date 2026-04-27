import pandas as pd
import glob
import os
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import re

path = r"D:\data\petWiki\data_raw"
output_path = r"D:\data\petWiki\silver_data"

os.environ['TMPDIR'] = 'D:\\temp'
os.environ['TEMP'] = 'D:\\temp'
os.environ['TMP'] = 'D:\\temp'

def process(filename):
    try:
        platform_map = {
            'm': 'mobile', 'd': 'desktop', 'b': 'wikibooks',
            'n': 'wikinews', 'q': 'wikiquote', 's': 'wikisource',
            'v': 'wikiversity', 'voy': 'wikivoyage', 'w': 'mediawiki',
            'wd': 'wikidata'
        }
        file_name = os.path.basename(filename)
        new_name = file_name.replace('.gz', '.parquet')
        out = os.path.join(output_path, new_name)

        if os.path.exists(out):
            return f"пропуск: {new_name} "

        df = pd.read_csv(
            filename,
            sep=" ",
            header=None,
            names=["project", "article", "views", 'bytes'],
            compression="gzip",
            on_bad_lines='skip'
        )

        df_clean = df[
            (~df['article'].str.contains(':')) &
            (~df['article'].str.match(r'^[QZ]\d+$', case=False)) &
            (df['article'] != '-') &
            (df['views'] > 1)
        ].copy()

        df_split = df_clean['project'].str.split('.', n=1, expand=True)

        df_clean['language'] = df_split[0]
        df_clean['platform'] = df_split[1]
        df_clean = df_clean.drop(['project', 'bytes'], axis=1)



        match = re.search(r'(\d{8})-(\d{6})', filename)
        if match:
            dt_str = match.group(1) + match.group(2)
            df_clean['datetime'] = pd.to_datetime(dt_str, format='%Y%m%d%H%M%S')

        df_clean['views'] = df_clean['views'].astype('int32')
        df_clean['platform'] = df_clean['platform'].map(platform_map).fillna('desktop').astype(str)
        df_clean['language'] = df_clean['language'].astype(str)

        df_clean = df_clean.dropna(subset=['article'])

        df_clean = df_clean[df_clean['article'].str.len() <= 250]

        df_clean.to_parquet(out, index=False, compression='snappy')

        print(f'файл {out}, cтрок: {len(df_clean)}')

        return 0
    except Exception as e:
        return f"ошибка в файле {filename}: {e}"

if __name__ == '__main__':

    files = glob.glob(os.path.join(path, "pageviews-*.gz"))

    os.makedirs(output_path, exist_ok=True)

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(tqdm(executor.map(process, files), total=len(files)))

    for res in results:
        if res != 0:
            print(res)

    print(f'Готово')