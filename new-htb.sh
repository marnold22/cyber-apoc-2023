#!/bin/bash

mkdir $1
cd $1
touch README.md
$(echo -e "# $1\n\n## FLAG: HTB{}\n\n## Status: Incomplete\n\n+ DOCKER: $2\n+ DOWNLOADABLE: $3\n\nDescription: $4\n\n## NOTES" > README.md)
