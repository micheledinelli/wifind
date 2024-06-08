from wifind.utils import get_data


def rooms():
    data = get_data()
    print('\n'.join(data.room.unique()))