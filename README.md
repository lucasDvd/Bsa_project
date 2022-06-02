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
![Treshold 0 5](https://user-images.githubusercontent.com/73751401/171592508-ef1d760e-c5a5-4ee4-8c6b-b16c9be9bd8e.png)

Here we can see that with a threshold set to 0.5 we obtain the differents metrics:
- Precision score : 0.57
- Recall score : 0.48
- Accuracy : 0.56
- F1 - score : 0.52

### Confusion Matrix
![Confusion matrix](https://user-images.githubusercontent.com/73751401/171594857-2c64f162-b4dd-4aa3-8cec-854c9b777a32.png)
