from commands import AddConfigCommand, SearchConfigCommand, DeleteConfigCommand
from exceptions import InvalidCommandException
import json


class CommandFactory:

    def __init__(self, config_service, output_service):
        self.config_service = config_service
        self.output_service = output_service

    def get_command(self, command_str):
        try:
            command_parts = command_str.split(" ")
            command_name = command_parts[0]
            config_name = command_parts[1]
        except:
            raise InvalidCommandException
        if command_name == "add_config":
            try:
                config_data = command_parts[2]
                config_data = json.loads(config_data)
            except:
                raise InvalidCommandException
            return AddConfigCommand(self.config_service, self.output_service, config_name,
                                    config_data)
        elif command_name == "search_config":
            return SearchConfigCommand(self.config_service, self.output_service, config_name)
        elif command_name == "delete_config":
            return DeleteConfigCommand(self.config_service, self.output_service, config_name)
        else:
            raise InvalidCommandException
