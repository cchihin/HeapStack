#!/bin/bash
for i in {10..20..2}; do
	if [[ $((2**i)) -lt 10000 ]]; then
		echo ./serial $((2**i)) 500000
		./serial $((2**i)) 500000 
	else
		echo ./serial $((2**i)) 1000
		./serial $((2**i)) 1000
	fi
	echo ""
done
