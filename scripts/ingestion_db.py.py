import pandas as pd
import os 
import gc
from sqlalchemy import create_engine
import logging
from datetime import datetime

start_time = datetime.now()
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s-%(message)s",
    filemode="a"
)    

engine = create_engine('sqlite:///inventorys.db', echo=False)

logging.info("========== DATA INGESTION STARTED ==========")
logging.info(f"Start Time: {start_time}")


CHUNK_SIZE = 10000
def ingest_db(df,table_name,engine,first_chunk=False):
    df.to_sql(table_name , con = engine , if_exists = 'replace' if first_chunk else 'append' , index= False,
             method = 'multi',
             chunksize=2000)


def load_raw_data():
    for file in os.listdir('data'):
    
        if file.endswith('.csv'):
    
            file_path = os.path.join('data', file)
            table_name = os.path.splitext(file)[0]
    
            logging.info(f"\nProcessing: {file}")
    
            total_rows = 0
    
            try:
    
                for i, chunk in enumerate(
                    pd.read_csv(
                        file_path,
                        chunksize=CHUNK_SIZE,
                        low_memory=True
                    )
                ):
    
                    ingest_db(
                        chunk,
                        table_name,
                       engine,
                       first_chunk=(i == 0)
                   )
                    total_rows += len(chunk)

                    logging.info(f"Inserted Rows: {total_rows}")
    
                    del chunk
                    gc.collect()
    
                logging.info(f"Completed: {file}")
               
    
            except Exception as e:
                logging.error(f"Error: {e}",exc_info=True)


    end_time = datetime.now()
    total_time = end_time - start_time
     
    logging.info("========== DATA INGESTION COMPLETED ==========")
    logging.info(f"End Time: {end_time}")
    logging.info(f"Total Execution Time: {total_time}")
    
if __name__=='__main__':
    load_raw_data()
