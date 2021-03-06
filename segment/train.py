import argparse

from train.trainer import Trainer


def __main__():
    parser = argparse.ArgumentParser(description="Generate training images from a VOD.")
    parser.add_argument("infile", type=str, help="video to be processed")
    parser.add_argument("slippi", type=str, help="Slippi file to use")

    args = parser.parse_args()

    trainer = Trainer(args.infile, args.slippi)

    trainer.train()


if __name__ == "__main__":
    __main__()
