path='RTB/Sottosezioni/Norme_di_progetto/Glossario.tex'


# if [ "${has_changes[0]}" == "true" ]; then
#     echo "Il documento è Norme_di_progetto"
# elif [ "${has_changes[1]}" == "true" ]; then
#     echo "Il documento è Piano_di_progetto"
# elif [ "${has_changes[2]}" == "true" ]; then
#     echo "Il documento è Analisi_dei_requisiti"
# fi

declare -a has_changes
has_changes=(0 0 0)

for ((i=1; i<=5; i++)); do
    if [[ $path == */Sezioni/*.tex || $path == */Sottosezioni/*.tex ]]; then
        echo "Sono fuori dal tunnel"
        father_dir=$(dirname "$path")
        doc_name=$(basename "$father_dir")
        echo $doc_name
        if [[ $doc_name == "Norme_di_progetto" ]]; then
            has_changes[0]=1
            echo ${has_changes[0]}
        elif [[ $doc_name == "Piano_di_progetto" ]]; then
            has_changes[1]=1
        elif [[ $doc_name == "Analisi_dei_requisiti" ]]; then
            has_changes[2]=1
        fi
    fi
    echo "Iterazione $i"
done

for change in "${has_changes[@]}"; do
    echo "$change"
done

if [[ "${has_changes[0]}" -eq "1" ]]; then
    echo "diocan"
else
    echo "porcodio"
fi
