#!/bin/bash
#server must respone You got me! -L to redirect, -X PUT
curl -sLX 'PUT' -d 'user_id=98' -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
