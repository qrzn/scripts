@echo off
setlocal enabledelayedexpansion

:: Zielordner für Downloads festlegen
set "saveFolder=C:\Users\Aushilfe-VD-DE\Desktop\test\"

:: Pfad zur Textdatei mit den URLs (diese sollte die URLs enthalten, eine pro Zeile)
set "urlFile=C:\Users\Aushilfe-VD-DE\Desktop\Mappe1.csv"

:: Durch jede Zeile der Textdatei iterieren
for /f "tokens=*" %%A in (%urlFile%) do (
    set "url=%%A"
    if not "!url!"=="" (
        :: Dateiname aus der URL extrahieren (z.B. https://example.com/image.jpg => image.jpg)
        for %%B in (!url!) do set "fileName=%%~nxB"
        
        :: Zielpfad für die Datei erstellen (z.B. 10675_01.jpg)
        set "targetPath=%saveFolder%!fileName!"

        :: Überprüfen, ob die Datei bereits existiert und fortlaufend umbenennen
        set /a counter=1
        :checkExistence
        if exist "!targetPath!" (
            set "targetPath=%saveFolder%!fileName!_!counter!.jpg"
            set /a counter+=1
            goto checkExistence
        )

        :: Datei mit curl herunterladen (falls curl installiert ist)
        curl -o "!targetPath!" "!url!"

        :: Erfolgsmeldung
        echo Heruntergeladen: !targetPath!
    )
)

:: Abschlussmeldung
echo Downloads abgeschlossen!
pause
