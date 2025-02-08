from __future__ import annotations

from portfolio_backend.core.utils.collections import deep_update
from portfolio_backend.core.utils.settings import get_settings_from_environment
"""
This module updates the global settings of the project by merging them with
environment-specific settings.

Functions:
    deep_update: Recursively updates a dictionary with another dictionary.
    get_settings_from_environment: Retrieves settings from environment variables.

Usage:
    The `deep_update` function is used to merge the global settings with the
    environment-specific settings obtained from `get_settings_from_environment`.

Constants:
    ENVVAR_SETTINGS_PREFIX: A prefix used to filter relevant environment variables
    for settings.
"""

deep_update(
    globals(),
    get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore
