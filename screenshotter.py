#!/usr/bin/env python3
# Take screenshots periodically
import yaml
import pyautogui
import time
import logging
import os

CONFIG_FILE = "settings.yml"


def app():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting screenshotter app")

    with open(CONFIG_FILE) as f:
        config = yaml.load(f, Loader=yaml.Loader)

    log_file = logging.FileHandler(config["logfile"])
    log_file.setLevel(logging.INFO)
    logging.getLogger("").addHandler(log_file)

    logging.info("Config:")
    logging.info(config)

    while True:
        logging.info("Taking a screenshot")
        img = pyautogui.screenshot()
        # Save screenshot with time file name

        # Check all filenames if tehre is something old
        logging.info(f"Going to sleep for {config['interval']} seconds")
        time.sleep(config["interval"])


if __name__ == "__main__":
    try:
        app()
    except Exception as e:
        logging.error(f"Exception: {e}")
