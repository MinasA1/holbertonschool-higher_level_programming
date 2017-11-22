#!/bin/bash
#displays the status code of response
curl -sI -o /dev/null -w "%{http_code}" "$1"
