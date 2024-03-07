from wifind.errors import NoDataException
from wifind.utils import get_data

def rooms(samples=None):
    """
    This function is used to list the rooms in the data file.
    """
    try:
        data = get_data()
        print(data.room.unique())
    except NoDataException as e:
        print(e)