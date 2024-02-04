import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # Initialize an empty DataFrame to hold all the concatenated data
    full_df = pd.DataFrame()

    taxi_dtypes = {
            'VendorID': pd.Int64Dtype(),
            'store_and_fwd_flag': str,
            'RatecodeID': pd.Int64Dtype(),
            'PULocationID': pd.Int64Dtype(),
            'DOLocationID': pd.Int64Dtype(),
            'passenger_count': pd.Int64Dtype(),
            'trip_distance': float,
            'fare_amount': float,
            'extra': float,
            'mta_tax': float,
            'tip_amount': float,
            'tolls_amount': float,
            'ehail_fee':float,
            'improvement_surcharge': float,
            'total_amount': float,
            'payment_type': pd.Int64Dtype(),
            'congestion_surcharge': float 
        }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    

    for month in range(10,13):
        
        month_str = f"{month:02d}"
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month_str}.csv.gz'
        print(url)
        
        parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
        # Read the data for current month
        df = pd.read_csv(url, sep=",", compression="gzip", dtype=taxi_dtypes, na_values='', parse_dates=parse_dates)

        # # Convert datetime columns
        # df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
        # df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

        # # # Format as '%Y/%m/%d %H:%M:%S'
        # df['lpep_pickup_datetime'] = df['lpep_pickup_datetime'].dt.strftime('%Y/%m/%d')
        # df['lpep_dropoff_datetime'] = df['lpep_dropoff_datetime'].dt.strftime('%Y/%m/%d')
        # df['lpep_pickup_date'] = pd.to_datetime(df['lpep_pickup_datetime']).dt.date

        

        # Concatenate the current month's data to the full DataFrame
        full_df = pd.concat([full_df, df], ignore_index=True)

        print(full_df.shape)
    return full_df
    
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'