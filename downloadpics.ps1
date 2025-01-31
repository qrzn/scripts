# Zielordner für Downloads festlegen
$saveFolder = "J:\Sales\Verkaufsdirektion\Intern\Aushilfe\Corinna\Bilder Forms\"

# Excel-Datei Pfad festlegen
$excelFilePath = "J:\Sales\Verkaufsdirektion\Intern\Aushilfe\Corinna\Bilder Forms\Mappe1.xlsx"

# Excel-Objekt erstellen und die Datei öffnen
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false  # Excel im Hintergrund ausführen
$workbook = $excel.Workbooks.Open($excelFilePath)
$worksheet = $workbook.Sheets.Item(1)  # Ersten Arbeitsblatt auswählen

# Zeilen durchlaufen
$rowCount = $worksheet.UsedRange.Rows.Count
for ($row = 1; $row -le $rowCount; $row++) {
    # Dateiname aus Spalte G (Spalte 7) holen
    $fileName = $worksheet.Cells.Item($row, 7).Text
    
    # Zähler für fortlaufende Nummerierung zurücksetzen
    $counter = 1

    # Spalten H bis Q (Spalten 8 bis 17) durchlaufen
    for ($col = 8; $col -le 17; $col++) {
        $url = $worksheet.Cells.Item($row, $col).Text
        
        if ($url) {
            # HTTP-Anfrage, um die Datei herunterzuladen
            try {
                $webClient = New-Object System.Net.WebClient
                
                # Bild herunterladen und speichern
                $contentType = ($webClient.DownloadString($url) -match "image/") ? "image/jpeg" : ""

                if ($contentType) {
                    # Erweiterung festlegen
                    $fileExtension = ".jpg"  # Standard-Erweiterung als .jpg
                    
                    # Zielpfad für die Datei erstellen (z.B. 10675_01.jpg)
                    $targetPath = Join-Path -Path $saveFolder -ChildPath "$fileName`_02_$($counter.ToString("00"))$fileExtension"

                    # Überprüfen, ob die Datei bereits existiert und den Zähler erhöhen, wenn nötig
                    while (Test-Path $targetPath) {
                        $counter++
                        $targetPath = Join-Path -Path $saveFolder -ChildPath "$fileName`_02_$($counter.ToString("00"))$fileExtension"
                    }

                    # Datei herunterladen
                    $webClient.DownloadFile($url, $targetPath)

                    Write-Host "Heruntergeladen: $targetPath"
                }
                else {
                    Write-Host "Kein gültiges Bildformat: $url"
                }
            }
            catch {
                Write-Host "Fehler beim Herunterladen von $url: $_"
            }
            
            # Zähler erhöhen
            $counter++
        }
    }
}

# Excel-Arbeitsblatt und -Datei schließen
$workbook.Close($false)
$excel.Quit()

Write-Host "Downloads abgeschlossen!"
