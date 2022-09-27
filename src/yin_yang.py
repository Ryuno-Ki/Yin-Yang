
"""
title: yin_yang
description: yin_yang provides an easy way to toggle between light and dark
mode for your kde desktop. It also themes your vscode and
all other qt application with it.
author: oskarsh
date: 21.12.2018
license: MIT
"""

import logging
import time

from src.config import config, plugins

logger = logging.getLogger(__name__)


def should_be_dark(time_current: time, time_light: time, time_dark: time) -> bool:
    """Compares two times with current time"""

    if time_light < time_dark:
        return not (time_light <= time_current < time_dark)
    else:
        return time_dark <= time_current < time_light


def set_mode(dark: bool, force=False):
    """Activates light or dark theme"""

    if not force and dark == config.dark_mode:
        return

    logger.info(f'Switching to {"dark" if dark else "light"} mode.')
    for p in plugins:
        if config.get_plugin_key(p.name, 'enabled'):
            try:
                logger.info(f'Changing theme in plugin {p.name}')
                p.set_mode(dark)
            except Exception as e:
                logger.error('Error while changing theme in ' + p.name, exc_info=e)

    config.dark_mode = dark
