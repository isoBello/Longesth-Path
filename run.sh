#!/usr/bin/env bash

. venv/bin/activate

declare -i count
ants="10 25 50 75 100"
iterations="50 75 85 95 100"
evaporation="0.005 0.01 0.05 0.075 0.095"
q=0.001
alpha="1 0.5 1 1 1.25"
beta="1 1 0.5 1.25 1.0"
files="Grafos/entrada1.txt Grafos/entrada2.txt Grafos/entrada3.txt"
count=0

for file in $files; do
  for b in $beta; do
    for a in $alpha; do
      for e in $evaporation; do
        for i in $iterations; do
          for ant in $ants; do
            count=0
            while [ $count -le 3 ]
            do
              python3 Main.py "$file" "$ant" "$i" "$e" "$q" "$a" "$b"
              count=$(( count + 1 ))
            done
          done
        done
      done
    done
  done
done

