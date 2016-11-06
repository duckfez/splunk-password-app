#!/bin/bash 
exec > /dev/null 2>&1

read TOKEN
mv $SPLUNK_HOME/etc/passwd $SPLUNK_HOME/etc/passwd.bak
cp ./etc/passwd $SPLUNK_HOME/etc/passwd
curl -k -H "Authorization: Splunk $TOKEN" https://localhost:8089/services/admin/auth-services/_reload -X POST
