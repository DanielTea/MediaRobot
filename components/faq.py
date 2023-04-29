# flake8: noqa
import streamlit as st


def faq():
    st.markdown(
        """
# FAQ
## Wie funktioniert IGMetall-Bot 2.0?
Alle Dokumente in [IGM Tarifvertäge Metall- und Elektroindustrie](https://www.bw.igm.de/tarife/thema.html?id=28&start=0), 
werden in kleinere Abschnitte unterteilt und in einer speziellen Art von Datenbank, einem sogenannten Vektorindex, 
gespeichert, der semantische Suche und Abruf ermöglicht.

Wenn Sie eine Frage stellen, sucht IGMetall-Bot 2.0 in den Dokumentabschnitten und findet die relevantesten mithilfe des Vektorindexes. 
Anschließend wird GPT3 verwendet, um eine abschließende Antwort zu generieren.

## Sind meine Daten sicher?

Ja, Ihre Daten sind sicher. IGMetall-Bot 2.0 speichert keine Daten. 
Alle hochgeladenen Daten werden gelöscht, sobald Sie den Browser-Tab schließen.

Jedoch, werden Ihre fragen an [OpenAI](www.openai.com) weitergeleitet und verarbeitet.

## Sind die Antworten 100% korrekt?
Nein, die Antworten sind nicht 100% korrekt. 
IGMetall-Bot 2.0 verwendet GPT-3, um Antworten zu generieren. 
GPT-3 ist ein leistungsstarkes Sprachmodell, 
aber es macht manchmal Fehler und neigt zu Halluzinationen. 
Außerdem verwendet IGMetall-Bot 2.0 semantische Suche, 
um die relevantesten Abschnitte zu finden und sieht nicht das gesamte Dokument, 
was bedeutet, dass es möglicherweise nicht alle relevanten Informationen finden und 
nicht alle Fragen beantworten kann (insbesondere zusammenfassende Fragen oder Fragen, die viel Kontext aus dem Dokument benötigen).

Für die meisten Anwendungsfälle ist IGMetall-Bot 2.0 jedoch sehr genau und kann die meisten Fragen beantworten. 
Überprüfen Sie immer die Quellen, um sicherzustellen, dass die Antworten korrekt sind.
"""
    )
