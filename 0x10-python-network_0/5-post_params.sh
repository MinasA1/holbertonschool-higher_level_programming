#!/bin/bash
#passes parameters along POST request, displays response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
