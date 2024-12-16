# Netflix EDA PySpark
Exploratory Data Analysis (EDA) on Netflix datasets using PySpark. This project is part of the **CE408 - Cloud Computing Assignment** by **Behram Khan**.


## Overview
This project demonstrates using PySpark to conduct an exploratory data analysis on the Netflix dataset. The analysis includes visualizations and insights derived from the dataset.

### Features:
- Data preprocessing with PySpark.
- Analysis of Netflix titles by genre, release year, and more.



## Dataset
The dataset used for this analysis is publicly available on [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) and contains information about Netflix titles, such as:
- Title
- Genre
- Release Year
- Country
- Duration
- Ratings

The dataset file is stored locally and mounted into the Docker container for processing.


## Requirements

### Software Requirements:
- Docker and Docker Compose
- Python 3.x (for local testing, if required)


## Setup Instructions

### Using Docker
1. Clone the repository:
   ```bash
   git clone https://github.com/behram7/Netflix_EDA_PySpark.git
   cd Netflix_EDA_PySpark
   ```

2. Start the Spark cluster:
   ```bash
   docker-compose up -d
   ```

3. Verify that the services are running:
   - Spark Master: [http://localhost:9090](http://localhost:9090)

### Running the Script
1. Copy the python script to the `spark-master` container:
   ```bash
   docker cp -L netflix_titles_eda.py spark-master:/opt/bitnami/spark/netflix_eda.py
   ```

2. Submit the PySpark job:
   ```bash
   docker exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/netflix_eda.py
   ```

3. Check the console output for analysis results and visualizations.



## Project Files

### Repository Structure:
![image](https://github.com/user-attachments/assets/30b25219-d2a2-4d3d-ada8-118f098c936e)


    Directory: C:\Users\Behram Khan\Desktop\assignment3


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        12/16/2024   8:14 PM                data
-a----        12/16/2024   8:13 PM           1301 docker-compose.yaml
-a----        12/16/2024   8:13 PM           1328 netflix_titles_eda.py
-a----        12/16/2024   8:13 PM           2281 README.md



## Results
https://github.com/user-attachments/assets/bcbefa2e-f280-4ffb-8e7a-4f7b084a6e4b


