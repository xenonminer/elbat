#!/bin/bash

if [ $# -lt 1]; then
    echo "Invalid usage: $0 <host>"
    exit
fi

HOST=$1

(set -x; gobuster dir -u "${HOST}" -w "/usr/share/SecLists/Discovery/Web-Content/raft-large-words-lowercase.txt" -b "404" "${@:2}")