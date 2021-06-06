#!/bin/bash
until python aa.py; do
    echo "'aa.py' exit code $?.  Program restarting.." >&2
    sleep 1
done