def deep_update(base_dict, update_dict):
    """
    Recursively update a dictionary with another dictionary.

    Args:
        base_dict (dict): The dictionary to update.
        update_dict (dict): The dictionary to update with.

    Returns:
        dict: The updated dictionary.
    """
    # Iterate over each key-value pair in the update dictionary
    for key, value in update_dict.items():
        # Check if the value is a dictionary
        if isinstance(value, dict):
            # Get the corresponding value from the base dictionary
            base_dict_value = base_dict.get(key)

            # If the base dictionary value is also a dictionary, recursively update it
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            else:
                # Otherwise, directly set the value in the base dictionary
                base_dict[key] = value
        else:
            # If the value is not a dictionary, directly set it in the base dictionary
            base_dict[key] = value

    return base_dict