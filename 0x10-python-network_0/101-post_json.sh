#!/bin/bash
# A script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl "$1" -s -X POST -H "Content-Type: appliction/json" -d @"$2"
