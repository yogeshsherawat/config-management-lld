from .command import Command


class AddConfigCommand(Command):

    def __init__(self, config_service, output_service, name, data):
        self.config_service = config_service
        self.output_service = output_service
        self.name = name
        self.data = data

    def execute(self):
        self.config_service.add_config(self.name, self.data)
        self.output_service.output(f"Config with name {self.name} added successfully")

