# -*- coding: utf-8 -*-
import re , sys

def sostituisci_glossario_dopo_setstretch(testo, glossario):
    # Trova la posizione di \setstretch{1.2}
    setstretch_pos = testo.find(r'\setstretch{1.2}')

    if setstretch_pos != -1:
        testo_dopo_setstretch = testo[setstretch_pos + len(r'\setstretch{1.2}'):]  # Testo dopo \setstretch{1.2}
        
        # Crea un pattern regex per il glossario escludendo le sezioni da escludere..cioè vado ad escludere dalla sostituzione tutte quelle parole contenute tra parentesi graffe
        regex = r'\b(?:' + '|'.join(re.escape(parola) for parola in glossario) + r')\b(?![^{}]*\})'

        # Sostituisci il glossario escludendo le sezioni specificate
        testo_dopo_setstretch = re.sub(regex, r'\\textit{\g<0>}\\textsubscript{\\textit{G}}', testo_dopo_setstretch)
        
        # Ricostruisce il testo con la parte sostituita
        testo = testo[:setstretch_pos + len(r'\setstretch{1.2}')] + testo_dopo_setstretch
    else:
        # Crea un pattern regex per il glossario escludendo le sezioni da escludere..cioè vado ad escludere dalla sostituzione tutte quelle parole contenute tra parentesi graffe
        regex = r'\b(?:' + '|'.join(re.escape(parola) for parola in glossario) + r')\b(?![^{}]*\})'

        # Sostituisci il glossario escludendo le sezioni specificate
        testo = re.sub(regex, r'\\textit{\g<0>}\\textsubscript{\\textit{G}}', testo)
        

    return testo

def leggi_file(nome_file):
    with open(nome_file, 'r') as file:
        return file.read()

def scrivi_file(nome_file, contenuto):
    with open(nome_file, 'w') as file:
        file.write(contenuto)

nome_file = 'RTB/Sezioni/Norme_di_progetto/Metriche_di_qualita.tex'
# nome_file = 'Documents/' + nome_file
glossario = ["actual cost", "analisi dei requisiti","apache kafka","API","architettura","arg","artefatto","attività","best practice","big data","bit","branch","broker","budget at completion","budget variance","customer acceptance","calendario","change management","Clickhouse","committente","complessità ciclomatica per metodo","MCCM","configuration item","configuration management","container","cost performance index","CPI","dashboard","database","database nosql","data gathering","data streaming processing","data visualization","deep dive","demo","devops","disaccoppiare","Discord","dispositivi iot","Docker","Dockerfile","earned value","element","estimated at completion","EAC","estimated to complete","ETC","Faker","Feature branch","fornitore","framework","front-end","gmail","github","github actions","google meet","Grafana","ID","IEEE","integrazione","issue","issue tracking system","jira","json","latex","label","librerie","log","maschera","milestone","multi-stage builds","MVP","normalizzazione","olap","olistico","open-source","overleaf","paradigma","pattern","pdf","piattaforma","PB","planned value","PV","POC","processi","programma","proponente","python","pull request","raw","report","repository","requisiti contrattuali","requisiti soluzione","requisiti utente","rete","roadmap","rollback","routine di codice","RTB","schedule variance","scouting tecnologico","script","sensore","servizio","single responsability principle","SRP","sistema","smart city","software","SOLID","sql","stack tecnologico","stakeholder","standard","stand-up meeting","statement coverage","MSC","stato avanzamento lavori","SAL","storage","stream","stream processing","technology baseline","telegram","test","test di accettazione","test di integrazione","test di regressione","test di sistema","test di unità","tool","use case","uml","unità architetturale","vscode","way of working","widget","workflow"]

documento = leggi_file(nome_file)
documento_modificato = sostituisci_glossario_dopo_setstretch(documento, glossario)

if documento != documento_modificato:
    scrivi_file(nome_file, documento_modificato)
    print("Modifiche apportate al file")
else:
    print("Nessuna modifica effettuata")