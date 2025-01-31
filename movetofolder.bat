@echo off
setlocal enabledelayedexpansion

:: Eine neue Datei für die Liste der verschobenen Dateien erstellen (oder überschreiben, falls sie bereits existiert)
echo Liste der verschobenen Dateien > verschobene_dateien.txt

:: Durch alle .jpg-Dateien im aktuellen Verzeichnis iterieren
for %%f in (*_*_*.jpg) do (
    :: Den Basisnamen extrahieren (alles vor dem ersten Unterstrich)
    set filename=%%~nf
    for /f "tokens=1 delims=_" %%a in ("!filename!") do set base=%%a

    :: Überprüfen, ob der Ordner mit dem Basisnamen bereits existiert
    if not exist "!base!" (
        mkdir "!base!"
    )

    :: Datei in den entsprechenden Ordner verschieben
    move "%%f" "!base!\"

    :: Die verschobene Datei in die Liste schreiben
    echo %%f wurde nach "!base!\" verschoben. >> verschobene_dateien.txt
)

echo Fertig! Eine Liste der verschobenen Dateien wurde in verschobene_dateien.txt erstellt.
pause
