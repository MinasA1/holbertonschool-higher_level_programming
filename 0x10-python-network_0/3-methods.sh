#!/bin/bash
#displays the methods used
curl -sI "$1" | grep Allow | cut -c 8-
