# -*- coding: utf-8 -*-
import re , sys

def sostituisci_glossario_dopo_setstretch(testo, glossario):
    # Trova la posizione di \setstretch{1.2}
    setstretch_pos = testo.find(r'\setstretch{1.2}')

    if setstretch_pos != -1:
        testo_dopo_setstretch = testo[setstretch_pos + len(r'\setstretch{1.2}'):]  # Testo dopo \setstretch{1.2}
        
        # Crea un pattern regex per il glossario escludendo le sezioni da escludere..cioè vado ad escludere dalla sostituzione tutte quelle parole contenute tra parentesi graffe
        regex = r'\b(?:' + '|'.join(r'(?<!\\)' + re.escape(parola) for parola in glossario) + r')\b(?![^{}]*\})'

        # Sostituisci il glossario escludendo le sezioni specificate
        testo_dopo_setstretch = re.sub(regex, r'\\textit{\g<0>}\\textsubscript{\\textit{G}}', testo_dopo_setstretch) # Da aggiungere il flag re.IGNORECASE
        
        # Ricostruisce il testo con la parte sostituita
        testo = testo[:setstretch_pos + len(r'\setstretch{1.2}')] + testo_dopo_setstretch
    else:
        # Crea un pattern regex per il glossario escludendo le sezioni da escludere..cioè vado ad escludere dalla sostituzione tutte quelle parole contenute tra parentesi graffe
        regex = r'\b(?:' + '|'.join(r'(?<!\\)' + re.escape(parola) for parola in glossario) + r')\b(?![^{}]*\})'

        # Sostituisci il glossario escludendo le sezioni specificate
        testo = re.sub(regex, r'\\textit{\g<0>}\\textsubscript{\\textit{G}}', testo) # Da aggiungere il flag re.IGNORECASE
        

    return testo

def leggi_file(nome_file):
    with open(nome_file, 'r') as file:
        return file.read()

def scrivi_file(nome_file, contenuto):
    with open(nome_file, 'w') as file:
        file.write(contenuto)

nome_file = sys.argv[1]
nome_file = 'Documents/' + nome_file
glossario = ["account","Account","actual cost", "analisi dei requisiti","Analisi dei Rquisiti","apache kafka","Apache Kafka","API","api","architettura","arg","artefatto","attività","best practice","big data","bit","branch","broker","browser","Browser","budget at completion","budget variance","Bug Tracking System","bug tracking system","Bug tracking system","Bullet Points","bullet points","Bullet points","customer acceptance","calendario","change management","Checklist","checklist","Chrome","chrome","Clickhouse","ClickHouse","clickhouse","clock rate","Clock Rate","Clock rate","committente","complessità ciclomatica per metodo","MCCM","configuration item","configuration management","container","Continous Integration","continous integration","Continous Integration","cost performance index","CPI","dashboard","database nosql","database","data gathering","data streaming processing","data visualization","deep dive","demo","devops","disaccoppiare","Discord","dispositivi iot","Docker","docker","Dockerfile","dockerfile","dual core CPU", "Dual-Core CPU","dual-core CPU","earned value", "Edge","edge","element","estimated at completion","EAC","estimated to complete","ETC","Faker","faker","Feature branch","feature branch", "Firefox","FireFox","firefox","fixture","Fixture","fornitore","framework","Framework","front-end","gmail","github actions","Github","github","google meet","Grafana","IDE","ID","IEEE","integrazione","IP","issue tracking system","issue","jira","json","Kafka","kafka","latex","Latex","label","librerie","Linux","linux","link","Link","log","Login","login","logout","Logout","MacOS","macos","Macos","maschera","Minimal Working Example","Minimal working example","minimal working example","milestone","mock","Mock","Modello a V","modello a V","modello a v","multi-stage builds","MVP","normalizzazione","olap","olistico","open-source","Overleaf","overleaf","paradigma","Patch","patch","pattern","pdf","peer-to-peer","Peer-to-Peer","piattaforma","PB","planned value","PV","POC","poc","PoC","processi","programma","proponente","Python","python","Pull request","pull request","pull","Pull","query","Query","raw","report","repository","requisiti contrattuali","requisiti funzionali","Requisiti funzionali","requisiti soluzione","requisiti utente","rete","roadmap","rollback","routine di codice","RTB","safari","Safari","schedule variance","scouting tecnologico","script","sensore","servizio","single responsability principle","SRP","sistema","Smart City","smart city","SnapShot","Snapshot","snapshot","Software","software","SOLID","sql","stack tecnologico","stakeholder","standard","stand-up meeting","statement coverage","MSC","stato avanzamento lavori","SAL","storage","stream processing","stream","Structural Coverage","structural coverage","stub","Stub","technology baseline","telegram","test di accettazione","test di integrazione","test di regressione","test di sistema","test di unità","Test End-to-End","test End-to-End","test end-to-end","Test end-to-end","test","tool","use case","UML","uml","unità architetturale","User Story","User story","user story","vscode","way of working","widget","Windows","windows","workflow"]

documento = leggi_file(nome_file)
documento_modificato = sostituisci_glossario_dopo_setstretch(documento, glossario)

if documento != documento_modificato:
    scrivi_file(nome_file, documento_modificato)
    print("Modifiche apportate al file")
else:
    print("Nessuna modifica effettuata")