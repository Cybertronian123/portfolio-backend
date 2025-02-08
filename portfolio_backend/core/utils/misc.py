from __future__ import annotations

import yaml


def yaml_coerce(value):
    """
    Convert string values to Python dictionaries using YAML.
    Args:
        value (str or any): The value to be coerced. If the value is a string, it will be parsed as YAML.
    Returns:
        dict or any: If the input value is a string, it returns a dictionary parsed from the YAML string.
                     Otherwise, it returns the input value unchanged.
    """
    # Check if the value is a string
    # Parse the string as YAML and return the resulting dictionary
    # Return the original value if it's not a string
    # Convert string values to Python dictionaries

    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
