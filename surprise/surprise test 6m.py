from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split
from surprise import BaselineOnly
from surprise import KNNBasic
from surprise import SlopeOne
from surprise import CoClustering
from surprise import SVD
from surprise import SVDpp
from surprise import NMF
from surprise import NormalPredictor
from surprise import Dataset
from surprise import accuracy
from surprise import Reader

import time
import pandas as pd
import os

file_path6 = os.path.expanduser('~/Downloads/CS5344 Project/surprise/surprise/data/ratingsProcessed6m.csv')

reader = Reader(line_format='user item rating', sep=',')

data6 = Dataset.load_from_file(file_path6, reader=reader)

# sample random trainset and testset
# test set is made of 25% of the ratings.
trainset6, testset6 = train_test_split(data6, test_size=.25)

# Choose the algo to use to compute RMSE
algo = SVD()
algo = BaselineOnly()
algo = KNNBasic()
algo = SlopeOne()
algo = CoClustering()
algo = SVDpp()
algo = NMF()
algo = NormalPredictor()

# Train the algorithm on the trainset, and predict ratings for the testset
start = time.time()
algo.fit(trainset6)
predictions = algo.test(testset6)
accuracy.rmse(predictions)
end = time.time()

elapsed = end - start
print(elapsed)

# Then compute RMSE
accuracy.rmse(predictions)
predictions = algo.fit(trainset6).test(testset6)
predictions

# compute similarity matrix
result = []
result = algo.compute_similarities()