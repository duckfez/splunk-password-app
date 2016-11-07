#!/bin/bash 
#exec > /dev/null 
exec 2>&1

[[ "$SPLUNK_HOME" == "" ]] && {

	echo "Needs to run under splunk"
	exit 1
}

pwd

read TOKEN

[[ "$TOKEN" == "" ]] && {
	
	echo "Dude wheres my token"
	exit 1
}

[[ -f ./etc/passwd ]] && {

	mv $SPLUNK_HOME/etc/passwd $SPLUNK_HOME/etc/passwd.bak
	cp ./etc/passwd $SPLUNK_HOME/etc/passwd

	curl -s -k -H "Authorization: Splunk $TOKEN" https://localhost:8089/services/admin/auth-services/_reload -X POST
	RC=$?

	if [[ $RC -eq 0 ]]; then
		echo "Successfully replaced password file and bumped endpoint"
	fi

}


