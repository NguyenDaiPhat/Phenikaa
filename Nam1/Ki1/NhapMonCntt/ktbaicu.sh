#!/bin/bash
echo "Nguyen Dai Phat"
for i in $( seq 1 50 ); do
	if [ $(( i % 3 )) -eq 0 ]; then 
		mkdir dir_"$i"_fizz
	elif [ $(( i % 5 )) -eq 0 ]; then 
		mkdir dir_"$i"_buzz
	elif [ $(( i % 3 )) -eq 0 ] && [ $(( i % 5 )) -eq 0 ]; then
		mkdir dir_"$i"_fizzbuzz
	else mkdir dir_"$i"_nofizzbuzz
	fi
done
