## NYC Vehicle Crash Analysis

**Research Goal:** How time and location affect the number of crashes in New York City.

**Timeline:** The timeline for the research area is 2017 - 2019.

To run the pipeline, please visit the `scripts` directory and do the following:
1. run `download.py`: This downloads the TLC yellow taxi raw data into the `data/raw` directory.
2. For the taxi_zones file, I acquired those files from the GitHub tute repo (https://github.com/akiratwang/MAST30034_Python/blob/main/data/taxi_zones/), downloaded and put them *manually* into the data/raw/taxi_zones folder. Please make sure you do the same thing and that the data exists in the folder already before continuing from this step.
3. For the crash dataset, I found it from here: https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/data, and the download link is here: https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD. Similar to step 2, ensure the data is downloaded in the data/raw/ folder.
4. run `scrape.py`: This downloads the twilight data using web scraping from https://dateandtime.info/citysunrisesunset.php?id=5128581&month=1&year=2019.

Then, visit the `notebooks` directory and run the following files in order:
1. `preprocess.ipynb`: This notebook details all preprocessing steps on the TLC yellow taxi data and outputs it to the `data/curated` directory.
2. `preprocess2.ipynb`: This notebook details all preprocessing steps on the remaining data and outputs it to the `data/curated` directory.
3. `analysis.ipynb`: This notebook is used to conduct analysis on the curated data, run and analyse the models, and discuss the important features according to those models. 
For a more in-depth discussion or analysis, visit the relevant section in the report.
