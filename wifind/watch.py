from wifind.predict import predict
import time


def watch(interval=2):
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - ", end="") 
    predict()
    while True:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - ", end="") 
        predict()
        time.sleep(interval)
