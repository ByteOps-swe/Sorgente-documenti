path="RTB/Sottosezioni/Norme_di_progetto/Glossario.tex"

if [[ $path == */Sezioni/*.tex || $path == */Sottosezioni/*.tex ]]; then
    echo "Sono fuori dal tunnel"
    father_dir=$(dirname "$path")
    doc_name=$(basename "$father_dir")
    if [[ $doc_name == "Norme_di_progetto" ]]; then
        has_changes[0]=true
    elif [[ $doc_name == "Piano_di_progetto" ]]; then
        has_changes[1]=true
    elif [[ $doc_name == "Analisi_dei_requisiti" ]]; then
        has_changes[2]=true
    fi
fi

if [ "${has_changes[0]}" == "true" ]; then
    echo "Il documento è Norme_di_progetto"
elif [ "${has_changes[1]}" == "true" ]; then
    echo "Il documento è Piano_di_progetto"
elif [ "${has_changes[2]}" == "true" ]; then
    echo "Il documento è Analisi_dei_requisiti"
fi
