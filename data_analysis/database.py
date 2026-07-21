import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# connect to PostgresSQL database
connection=psycopg2.connect(host=os.getenv('DB_HOST'),port=os.getenv('DB_PORT'), database=os.getenv('DB_NAME'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'))

cursor=connection.cursor()

df=pd.read_csv('../dataset.csv')

for _, row in df.iterrows():
    cursor.execute(
        'INSERT INTO Images(filename, width, height, keypoints,'
        'matches, blur, brightness, contrast, processing_time,'
        'reprojection_error, new_points) '
        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (
            row['image'],
            row['width'],
            row['height'],
            row['keypoints'],
            row['matches'],
            row['blur'],
            row['brightness'],
            row['contrast'],
            row['processing_time'],
            row['reprojection_error'],
            row['new_points'],
        )
    )

# save changes to rhe database
connection.commit()

cursor.close()
connection.close()