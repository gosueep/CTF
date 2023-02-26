#!/bin/bash

> output.txt

for i in {1..1000}; do
    if ! (($i % 100)); then    
        echo $i
    fi
    py fish.py flowers.fish.txt >> output.txt
done

