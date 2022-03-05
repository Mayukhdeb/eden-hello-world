import argparse

from eden.block import Block
from eden.hosting import host_block

parser = argparse.ArgumentParser()
parser.add_argument(
    "-ug",
    "--use-gpu",
    help="set to True if you want to check if eden is on a GPU runtime",
    required=False,
    default=False,
    type=bool,
)
parser.add_argument(
    "-n",
    "--num-workers",
    help="maximum number of workers to be run in parallel",
    required=False,
    default=1,
    type=int,
)
parser.add_argument(
    "-l",
    "--logfile",
    help="filename of log file",
    required=False,
    type=str,
    default=None,
)
parser.add_argument(
    "-p", "--port", help="localhost port", required=False, type=int, default=5656
)

args = parser.parse_args()

eden_block = Block()

my_args = {
    "name": "abraham",
    "number": 12345,
}


@eden_block.run(args=my_args)
def do_something(config):

    device = "cpu"
    if args.use_gpu:
        device = config.gpu

    print(f"on device:{device}")

    ## your stuff goes here

    return {
        "message": f"hello {config['name']}",
        "number": config["number"],
        "device": device,
    }


host_block(
    block=eden_block,
    port=args.port,
    logfile=args.logfile,
    requires_gpu=args.use_gpu,
    max_num_workers=args.num_workers,
)
