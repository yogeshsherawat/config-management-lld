from abc import ABC, abstractmethod
from command_factory import CommandFactory
from exceptions import InvalidCommandException


class Mode(ABC):
    """
    Abstract class for different modes of the application
        - File Mode
        - Interactive Mode
    """

    def __init__(self, config_service, output_service):
        self.config_service = config_service
        self.output_service = output_service

    @abstractmethod
    def process(self):
        pass

    def process_command(self, command_str):
        command_factory = CommandFactory(self.config_service, self.output_service)
        try:
            command = command_factory.get_command(command_str)
        except InvalidCommandException:
            self.output_service.output("Invalid command")
            return
        command.execute()
