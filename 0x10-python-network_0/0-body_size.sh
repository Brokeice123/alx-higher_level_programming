#!/bin/bash
# Script that measures the size of the body of a response
curl -sI "$1" | wc -c
