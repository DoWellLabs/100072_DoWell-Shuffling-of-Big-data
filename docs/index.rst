.. Dowell Shuffling Big Data documentation master file, created by
   sphinx-quickstart on Tue Jul  4 13:44:15 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

=======
Welcome to Dowell Shuffling Big Data's documentation!
=====================================================


Shuffling Big Data
==================

Welcome to the Dowell Shuffling Big Data Library. The Library is based on Dowell's shuffling big data API. The API provides a comprehensive tool for shuffling a set of items. The items shuffled are 2-dimensional data. It provides a high level functionality in randomisation and test for central limit theorem on a give dataset. 

Installation
============

It supports Python 3.5+. The requests package is needed. 
No package yet. However you can clone the Dowell Shuffling Data Repository for the code. 

Features
========

The Shuffling Big Data API offers the following features. 

.. code-block::

   - Getting shuffled data based on shuffling parameters. 
   - Get the graph data of the shuffled data in an image format. 
   - Get the means dataframe of the shuffled data
   - Get the series dataframe of the shuffled data.




How it works
============

Preparing the Shuffling Paramters
---------------------------------

The shuffling parameters consist of four paramters - deck, error , test_num and deck_items. 
Deck is an integer user defined value that can be changed but should be greater than or equals to 100
Error is a float number
Test_num is the number of times the data given is shuffled
deck_items: This is the number ID of each data points to be shuffled. The number ID of each data points rather than data points itself are passed into the API. The deck_items is passed as a string of multiple IDs separated by commas. 

.. code-block:: python

   # Set the shuffling parameters 


   params = {
       "deck": 200, #user defined value can be change but should be >=100
       "error": 1.67, #value can change but should be a floating number
       "test_num": 7, #this is the number of times the data given is shuffled
       "deck_items": '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100' #items to be shuffled
   }

Output
------

The API returns json object with four keys - MeansDataframe, SeriesDataframe, OptimumSeries, graph_data
OptimumSeries - This is shuffled data. 
Graph_data - It is returned as an image. 

Usage
=====

Import the ShufflingBig Data class
----------------------------------

.. code-block:: python


   from shuffling_big_data import ShufflingBigData

Prepare the shuffling parameters
--------------------------------

.. code-block:: python


   params = {
       "deck": 200, #user defined value can be change but should be >=100
       "error": 1.67, #value can change but should be a floating number
       "test_num": 7, #this is the number of times the data given is shuffled
       "deck_items": '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100' #items to be shuffled
   }

Instantiating the Shuffling Data Class
--------------------------------------

The Data can be instantiated with with all the shuffling parameters set or not. However, it can't be shuffled without all the parameters set. 

.. code-block:: python

   from shuffling_big_data import ShufflingData

    #Initialising the Shuffling_big_data class and passing the params dict to the params keyword argument

   s1 = ShufflingData(params = params)

Initialising without the all or any parameters set

.. code-block:: python

   s2 = ShufflingData()

Working with the parameters
---------------------------

Setting params attribute with a variable called params. The params variable has to be an dict with four keys. The four keys should be the keys mentioned in the 'Setting parameters section'

.. code-block:: python


       s1.request_params = params 

           #or

       s1.params = params

Getting and Setting the each param

.. code-block:: python

   s1.deck # returns the deck size. If deck size has not been set, it raises an error
   s1.deck = 100 # sets the deck size. Remember it must be 100 and above

   s1.error # returns the deck size. If error has not been set, it raises an error
   s1.error = 1.45 #sets the error size. Remember it must be a float

   s1.test_num #returns the deck size. If test_num has not been set, it raises an error
   s1.test_num = 7 #sets the test_num. Remember it should be an integer. If it's a float, it rounds it to a whole number

   s1.deck_items #returns the deck_items. If deck_items has not been set, it raises an error
   s1.deck_items = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100' 

   #sets the deck_items. If deck_items doesn't isn't a string with more than 60 comma separated items, it raises an error

Output
------

Getting the output from the Shuffling Big Data object passed with all parameters

.. code-block:: python

   s1.response.all #Returns all the output
   s1.image # Returns the graph_data
   s1.mean_dataframe #Returns the mean_dataframe
   s1.series_dataframe# Returns the series dataframe

For the instantiated ShufflingBigData Class without all inital paramters, the shuffle method shuffles the data. However, all the shuffling parameters have to be set. 

.. code-block:: python

   s1.shuffle() #The shuffle method shuffles the data and returns the shuffled data class.

Classes
=======

The 'ShufflingDataClass' Class
------------------------------

The ShufflingBigData class is  a class that shuffles data based on some parameters. 
It receives the number ID of each data points in a string along with other parameters and returns the output
It returns a json object with four key values - means_dataframe, series_dataframe, optimumseries and base64 image. 
The 'OptimumSeries' key returns the shuffled in a string format. The string contains a pair value of the index and 

Attributes:
-----------

.. code-block::

       :'params' params: A dictionary that contains four keys deck, error, test_num, deck_items
           :key 'deck': A user defined integer that can be changed but should be >= 100
           :key 'error': A user defined float number that can be changed. It must be a float object. 
           :key 'test_num': A user defined integer. This is the number of times the data given is shuffled.
           :key 'deck_items': A user defined iterable or strings containing iterables. This is the item that is shuffled 
                   The deck_items needs to have at least 60 items in it. 

       :'mean_dataframe':
           returns the dataframe of th

       'series_dataframe':
           returns the series dataframe

       :'all':
           returns all the output

       :'graph_data':
           returns the graph data



Methods:
--------

.. code-block::

   shuffle()
           shuffles the ID numbers of the data point and returns the shuffled output.

   'response'
           A property method that gets the shuffled data which is the response class. 

   'request_params':
           getter property. The parameters used in shuffling the data can be return. 

   'request_params':
           setter property. The parameters can be set using the setter property.

   'deck':
           A property method that gets and sets the value of the deck parameter. 

   'error':
           A property method that gets and sets the value of the error parameter

   'test_num':
           A property method that gets and sets the value of the test_num parameter

   'deck_items':
           A property method that gets and sets the value of the deck_items parameter


   Returns:
       'Response': A json object that's returned to a python dictionary
       The response includes the 


Response Class
==============

The 'Response' is a class that handles the shuffled data. 

Attributes:
-----------

.. code-block::

       'response':dict
           The shuffled data is passed as an argument to the initialization function



Methods:
--------

.. code-block::

       'shuffled_data()'
               'returns': the suffled data

       'graph(filename:str = None)'
               :args 'filename': A filename of the image. If it's an absolute or relative, it gets store there.
               If it's the filename with no path, it get's store in your current working directory. 

               returns: an image file

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

