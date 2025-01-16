import os
from .misc import yaml_coerce

def get_settings_from_environment(prefix):
    """
    Retrieve settings from environment variables with a given prefix.
    This function searches the environment variables for keys that start with the specified prefix,
    strips the prefix from the keys, and returns a dictionary where the keys are the stripped
    environment variable names and the values are the corresponding environment variable values
    coerced using the `yaml_coerce` function.
    Args:
        prefix (str): The prefix to search for in the environment variable keys.
    Returns:
        dict: A dictionary containing the settings with the prefix stripped from the keys.
    Example:
        If the environment contains the variables:
        - 'MYAPP_DB_HOST': 'localhost'
        - 'MYAPP_DB_PORT': '5432'
        Calling `get_settings_from_environment('MYAPP_')` will return:
        {
            'DB_HOST': 'localhost',
            'DB_PORT': '5432'
        }
    """
    

    
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
    