def download(YEAR, MONTHS, URL_TEMPLATE, TAXI_DATA):
    '''
    A python script to download the taxi datasets.

    Parameters:
    YEAR needs to be a string
    MONTHS need to be range(a, b), where a and b are integers from 1 to 13 and a < b
    URL_TEMPLATE is the URL that the data is going to be downloaded from
    TAXI_DATA is the file name of the taxi data, needs to be a string

    Note that this function is specifically for downloading the taxi data for this project
    only, and will might not behave the way as expected if it is used to download other datasets.
    '''

    # These code are all copied from the prereq notebook, with some modifications
    import os
    from urllib.request import urlretrieve
    
    #YEAR = '2022'
    # adjust the range function to the numerical months i.e 1 = jan, 2 = feb, etc...
    # MONTHS = range(1, 13)
    #MONTHS = range(1, 3)
    # this is the URL template as of 07/2022
    #URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"#year-month.parquet

    output_relative_dir = '../data/raw/'

    # check if it exists as it makedir will raise an error if it does exist
    if not os.path.exists(output_relative_dir):
        os.makedirs(output_relative_dir)
        
    # create the path for the dataset we need
    if not os.path.exists(output_relative_dir + TAXI_DATA):
        os.makedirs(output_relative_dir + TAXI_DATA)
    # data output directory
    tlc_output_dir = output_relative_dir + TAXI_DATA


    assert(MONTHS and YEAR)
    for month in MONTHS:
        # 0-fill i.e 1 -> 01, 2 -> 02, etc
        month = str(month).zfill(2) 
        print(f"Begin month {month}")
        
        # generate url
        url = f'{URL_TEMPLATE}{YEAR}-{month}.parquet'
        # generate output location and filename
        output_dir = f"{tlc_output_dir}/{YEAR}-{month}.parquet"
        # download
        urlretrieve(url, output_dir) 
        
        print(f"Completed month {month}")

    return

# download the green taxi data
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_"
YEAR = '2019'
MONTHS = range(1, 13)
TAXI_DATA = "green"
download(YEAR, MONTHS, URL_TEMPLATE, TAXI_DATA)

# download the yellow taxi data
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"
YEAR = '2019'
MONTHS = range(1, 13)
TAXI_DATA = "yellow"
download(YEAR, MONTHS, URL_TEMPLATE, TAXI_DATA)