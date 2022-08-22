# MAST30034 Project 1 README.md
- Name: Andrew Dharmaputra
- Student ID: 1213935

## Student Instructions
You **must** write up `README.md` for this repository to be eligable for readability marks.

1. Students must keep all Jupyter Notebooks in the `notebooks` directory.
2. Students must keep all `.py` scripts under the `scripts` directory. These can include helper functions and modules with relevant `__init__.py`
3. Students must store all raw data downloaded (using a Python script) in the `data/raw` folder. This will be in the `.gitignore` so **do not upload any raw data files whatsoever**.
4. Students must store all curated / transformed data in the `data/curated` folder. This will be in the `.gitignore` so **do not upload any raw data files whatsoever**. We will be running your code from the `scripts` directory to regenerated these.
5. All plots must be saved in the `plots` directory.
6. Finally, your report `.tex` files must be inside the `report` directory. If you are using overleaf, you can download the `.zip` and extract it into this folder.
7. Add your name and Student ID to the fields above.
8. Add your relevant `requirements.txt` to the root directory. If you are unsure, run `pip3 list --format=freeze > requirements.txt` (or alternative) and copy the output to the repository.
9. You may delete all `.gitkeep` files if you really want to. These were used to ensure empty directories could be pushed to `git`.
10. When you have read this, delete the `Student Instructions` section to clean the readme up.

Remember, we will be reading through and running your code, so it is in _your best interest_ to ensure it is readable and efficient.


**Research Goal:** My research goal is analysis of how time and location affect the number of crashes in New York City.

**Timeline:** The timeline for the research area is 2017 - 2019.

To run the pipeline, please visit the `scripts` directory and do the following:
1. run `download.py`: This downloads the TLC yellow taxi raw data into the `data/raw` directory.
2. For the taxi_zones file, I acquired those files from the GitHub tute repo (https://github.com/akiratwang/MAST30034_Python/blob/main/data/taxi_zones/), downloaded and put them *manually* into the data/raw/taxi_zones folder. Please make sure you do the same thing and that the data exists in the folder already before continuing from this step.
3. For the crash dataset, I found it from here: https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/data, and the download link is here: https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD. Similar to step 2, ensure the data is downloaded in the data/raw/ folder.
4. run `scrape.py`: This downloads the twilight data using web scraping from https://dateandtime.info/citysunrisesunset.php?id=5128581&month=1&year=2019.

Then, visit the `notebooks` directory and run the following files in order:
1. `preprocess.ipynb`: This notebook details all preprocessing steps on the TLC yellow taxi data and outputs it to the `data/curated` directory.
2. `preprocess2.ipynb`: This notebook details all preprocessing steps on the remaining data and outputs it to the `data/curated` directory.
3. `analysis.ipynb`: This notebook is used to conduct analysis on the curated data, run and analyse the models, and discuss the important features according to those models. If you want a more in-depth discussion, visit the relevant section in the report.
