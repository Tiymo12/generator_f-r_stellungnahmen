
import streamlit as st

st.set_page_config(page_title="Stellungnahme-Generator", layout="wide")

st.title("📝 Stellungnahme-Generator für Finanzierungen")

# Auswahl der Finanzierungsart
finanzierungsart = st.radio("Art der Finanzierung", ["Wohnbaufinanzierung", "Konsumkredit"])

st.subheader("1. Antragszweck")
kaufpreis = st.text_input("Kaufpreis (in TEUR)")
nebenkosten = st.text_input("Nebenkosten (in TEUR)")
sanierung = st.text_input("Sanierungskosten (in TEUR)")
eigenmittel = st.text_input("Eigenmittel (in TEUR)")
finanzierungsvolumen = st.text_input("Finanzierungsvolumen (in TEUR)")
konditionen = st.text_area("Konditionen (Zinssatz, Laufzeit, Sondertilgungen etc.)")

st.subheader("2. Person des Kreditnehmers")
familienstand = st.text_input("Familienstand")
kinder = st.text_input("Kinder (inkl. Geburtsjahre)")
wohnort = st.text_input("Wohnsituation / Wohnort")
beruf = st.text_input("Beruf & Arbeitgeber")
einkommen = st.text_input("Nettoeinkommen (monatlich)")
beschaeftigt_seit = st.text_input("Beschäftigt seit")
weitere_einkuenfte = st.text_input("Weitere Einkünfte (z. B. Kindergeld, Mieteinnahmen)")

st.subheader("3. Kundenbeziehung & Kontoverhalten")
kunde_seit = st.text_input("Kunde seit")
hauptbank = st.text_input("Hauptbankverbindung")
kontoverhalten = st.text_input("Kontoverhalten")
produkte = st.text_input("Produktdurchdringung (Giro, Spar, WP etc.)")
rating = st.text_input("Rating")

st.subheader("4. Haushaltsrechnung & externe Auskünfte")
haushaltsrechnung = st.text_input("Ergebnis der Haushaltsrechnung (Überschuss/Unterdeckung)")
besonderheiten = st.text_input("Besonderheiten (Karenz, Pension etc.)")
crif = st.text_input("CRIF-Abfrage (ja/nein, Einträge?)")
ksv = st.text_input("KSV (z. B. 0, 1)")
ukv = st.text_input("UKV")
cm2 = st.text_area("CM2-Daten (Jahressummen und YTD)")
cm4 = st.text_area("CM4-Daten (Jahressummen und YTD)")
kbs = st.text_input("KBS-Wert nach Finanzierung")

st.subheader("5. Finanzielle Schwierigkeiten / Forbearance")
finanzielle_schwierigkeiten = st.text_area("Hinweise auf finanzielle Schwierigkeiten")

st.subheader("6. Sicherheiten")
sicherheiten = st.text_area("Liste der Sicherheiten")

st.subheader("7. Gesamturteil & Empfehlung")
empfehlung = st.text_area("Empfehlung / Bewilligung mit Begründung")

if st.button("Stellungnahme generieren"):
    st.subheader("📝 Generierte Stellungnahme")
    st.markdown(f"""
**Art der Finanzierung:** {finanzierungsart}

**Antragszweck:**  
Der Kredit über {finanzierungsvolumen} TEUR dient zur Finanzierung eines Projekts mit folgenden Kosten:  
- Kaufpreis: {kaufpreis} TEUR  
- Nebenkosten: {nebenkosten} TEUR  
- Sanierung: {sanierung} TEUR  
- Eigenmittel: {eigenmittel} TEUR  
Konditionen: {konditionen}

**Person des Kreditnehmers:**  
{familienstand}, {kinder}, wohnhaft in {wohnort}.  
Beruf: {beruf}, Einkommen: {einkommen}, beschäftigt seit {beschaeftigt_seit}.  
Weitere Einkünfte: {weitere_einkuenfte}

**Kundenbeziehung & Kontoverhalten:**  
Kunde seit {kunde_seit}, Hauptbank: {hauptbank}.  
Kontoverhalten: {kontoverhalten}, Produkte: {produkte}, Rating: {rating}

**Haushaltsrechnung & externe Auskünfte:**  
Haushaltsrechnung: {haushaltsrechnung}, Besonderheiten: {besonderheiten}  
CRIF: {crif}, KSV: {ksv}, UKV: {ukv}  
CM2: {cm2}  
CM4: {cm4}  
KBS: {kbs}

**Finanzielle Schwierigkeiten / Forbearance:**  
{finanzielle_schwierigkeiten}

**Sicherheiten:**  
{sicherheiten}

**Gesamturteil & Empfehlung:**  
{empfehlung}
""")
