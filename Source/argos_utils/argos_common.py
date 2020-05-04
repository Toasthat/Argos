from os import getenv

from tomlkit import parse


def load_config(toml_file, table):
    with open(toml_file, "r") as f:
        data = f.read()
        config = parse(data)
        # print(config)
    return config[table]


ARGOS_HOME = getenv("ARGOS_HOME")
ARGOS_CONFIG = ARGOS_HOME + "/Storage/config/argos.toml"
