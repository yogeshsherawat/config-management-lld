from .command import Command


class SearchConfigCommand(Command):

    def __init__(self, config_service, output_service, name):
        self.config_service = config_service
        self.name = name
        self.output_service = output_service

    def execute(self):
        configs = self.config_service.search_config(self.name)
        self.output_service.output(configs)
