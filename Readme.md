# Simple APIs demo with FASTAPI

This repo demonstrates the example use case of FastAPI increating API for ML project POC.

## About
This project provide some simple API for user to interactive with. It reads in the csv data using `Pandas` library and allow user to interact with the data.

## Data Source
I use the data set from [Kaggle](https://www.kaggle.com/carrie1/ecommerce-data?select=data.csv). The dataset is attached along with this repo. I removed most of the rows of the csv file to reduce the size of the dataset.

## Getting Started
1. The first step is to clone this repo to your local directory.
2. Then, there are to ways to start the api:  
    **Run directly from Linux/WSL environment**
    ```[shell]
    cd <your-path>/API-WITH-FASTAPI
    ```
    Install the necessary libraries:
    ```
    pip install -r requirements.txt
    ```
    Then run the following in your console
    ```[shell]
    uvicorn main:app --reload
    ```
    The shell will prompt you with the localhost address that you can interact with. By default, it will use localhost:8000.
    To run it interactively, you can open it with `[address]:[port]/docs` in your browser. For example, http://127.0.0.1:8000/docs  
    
    **Run on docker** 
    Runing on docker is simpler, make sure you have docker installed and run the following cmd in the terminal.
    ```
    docker compose up
    ```
    You can then run open the interactive api in the browser by going to this link:
    ```
    localhost:80/docs
    ```
## To-do
- Using CSV is simple, plan to add SQL handler