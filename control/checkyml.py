from os import getcwd
from yaml import load, FullLoader, safe_load

class ParseYaml:

    def load_yml():
        auctual_path = getcwd()

        with open(f"{auctual_path}\machine\latest.yml") as yml_file:
          print(safe_load(yml_file))

ParseYaml.load_yml()