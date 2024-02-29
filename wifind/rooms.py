from wifind.utils import get_data

def rooms(samples=None):
    """
    This function is used to list the rooms in the data file.
    """
    data = get_data()
    ks = []
    for d in data:
        for key in d.keys():
            ks.append(key)
    
    # return the unique values
    print(list(set(ks)))