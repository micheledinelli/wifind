from wifind.scan import scan
from wifind.utils import save_data 
from wifind.train import train

def learn(room):
    """
    This function is used to learn and gather data about a specific room.

    Parameters:
    room (str): The name of the room to gather data about.
    """
    # Obtain and store online data
    online_data = scan(room)
    save_data(online_data)
    train()