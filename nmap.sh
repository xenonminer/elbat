#!/bin/bash

if [ $# -lt 1]; then
    echo "Invalid usage: $0 <host>"
    exit
fi

HOST=$1

mkdir nmap
(set -x; nmap -p- -vvv -oN nmap/norate "${HOST}")

PORTS=cat nmap/norate | grep open | awk -F/ '{print $1}' ORS=','; echo

(set -x; nmap -p "${PORTS}" -sC -sV -oN nmap/scriptscan "${HOST}")