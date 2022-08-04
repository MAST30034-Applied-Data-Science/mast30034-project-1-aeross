def download(YEAR, MONTHS, URL_TEMPLATE, TAXI_DATA):
    '''
    YEAR needs to be a string
    MONTHS need to be range(a, b), where a and b are integers from 1 to 13 and a < b
    URL_TEMPLATE is the URL that the data is going to be downloaded from
    TAXI_DATA is the file name of the taxi data, needs to be a string
    '''

    # These code are all copied from the prereq notebook
    import os
    from urllib.request import urlretrieve
    
    #YEAR = '2022'
    # adjust the range function to the numerical months i.e 1 = jan, 2 = feb, etc...
    # MONTHS = range(1, 13)
    #MONTHS = range(1, 3)
    # this is the URL template as of 07/2022
    #URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"#year-month.parquet

    # changed this because I'm on the GitHub project repo
    output_relative_dir = '../data/'

    # check if it exists as it makedir will raise an error if it does exist
    if not os.path.exists(output_relative_dir):
        os.makedirs(output_relative_dir)
        
    # now, for each type of data set we will need, we will create the paths
    for target_dir in ('raw/green', 'raw/yellow'): # taxi_zones should already exist
        if not os.path.exists(output_relative_dir + target_dir):
            os.makedirs(output_relative_dir + target_dir)
        
    # data output directory is `data/tlc_data/`
    tlc_output_dir = output_relative_dir + TAXI_DATA

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