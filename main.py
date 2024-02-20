




"""

models
    - config
        - data : dict -> can be loaded from json file
        - name : str -> searchable field

DB
    - db connection related methods

DAO
    - config's save/edit/delete operation in here

services
    - config's business logic in here
        - add a new config
        - edit a config
        - search a config by name
            - search client can be changed over time
                - to tackle this, will use composition

    - output service
        - to output the result of the command

    - search
        - isearch
        - inmemory search
        - elastic search
        search clients can vary so need to accomadate this

commands
    - command line interface related methods in here
    - add a new config
    - delete a config
    - search a config by name

modes
    - interactive mode
    - file mode

exceptions
    - self explanatory

command_factory
    - to get the command from the command string

main
    - main method to run the application


"""

from modes import FileMode
from services import ConfigService, OutputService
from services.search import InMemoryConfigSearch

config_service = ConfigService(InMemoryConfigSearch())
output_service = OutputService()
mode = FileMode(config_service, output_service, "file.txt")
mode.process()
