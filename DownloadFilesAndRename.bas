Sub DownloadFilesAndRename()
    Dim ws As Worksheet
    Dim row As Long, col As Long
    Dim url As String
    Dim saveFolder As String
    Dim fileName As String
    Dim http As Object
    Dim fileNum As Integer
    Dim fileData() As Byte
    Dim targetPath As String
    Dim contentType As String
    Dim fileExtension As String
    Dim counter As Long

    ' Arbeitsblatt zuweisen
    Set ws = ThisWorkbook.Sheets(1)  ' Ändere dies, wenn du ein anderes Blatt verwenden möchtest

    ' Zielordner für Downloads festlegen
    saveFolder = "J:\Sales\Verkaufsdirektion\Intern\Aushilfe\Corinna\Bilder Forms\" ' Pfad für den Speicherort anpassen

    ' Durch alle Zeilen iterieren (ab Zeile 1, falls Zeile 1 Header ist, For row = 1 in 2 ändern)
    For row = 1 To ws.UsedRange.Rows.Count
        ' Datei-Name aus Spalte G holen
        fileName = ws.Cells(row, 7).Value ' Spalte G ist die 7. Spalte

        ' Schleife durch Spalten H bis Q (Spalten 8 bis 17)
        counter = 1  ' Zähler für die fortlaufende Nummerierung
        For col = 8 To 17 ' Spalten H bis Q
            url = ws.Cells(row, col).Value ' Link aus der Zelle holen
            
            If url <> "" Then
                ' HTTP-Anfrage erstellen
                Set http = CreateObject("MSXML2.XMLHTTP")
                http.Open "GET", url, False
                http.Send

                If http.Status = 200 Then
                    ' Content-Type des Responses ermitteln
                    contentType = http.getResponseHeader("Content-Type")
                    
                    ' Überprüfen, ob es sich um ein JPEG-Bild handelt
                    If InStr(contentType, "image/jpeg") > 0 Then
                        fileExtension = ".jpg"
                    Else
                        ' Falls der Content-Type nicht "image/jpeg" ist, weiter behandeln
                        fileExtension = ".jpg"  ' Standard auf .jpg setzen (oder du kannst eine andere Erweiterung setzen)
                    End If

                    ' Zielpfad für die Datei erstellen (z.B. 10675_01.jpg)
                    targetPath = saveFolder & fileName & "_02_" & Format(counter, "00") & fileExtension

                    ' Überprüfen, ob die Datei bereits existiert, falls ja, Zähler erhöhen
                    Do While Dir(targetPath) <> ""
                        counter = counter + 1
                        targetPath = saveFolder & fileName & "_02_" & Format(counter, "00") & fileExtension
                    Loop

                    ' Datei herunterladen und speichern
                    fileData = http.responseBody
                    fileNum = FreeFile
                    Open targetPath For Binary Access Write As #fileNum
                    Put #fileNum, 1, fileData
                    Close #fileNum

                    Debug.Print "Heruntergeladen: " & targetPath
                Else
                    Debug.Print "Fehler bei: " & url & " (Status: " & http.Status & ")"
                End If
                
                ' Zähler erhöhen
                counter = counter + 1
            End If
        Next col
    Next row

    MsgBox "Downloads abgeschlossen!"
End Sub

