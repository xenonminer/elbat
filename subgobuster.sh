#!/bin/bash

if [ $# -lt 1]; then
    echo "Invalid usage: $0 <host>"
    exit
fi

HOST=$1

(set -x; gobuster vhost -u "${HOST}" -w "/usr/share/SecLists/Discovery/DNS/subdomains-top1million-20000.txt")