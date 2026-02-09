# Online retail ETL pipeline

This project implements an Extract->Transform->Load pipeline in python for online retail transactions transforming transactional retail data into clean, analytics-ready customer-level features, simulating a real-world data engineering workflow.

We test the code with the following dataset.

## Dataset
The data set used here is one which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.

This data set is public (UC Irvine ML repository) and can be found in
#### Chen, D. (2015). Online Retail [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.

```cmd
online-retail-etl/
│
├── data/
│   ├── raw/online_retail.xlxs
│   └── processed/customer_features.parquet
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── etl_pipeline.py
│
├── README.md
```

In the future I hope to load data into relational database

## How to run

```cmd
python src/etl_pipeline.py
```
