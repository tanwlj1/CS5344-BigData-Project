
import os
import pandas as pd

input_file = os.path.expanduser('~/Downloads/CS5344 Project/surprise/surprise/ratings.csv')
output_file = os.path.expanduser('~/Downloads/CS5344 Project/surprise/surprise/ratingsProcessed6m.csv')

data1 = pd.read_csv(input_file)
data1.to_csv(output_file ,  index = False, header=False)
