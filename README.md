# ucsd-ces-2019-leaderboard-election

## Description

This is a simple project for reading from election evaluation google forms, hide and forward appropriorate information to each member in the leaderboard, and finally calculate the overall score for each candidate.

## Election rules

To be added

## Usage 
Before running the program, populate approapriate authentication json file from Google's Cloud API and put it in the same directory as this project with name `authentication.json`

### To generate candidates' comments to the leaderboard member
- Open `Comment Population.ipynb` with Jupyter Notebook and run all cells
- A series of csv files would be populated in the working directory with leaderboard member names

### To generate final score for each candidate
- Open `Score Calculation.ipynb` with Jupyter Notebook and run all cells
- A csv file named `result.csv` would contain final score for each candidate
