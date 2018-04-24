
import os
# File names: to read in from and read out to
import pandas as pd


input_file = os.path.expanduser('~/Downloads/CS5344 Project/surprise/surprise/books.csv')
output_file = os.path.expanduser('~/Downloads/CS5344 Project/surprise/surprise/distinctBook.csv')
columns = ['book_id','original_title','isbn13','authors','original_publication_year']

data1 = pd.read_csv(input_file)
data1=data1[columns]
#data1 = data1[0:10]
data1.to_csv(output_file ,  index = False, header=True)

input_file = os.path.expanduser('~/Downloads/CS5344 Project/surprise/surprise/ratings.csv')
output_file = os.path.expanduser('~/Downloads/CS5344 Project/surprise/surprise/ratingsProcessed6m.csv')

data1 = pd.read_csv(input_file)
#data1=data1[columns]
data2 = data1[0:1000000]
data1.to_csv(output_file ,  index = False, header=False)




testset6.to_csv('xinrubookscsv1m.csv' ,  index = False, header=False)
