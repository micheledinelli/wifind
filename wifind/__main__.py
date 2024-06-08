import argparse
from wifind.learn import learn
from wifind.utils import clear
from wifind.predict import predict, predict_proba
from wifind.rooms import rooms
from wifind.watch import watch
from wifind._version import __version__

def main():
    try:
        parser = argparse.ArgumentParser(description="WiFi fingerprinting indoor localization system.")
        subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        learn_parser = subparsers.add_parser("learn", help="Learn current position")
        learn_parser.add_argument("-r", "--room", help="Name of the room to sample", required=True)

        clear_parser = subparsers.add_parser("clear", help="Clear the data file")
        predict_parser = subparsers.add_parser("predict", help="Predict the room")
        predict_parser.add_argument("-p", "--proba", help="Predict the probability", action="store_true", required=False)
        
        room_parser = subparsers.add_parser("rooms", help="List the rooms in the data file")
        room_parser.add_argument("-s", "--samples", help="List the number of sample", required=False)

        parser.add_argument("-w", "--watch", help="Print in the terminal location changes", required=False, const=True, nargs='?')
        parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

        args = parser.parse_args()

        if args.subcommand == "learn":
            learn(args.room)
        elif args.subcommand == "clear":
            clear()
        elif args.subcommand == "predict":

            if args.proba:
                predict_proba()
            else:
                predict()    
        elif args.subcommand == "rooms":
            rooms()
        elif args.watch:
            watch(args.watch)
        
    except (KeyboardInterrupt, SystemExit):
        exit(0)

if __name__ == "__main__":
    main()