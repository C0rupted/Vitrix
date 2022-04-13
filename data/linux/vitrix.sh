#!/usr/bin/env bash

DIR=$(dirname "$0")

$DIR/python-env/bin/python3 $DIR/vitrix/menu.py > log.txt
