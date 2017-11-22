#!/bin/bash
#displays the status code of response
curl -sH "Content-Type: application/json" -d "$2" "$1"
