import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # Replace camelcase and spaces
    data.columns = (data.columns
                    .str.replace(' ','_')
                    .str.lower())

    print("Processing: rows with zero passangers: ", {data['passenger_count'].isin([0]).sum()})
    print(len(data[(data['passenger_count']>0) & (data['trip_distance']>0)]))

    data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'])
    data['lpep_dropoff_datetime'] = pd.to_datetime(data['lpep_dropoff_datetime'])

        # # Format as '%Y/%m/%d %H:%M:%S'
    # data['lpep_pickup_datetime'] = data['lpep_pickup_datetime'].dt.strftime('%Y/%m/%d')
    # data['lpep_dropoff_datetime'] = data['lpep_dropoff_datetime'].dt.strftime('%Y/%m/%d')

    return data[(data['passenger_count']>0) & (data['trip_distance']>0) & data['vendorid'].isin([1, 2])]



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
