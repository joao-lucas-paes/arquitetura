#!/bin/bash


while IFS= read -r line; do
    prefix="${line%%-*}" 
    suffix="${line#*-}"
    dir="./$prefix/$suffix"

    if [ ! -d "$dir" ]; then
        echo "Diretório $dir não existe. Criando..."
        mkdir -p "$dir"
        echo "Diretório $dir criado com sucesso!"
    else
        echo "Diretório $dir já existe."
    fi

    for ((ncore = 9; ncore <= 32; ncore++)); do
        ./run-sniper -d $dir/$ncore/small --benchmarks=$prefix-$suffix-small-$ncore -c nehalem-lite  
    done

    
done < testes
