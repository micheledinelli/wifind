from wifind.scan import scan
from wifind.utils import save_data 
from wifind.train import train


def learn(room: str):
    online_data = scan(room)
    save_data(online_data)
    train()