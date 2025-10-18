import abc
from rich.console import Console

console = Console()

class BaseCommand(abc.ABC):
    def __init__(self):
        self.console = console

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        """Execute the command."""
        pass
