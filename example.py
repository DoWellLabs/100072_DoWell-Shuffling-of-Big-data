<<<<<<< HEAD
=======
from shuffling_big_data import ShufflingBigData

from m2r import parse_from_file

output = parse_from_file('READme.md')
print(output)



'''
params = {
    "deck": 100, #user defined value can be change but should be >=100
    "error": 1.67, #value can change but should be a floating number
    "test_num":11, #this is the number of times the data given is shuffled
    "deck_items": ['1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100']#items to be shuffled
}

s1 = ShufflingBigData(params = params) # Initialising the dataframe with all the parameters set
s1.response.all # returns all the response
s1.response.shuffled_data # returns all the shuffled_data
s1.response.graph_data # returns the graph_data in an image format 
s1.response.mean_dataframe # returns the mean_dataframe
s1.response.series_dataframe # returns the series_dataframe


#Initialising the Shuffling class without all the parameters set.
s2 = ShufflingBigData()


    Parameters can be set as a whole

s2.params = params

    Parameters can be set individually

s2.error = 1.66 #setting the error parameter value
s2.deck = 100 #setting the deck size. It must be more than 100
s2.test_num = 8 #setting the test_num to a certain value. 
# setting the deck items
s2.deck_items = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100'


s2.shuffle()

'''
>>>>>>> 3df8f63 (Initial Commit)
