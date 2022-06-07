from os import getcwd
from yaml import load, FullLoader, safe_load

class ParseYaml:

    def load_yml():
        auctual_path = getcwd()

        with open(f"{auctual_path}\machine\latest.yml") as yml_file:
          parsed_yml_file = (safe_load(yml_file))


    def vm_settings():