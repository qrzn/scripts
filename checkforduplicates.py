import os
import hashlib

# Funktion zum Berechnen des Hashwerts einer Datei
def berechne_hash(dateipfad, hash_algo='sha256'):
    hash_obj = hashlib.new(hash_algo)
    
    with open(dateipfad, 'rb') as datei:
        while chunk := datei.read(8192):  # Liest die Datei in 8 KB-Chunks
            hash_obj.update(chunk)
    
    return hash_obj.hexdigest()

# Funktion zum Finden von Duplikaten
def finde_duplikate(verzeichnis):
    dateien_hashes = {}
    duplikate = []
    
    # Durchlaufe das Verzeichnis und überprüfe jede .jpg & .jpeg Datei
    for wurzel, _, dateien in os.walk(verzeichnis):
        for datei in dateien:
            if datei.lower().endswith('.jpg', '.jpeg'):
                dateipfad = os.path.join(wurzel, datei)
                hashwert = berechne_hash(dateipfad)
                
                # Wenn der Hashwert bereits existiert, sind die Dateien Duplikate
                if hashwert in dateien_hashes:
                    duplikate.append((dateien_hashes[hashwert], dateipfad))
                else:
                    dateien_hashes[hashwert] = dateipfad
    
    return duplikate

# Funktion zum Speichern der Duplikate in einer Datei
def speichere_duplikate(duplikate, dateiname='duplikate.txt'):
    with open(dateiname, 'w') as f:
        for original, duplikat in duplikate:
            f.write(f"Original: {original}\nDuplikat: {duplikat}\n\n")
    print(f"Duplikate wurden in der Datei '{dateiname}' gespeichert.")

# Beispielaufruf
verzeichnis = '/path/to/directory'  # Ändere dies auf dein Zielverzeichnis
duplikate = finde_duplikate(verzeichnis)

if duplikate:
    speichere_duplikate(duplikate)
else:
    print("Keine Duplikate gefunden.")
