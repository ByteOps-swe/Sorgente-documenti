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
        testo_dopo_setstretch = re.sub(regex, r'\\textit{\g<0>}\\textsubscript{\\textit{G}}', testo_dopo_setstretch, flags=re.IGNORECASE) # Da aggiungere il flag re.IGNORECASE
        
        # Ricostruisce il testo con la parte sostituita
        testo = testo[:setstretch_pos + len(r'\setstretch{1.2}')] + testo_dopo_setstretch
    else:
        # Crea un pattern regex per il glossario escludendo le sezioni da escludere..cioè vado ad escludere dalla sostituzione tutte quelle parole contenute tra parentesi graffe
        regex = r'\b(?:' + '|'.join(r'(?<!\\)' + re.escape(parola) for parola in glossario) + r')\b(?![^{}]*\})'

        # Sostituisci il glossario escludendo le sezioni specificate
        testo = re.sub(regex, r'\\textit{\g<0>}\\textsubscript{\\textit{G}}', testo, flags=re.IGNORECASE) # Da aggiungere il flag re.IGNORECASE
        

    return testo

def leggi_file(nome_file):
    with open(nome_file, 'r') as file:
        return file.read()

def scrivi_file(nome_file, contenuto):
    with open(nome_file, 'w') as file:
        file.write(contenuto)

nome_file = sys.argv[1]
if "Glossario.tex" in nome_file:
    print("Gloassario.tex non puo' avere G a pedice")
    sys.exit()
nome_file = 'Documents/' + nome_file
glossario = ["account","actual cost", "analisi dei requisiti","apache kafka","api","architettura","arg","artefatto","attività","best practice","big data","bit","feature branch","branch","broker","browser","budget at completion","BAC","budget variance","BV","bug tracking system","bullet points","customer acceptance","CA","calendario","change management","checklist","chrome","clickhouse","clock rate","committente","complessità ciclomatica per metodo","MCCM","configuration item","configuration management","container","continuous integration","cost performance index","CPI","dashboard","database nosql","database sql","database","data gathering","data streaming processing","data visualization","deep dive","demo","devops","disaccoppiare","discord","dispositivi iot","dockerfile","docker","dual core CPU","dual-core CPU","earned value","EV","microsoft edge","edge","element","estimated at completion","EAC","estimated to complete","ETC","faker","firefox","fixture","fornitore","framework","front-end","gmail","github actions","github","git","google meet","grafana","ID","IDE","IEEE","integrazione","IP","issue tracking system","issue","ITS","jira","json","kafka","latex","label","librerie","linux","link","log","login","logout","macos","maschera","minimal working example","milestone","mock","modello a v","multi-stage builds","MVP","normalizzazione","olap","olistico","open source","open-source","overleaf","paradigma","patch","pattern","pdf","peer-to-peer","piattaforma","PB","planned value","PV","poc","processi","programma","proponente","python","pull request","pull","query","raw","report","repository","requisiti contrattuali","requisiti funzionali","requisiti soluzione","requisiti utente","rete","roadmap","rollback","routine di codice","RTB","safari","schedule variance","scouting tecnologico","script","sensore","servizio","single responsability principle","SRP","sistema","smart city","snapshot","software","SOLID","sql","stack tecnologico","stakeholder","standard","stand-up meeting","statement coverage","MSC","stato avanzamento lavori","SAL","storage","stream processing","stream","structural coverage","stub","technology baseline","telegram","test di accettazione","test di integrazione","test di regressione","test di sistema","test di unità","test end-to-end","test","tool","use case","uml","unità architetturale","user story","vscode","way of working","widget","windows","workflow"]
sys.exit()
documento = leggi_file(nome_file)
documento_modificato = sostituisci_glossario_dopo_setstretch(documento, glossario)

if documento != documento_modificato:
    scrivi_file(nome_file, documento_modificato)
    print("Modifiche apportate al file")
else:
    print("Nessuna modifica effettuata")