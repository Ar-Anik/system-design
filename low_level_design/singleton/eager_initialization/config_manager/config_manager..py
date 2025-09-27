import json
import os

class ConfigurationManager:
    _instance = None    # global access point
    _config = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._load_configuration()
        return cls._instance

    @classmethod
    def _load_configuration(cls):
        """Load Configuration from file or environment variables."""
        print("Loading Configuration...")

        config_file = os.environ.get('APP_CONFIG_FILE', os.path.join(os.path.dirname(__file__), 'config.json'))

        try:
            with open(config_file, "r") as f:
                cls._config = json.load(f)
        except FileNotFoundError:
            print(f"Config file not found: {config_file}. Using default values.")
            cls._config = {
                "db_url": os.environ.get("DB_URL", "postgresql://admin:secret@localhost:5432/mydatabase"),
                "debug": os.environ.get("DEBUG", "true").lower() == "true",
                "app_name": os.environ.get("APP_NAME", "MyDefaultApp"),
                "max_connections": int(os.environ.get("MAX_CONNECTIONS", "10"))
            }

    def get(self, key, default=None):
        return self._config.get(key, default)

    @classmethod
    def get_instance(cls):
        return cls._instance

# Eager Initialization - runs when the module is imported
ConfigurationManager._instance = ConfigurationManager()
"""
> In-Python, the moment we import a module, Python executes all the top-level statements in that file once.
So, this part : ConfigurationManager._instance = ConfigurationManager() will execute immediately as soon as 
the file containing it is imported — before we call any function or method from it.

> Python loads and runs the module top-to-bottom the first time it’s imported — no matter what we import from it.
That means:
    * Class definitions run.
    * Function definitions run (functions are just objects being created).
    * Any top-level code (like ConfigurationManager._instance = ConfigurationManager()) runs immediately.

Once the module is loaded, Python caches it in sys.modules, so subsequent imports don’t run it again — unless 
we explicitly reload it.
"""

if __name__ == '__main__':
    config = ConfigurationManager()

    print("Config object dict : ", config.__dict__)
    print("config : ", dir(config))

    print("Database URL: ", config.get('db_url'))
    print("Debug Mode: ", config.get('debug'))
    print('Application Name: ', config.get('app_name'))
    print('Max Connections: ', config.get('max_connections'))

    another_obj = ConfigurationManager()
    another_ref = ConfigurationManager.get_instance()

    print("Same Instance: ", another_obj is config)
    print("Same Instance: ", another_ref is config)
