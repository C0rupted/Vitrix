#!/usr/bin/env bash

DIR=$(dirname "$0")

$DIR/python-env/bin/python3 $DIR/src/menu.py > log.txt
