import argparse
from wifind.learn import learn
from wifind.utils import clear
from wifind.predict import predict
from wifind.rooms import rooms

def main():
    try:
        parser = argparse.ArgumentParser(description="Scan Wi-Fi networks.")
        subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        learn_parser = subparsers.add_parser("learn", help="Learn current position")
        learn_parser.add_argument("-r", "--room", help="Name of the room to sample", required=True)

        # depp_learn_parser = subparsers.add_parser("deep-learn", help="Learn current position")
        # depp_learn_parser.add_argument("-n", "--num", help="Number of samples to collect", required=True)
        # depp_learn_parser.add_argument("-r", "--room", help="Name of the room to sample", required=True)

        clean_parser = subparsers.add_parser("clear", help="Clear the data file")
        predict_parser = subparsers.add_parser("predict", help="Predict the room")
        
        room_parser = subparsers.add_parser("rooms", help="List the rooms in the data file")
        room_parser.add_argument("-s", "--samples", help="List the number of sample", required=False)

        args = parser.parse_args()

        if args.subcommand == "learn":
            learn(args.room)
        elif args.subcommand == "clear":
            clear()
        elif args.subcommand == "predict":
            predict()
        elif args.subcommand == "rooms":
            rooms(args.samples)
    except (KeyboardInterrupt, SystemExit):
        exit(0)

if __name__ == "__main__":
    main()