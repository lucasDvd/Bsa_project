# This is our repository for the BSA Project - Text Classification

## Purpose of the project 
The aim of the project is to predict the difficulty language of a sentence using ML models on Google Cloud. Difficulty is labelled with differents level : A1,A2,B1,B2,C1,C2.

## Methodologie
At the begining we tried training our dataset without cleaning directly on the Google Cloud. But here we faced some issues regarding the quality of the data. 
Therefore we decide to clean our dataset. For this, we :
- Put all letter in lower case.
- Remove all special character 
- Delete duplicates 
- Delete the first row in the csv format because Google Cloud didn't recognized it as column names.
- Delete the column "id"

Then we were able to train our model directly on Google Cloud.

## Evaluation
![Capture d’écran (43)](https://user-images.githubusercontent.com/73751401/169562841-eee20ba1-ce49-4291-91a7-8d1fe4c9ae49.png)
