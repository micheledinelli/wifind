import sys

NO_DATA_MSG = "No data available, please learn a location first.\nSee wifind learn --help"

class NoDataException(Exception):
    """
    This class is used to raise an exception when no data is available.
    """
    def __init__(self):
        self.message = NO_DATA_MSG
        super().__init__(self.message)
    
    def raise_exception(self):
        pass