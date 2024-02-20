from services.mode import Mode


class FileMode(Mode):

    def __init__(self, config_service, output_service, file_path):
        super().__init__(config_service, output_service)
        self.file_path = file_path

    def process(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                command_str = line.strip()
                self.process_command(command_str)
