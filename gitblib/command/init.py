from gitblib.command.command import Command
from gitblib.utility.createrepo import repo_create


class Init(Command):
    def execute(self, args):
        print('TODO init')
        repo_create(args.path)
