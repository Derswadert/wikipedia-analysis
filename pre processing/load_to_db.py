import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import glob
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import logging

os.environ['TMPDIR'] = 'D:\\temp'
os.environ['TEMP'] = 'D:\\temp'
os.environ['TMP'] = 'D:\\temp'

load_dotenv(encoding='utf-8')

def process_file(file_path):
    try:
        engine = create_engine(os.getenv("DB_URL"))

        df = pd.read_parquet(file_path)

        df.to_sql(
            "fact_pageviews",
            con=engine,
            if_exists="append",
            index=False,
            chunksize=10000,
        )

        return f"{file_path}"

    except Exception as e:
        logging.exception(f"Ошибка обработки файла {file_path}")
        return 1
    finally:
        engine.dispose()


if __name__ == "__main__":

    path = "D:/data/petWiki/silver_data/"
    files = glob.glob(os.path.join(path, "*.parquet"))

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(tqdm(executor.map(process_file, files), total=len(files)))
    for res in results:
        print(res)

    print("Готово")