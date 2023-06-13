#!/bin/bash
for i in $(seq 1 30 ); do
	if [ $(( i % 3 )) -eq 0 ]; then
		mkdir thu_muc_so_$i
	fi
done
