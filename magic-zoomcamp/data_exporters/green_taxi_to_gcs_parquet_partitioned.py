import pyarrow as pa
import pyarrow.parquet as pq
import os
import pandas as pd


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/turnkey-triumph-412303-6e16cb0bb63c.json"

bucket_name = 'zoomcamp_mage_green_taxi'
project_id = 'turnkey-triumph-412303'

table_name = 'ny_green_taxi_data'
root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data(data, *args, **kwargs):
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols = ['lpep_pickup_date'],
        filesystem=gcs
    )

    


