import base64
import os

from .exception import  ResponseError

_image_file_name = 'image.png' #Image file path

class Response:
    """A class that returns the shuffled data and it's other meta_data
    
    Attributes:
        response:dict
            The shuffled data is passed as an argument to the initialization function
    
    Methods:
    
        shuffled_data()
                returns: the suffled data
                
        image(filename:str = None)
                :args filename: A filename of the image. If it's an absolute or relative, it gets store there.
                If it's the filename with no path, it get's store in your current working directory. 
                
                returns: an image file
        mean_dataframe()
        
        series_dataframe()
        
        all()


    Raises:
        ParameterError: Errors arising from shuffling parameters. 

    Returns:
        _type_: _description_
    """

     
    def __init__(self, shuffle:dict) -> None:
        self._shuffle = shuffle
    
    
    @property
    def mean_dataframe(self, filter:str = None):
        """Returns the Mean Dataframe of the shuffled data

        Args:
            filter (str, optional): Args that determines if the user wants it in a pandas dataframe(Yet to be implemented). 
            Defaults to None.
            . 
        Returns:
            list: 
        """
        
        return self._shuffle.get('MeansDataframe' , None)
    
    @property
    def series_dataframe(self , filter=None):
        """Returns the series dataframe of the shuffled data

        Args:
            filter (str, optional):Args that determines if the user wants it in a pandas dataframe(Yet to be implemented)
            Defaults to None.

        Returns:
            list: 
        """
        return self._shuffle.get('SeriesDataframe' , None)
    
    
    @property
    def shuffled_data(self , filter=None):
        """Returns the shuffled data

        Args:
            filter (str, optional): Args that determines if the user wants it in a pandas dataframe(Yet to be implemented).
            Defaults to None.

        Returns:
           list: 
        """
        shuffle = []
        data = self._shuffle.get('OptimumSeries' , None)
        if data == None:
            return None
        for _ in data.split("\n"):
            index = _.find(',')
            shuffle.append(_[index+1:])
        
        return shuffle
    
    @staticmethod
    def _check_graph_data(response):
        if not response['image']:
            return ResponseError("Response object has no image key")
        if os.path.exists(_image_file_name):
            return 'Image exists already. Check the image filepath'
        return True
    
    @property
    def graph_data(self , filename:str = None):
        """_summary_
        
        It returns graph data of the suffled data as an image
        
        Returns:
            str:
        """
        
         
        self._check_graph_data(self._shuffle) #Checks if the response has the image object
        
        image = filename if filename != None else _image_file_name
        imgdata = base64.b64decode(self._shuffle['image'])
        with open(image , 'wb') as file:
            file.write(imgdata)
        return image
    
    @property
    def all(self):
        """Returns all the output
        Returns:
            dict: 
        """
        return self._shuffle
    