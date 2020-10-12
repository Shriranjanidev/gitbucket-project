import argparse
import sys
from command.Init import Init

argparser = argparse.ArgumentParser(description = 'An implementation of git')
argsubparsers = argparser.add_subparsers(title = 'Commands', dest = 'command')
argsubparsers.required = True

argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository")

argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Path to create the repository.")

command_dict = dict({
    'init': Init()
})

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)  
    cmd = command_dict.get(args.command)
    cmd.execute(args)