# Shuffling Big Data

Welcome to the Dowell Shuffling Big Data Library. The Library is based on Dowell's shuffling big data API. The API provides a comprehensive tool for shuffling a set of items. The items shuffled are 2-dimensional data. It provides a high level functionality in randomisation and test for central limit theorem on a give dataset. 


# Installation 

It supports Python 3.5+. The requests package is needed. 

``` bash
pip install dowell-shuffling-big-data
```
# Features

The Shuffling Big Data API offers the following features. 
    : Getting shuffled data
    : Get the graph data in an image format. 


# How it works

# Preparing the Shuffling Paramters

The shuffling parameters consist of four paramters - deck, error , test_num and deck_items. 
Deck is an integer user defined value that can be changed but should be greater than or equals to 100
Error is a float number
Test_num is the number of times the data given is shuffled
deck_items: This is the number ID of each data points to be shuffled. The number ID of each data points rather than data points itself are passed into the API. The deck_items is passed as a string of multiple IDs separated by commas. 

```python
# Set the shuffling parameters 


params = {
    "deck": 200, #user defined value can be change but should be >=100
    "error": 1.67, #value can change but should be a floating number
    "test_num": 7, #this is the number of times the data given is shuffled
    "deck_items": '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100' #items to be shuffled
}

```
# Output

The API returns json object with four keys - MeansDataframe, SeriesDataframe, OptimumSeries, graph_data
OptimumSeries - This is shuffled data. 
Graph_data - It is returned as an image. 


# Usage

# Import the ShufflingBig Data class

```python

from shuffling_big_data import ShufflingBigData

```
# Prepare the shuffling parameters

```python

params = {
    "deck": 200, #user defined value can be change but should be >=100
    "error": 1.67, #value can change but should be a floating number
    "test_num": 7, #this is the number of times the data given is shuffled
    "deck_items": '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100' #items to be shuffled
}

```

# Instantiating the Shuffling Data Class

The Data can be instantiated with with all the shuffling parameters set or not. However, it can't be shuffled without all the parameters set. 

```python
from shuffling_big_data import ShufflingData

 #Initialising the Shuffling_big_data class and passing the params dict to the params keyword argument

s1 = ShufflingData(params = params)

```



Initialising without the all or any parameters set

```python
s2 = ShufflingData()
```

# Working with the parameters

Setting params attribute with a variable called params. The params variable has to be an dict with four keys. The four keys should be the keys mentioned in the 'Setting parameters section'



```python
    
    s1.request_params = params 

        #or
    
    s1.params = params
```

Getting and Setting the each param

```python
s1.deck # returns the deck size. If deck size has not been set, it raises an error
s1.deck = 100 # sets the deck size. Remember it must be 100 and above

s1.error # returns the deck size. If error has not been set, it raises an error
s1.error = 1.45 #sets the error size. Remember it must be a float

s1.test_num #returns the deck size. If test_num has not been set, it raises an error
s1.test_num = 7 #sets the test_num. Remember it should be an integer. If it's a float, it rounds it to a whole number

s1.deck_items #returns the deck_items. If deck_items has not been set, it raises an error
s1.deck_items = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100' 

#sets the deck_items. If deck_items doesn't isn't a string with more than 60 comma separated items, it raises an error
```

# Output 

Getting the output from the Shuffling Big Data object passed with all parameters


```python
s1.response.all #Returns all the output
s1.image # Returns the graph_data
s1.mean_dataframe #Returns the mean_dataframe
s1.series_dataframe# Returns the series dataframe

```

For the instantiated ShufflingBigData Class without all inital paramters, the shuffle method shuffles the data. However, all the shuffling parameters have to be set. 

```python
s1.shuffle() #The shuffle method shuffles the data and returns the shuffled data class. 
```


