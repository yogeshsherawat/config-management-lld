


class Config:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get_name(self):
        return self.name

    def get_data(self):
        return self.data

    def set_name(self, name):
        self.name = name

    def set_data(self, data):
        self.data = data

    def __str__(self):
        return f"Name: {self.name}, Data: {self.data}"