#!/bin/bash
for i in {10..20..2}; do
	if [[ $((2**i)) -lt 10000 ]]; then
		echo ./heapstack $((2**i)) 500000
		./heapstack $((2**i)) 500000 
	else
		echo ./heapstack $((2**i)) 1000
		./heapstack $((2**i)) 1000
	fi
	echo ""
done
