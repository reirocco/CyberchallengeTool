#!/bin/bash

while true;
do
	nc -v -l -p 18211 >> out.txt
done

