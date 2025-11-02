#!/usr/bin/bash

function test() {
	if [[ "$line" =~ ^\([0-9]{3}\)\ [0-9]{3}-[0-9]{4}$ || \
              "$line" =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
		return 0
	else
		return 1
	fi
}

while read line; do
	if test "$line"; then
		echo "$line"
	fi
done < ./file.txt

