import json


class Config:
    def __init__(self, environment):

        # Open the JSON file
        with open(f".\\config\\{environment}.json", 'r') as f:
            # Load the array from the JSON file
            data = json.load(f)
            self.settings = data["settings"]

        with open(f".\\config\\passwords.json", 'r') as f:
            # Load the array from the JSON file
            data = json.load(f)
            self.settings.update(data["settings"])

        print(f"Config loaded {str(len(self.settings))} Settings")

    def get(self, key):
        return self.settings[key]
