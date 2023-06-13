#!/bin/bash
echo "Nguyen Dai Phat"
for i in $( seq 1 50 ); do
	if [ $(( i % 3 )) -eq 0 ]; then 
		mkdir dir_"$i"_fizz
        fi
	if [ $(( i % 5 )) -eq 0 ]; then 
		mkdir dir_"$i"_buzz
        fi
	if [ $(( i % 3 )) -eq 0 ] && [ $(( i % 5 )) -eq 0 ]; then
		mkdir dir_"$i"_fizzbuzz
	elif [ $(( i % 3 )) -eq 0 ] && [ $(( i % 5 )) -eq 0 ]; then
                mkdir dir_"$i"_nofizzbuzz
	fi
done
