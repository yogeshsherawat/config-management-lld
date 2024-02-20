from .command import Command


class DeleteConfigCommand(Command):

    def __init__(self, config_service, output_service, name):
        self.config_service = config_service
        self.name = name
        self.output_service = output_service

    def execute(self):
        self.config_service.delete_config(self.name)
        self.output_service.output(f"Config with name {self.name} deleted successfully")

