"""Module exceptions."""

class ClientError(Exception):
    """Raised when an error occurs during API request"""

class ParameterError(Exception):
    """Raised when the values of the parameters do not meet the requirments"""
    
class ResponseError(Exception):
    """Raised when the content does not contain expected value"""
