import requests

from typing import AnyStr

from .exception import (ClientError , ParameterError , ResponseError)
from .response import Response

SHUFFLING_PARAMETERS = ('deck' , 'error' , 'test_num' , 'deck_items')
URL = "http://100072.pythonanywhere.com/api"




class ShufflingBigData:
    
    """
    Summary:
        The ShufflingBigData class is  a class that shuffles data based on some parameters. 
        It receives the number ID of each data points in a string along with other parameters and returns the output
        It returns a json object with four key values - means_dataframe, series_dataframe, optimumseries and base64 image. 
        The OptimumSeries key returns the shuffled in a string format. The string contains a pair value of the index and 
        
        
    Attributes:
        :params params: A dictionary that contains four keys deck, error, test_num, deck_items
            :key deck: A user defined integer that can be changed but should be >= 100
            :key error: A user defined float number that can be changed. It must be a float object. 
            :key test_num: A user defined integer. This is the number of times the data given is shuffled.
            :key deck_items: A user defined iterable or strings containing iterables. This is the item that is shuffled 
                    The deck_items needs to have at least 60 items in it. 
        
        
    Methods:
        shuffle()
            shuffles the ID numbers of the data point and returns the shuffled output.
        
        response
            A property method that gets the shuffled data which is a dict of four key values. 
        
        request_params:
            getter property. The parameters used in shuffling the data can be return. 
        
        request_params:
            setter property. The parameters can be set using the setter property.
        
        deck:
            A property method that gets and sets the value of the deck parameter. 
        
        error:
            A property method that gets and sets the value of the error parameter
        
        test_num:
            A property method that gets and sets the value of the test_num parameter
        
        deck_items:
            A property method that gets and sets the value of the deck_items parameter
            

    Returns:
        Response: A json object that's returned to a python dictionary
        The response includes the 
    """
    sessions = requests.Session()
    number_params_keys = 4
    response_data = {}
    
    def __init__(self , params:dict = {}):
        """Shuffles the data based on the parameters passed as a keyword argument. 

        Args:
            params (dict, optional): The shuffling data parameters. Defaults to {}.
        """
        self.params = params
        if self.params != {} and len(self.params.keys()) == ShufflingBigData.number_params_keys:
            self.shuffle()
            
            
    @property
    def response(self):
        """Returns the shuffled data class. 

        Returns:
            Response: 
        """
        self._check(self.request)
        return Response(self.request)
        
    @property
    def deck(self):
        """A property function that returns the deck key value of the shuffling parameter
        Returns:
            int: 
        """
        return self.params['deck']
    
    @deck.setter
    def deck(self , deck:int):
        """A setter property that sets the deck key value of the shuffling parameter
        Args:
            deck (int): It must have a value greater or equals to 100
        """
        self.check_deck(deck) #Validates the deck key value
        self.params['deck'] = deck
        
    @property
    def error(self):
        """A property function that returns the error value of the shuffling parameter

        Returns:
            float:
        """
        try:
            return self.error['error']
        except:
            raise ParameterError('Error accessed before initialisation')
        
    
    @error.setter
    def error(self , error:float):
        """A setter property that sets the error value of the shuffling parameter

        Args:
            error (float): _description_
        """
        self.params['error'] = error
    
    @property
    def test_num(self):
        if self.params != {}:
            return self.params['test_num']
        raise ParameterError('Parameters are referenced before they are initialized')
    
    @test_num.setter
    def test_num(self , test_num:int):
        """A property method that sets the test_num parameter

        Args:
            test_num (int): the new test_num value

        Raises:
            ParameterError: raises an error if the value passed is zero
        """
        if test_num == 0:
            raise ParameterError("Number of iterations cannot be zero")
        self.params['test_num'] = round(test_num)
        
    @property
    def deck_items(self):
        """Returns the number IDs of data points to be shuffled. 

        Raises:
            ParameterError: raises an error if the value is accessed before being initialised

        Returns:
            str: 
        """
        try:
            return self.params['deck_items']
        except:
            raise ParameterError('Deck_items accessed before initialisation')
        
    @deck_items.setter
    def deck_items(self , deck_items:str):
        """Sets the value of deck_items parameter. 

        Args:
            deck_items (str): An str consisting of comma separated number items.

        Raises:
            ValueError: If the items are not separated by commas and not more than 60
        """
        if ',' in deck_items and len(deck_items.split(',')) > 100:
            self.params['deck_items'] = deck_items
        else:
            raise ValueError('Deck_Items are to be separated by commas and items are to be more than 60')
    
    @staticmethod  
    def check_deck(deck:int):
        """Validates the deck items value

        Args:
            deck (int):

        Raises:
            ParameterError: raises an error if the deck value passed is less than 100
        """
        if deck < 100:
            raise ParameterError("Deck has to be more than 100")
    
    @staticmethod
    def _check(request):
        """
        Checks if requests to the Dowell Shuffling Big Data API was successful
    
        Returns:
            Bool:  
        """
        try:
            if not request:
                raise ClientError("Request is not made or the response brought no data")
            if request == None:
                raise ParameterError("Problems with the parameter")
            return True
        except:
            return False
    
    
    def end_session(self):
        """Ends the request session to the Dowell Shuffling Data API
        
        Returns:
            None
        """
        self.sessions.cookies.clear()
    
    def shuffle(self):
        """
        Sends a post request to the Dowell Shuffling Big Data API to get shuffled data

        Raises:
            e: Returns any error encountered while trying to access the Dowell Shuffling Big Data API
        """
        
        if self.params is {}:
            raise ParameterError('Parameters need to be initialized. Without any data, there is no shuffling')
        try:
            self.validate_params(self.params)
            self.request = ShufflingBigData.sessions.post(URL, self.params).json()
            return self.response
        except ClientError as e:
            raise e
        
    @staticmethod
    def validate_params(parameters:dict):
        """Validates the shuffling parameters

        Args:
            parameters (dict): shuffling parameters

        Raises:
            ParameterError: A parameter error is an error that occurs when the parameters don't 
            meet the required standard
        """
        params_keys = parameters.keys()
        if len(params_keys) < ShufflingBigData.number_params_keys:
            param =set(SHUFFLING_PARAMETERS) - set(params_keys)
            raise ParameterError("{} has to be in the string".format(param.pop()))
        
        ShufflingBigData.check_deck(parameters['deck'])
            
    
        
        
    
    
    
        
        

