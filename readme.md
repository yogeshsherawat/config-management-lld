# Design a Configuration Management System

## Features

- **Add Configuration**
  - Users should be able to add new configurations to the system.

- **Delete Configuration**
  - Users should have the ability to delete existing configurations.

- **Search for Configuration**
  - Users should be able to search for specific configurations within the system.

- **Subscribe to Configuration**
  - Users can subscribe to configurations of interest. This ensures that they are notified of any updates to those configurations.

## Solution

### Models
- `config`
  - `data : dict` -> can be loaded from a json file
  - `name : str` -> searchable field

### DB
- Database connection related methods

### DAO
- Config's save/edit/delete operations are handled here

### Services
- Handles config's business logic, including:
  - Adding a new config
  - Editing a config
  - Searching a config by name
    - To tackle changes in the search client over time, composition will be used

- `output service`
  - To output the result of the command

- `search`
  - `isearch`
  - `inmemory search`
  - `elastic search`
    - Search clients can vary, so the system needs to accommodate this

### Commands
- Command Line Interface (CLI) related methods
  - Add a new config
  - Delete a config
  - Search a config by name

### Modes
- Interactive mode
- File mode

### Exceptions
- Self-explanatory

### Command Factory
- To get the command from the command string

### Main
- The main method to run the application
