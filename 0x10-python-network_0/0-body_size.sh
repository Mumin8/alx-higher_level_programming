#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
curl -Ls "$1" | wc -c
