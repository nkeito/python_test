#!/bin/bash

python3 polulate_db.py lejos

export FLASK_APP="flask_webpage/main.py"
flask run



