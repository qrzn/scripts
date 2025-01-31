Sub ExtrahiereLinks()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim cell As Range
    Dim links As Variant
    Dim i As Integer

    ' Aktuelles Arbeitsblatt festlegen
    Set ws = ThisWorkbook.Sheets("Sheet1") ' Hier den Namen des Arbeitsblatts anpassen

    ' Letzte Zeile in Spalte H ermitteln
    lastRow = ws.Cells(ws.Rows.Count, "H").End(xlUp).Row

    ' Schleife durch jede Zelle in Spalte H
    For Each cell In ws.Range("H1:H" & lastRow)
        ' Wenn die Zelle nicht leer ist
        If cell.Value <> "" Then
            ' Links anhand des Semikolons trennen
            links = Split(cell.Value, ";")
            
            ' Links in den Spalten I-Z eintragen
            For i = 0 To UBound(links)
                ' Wenn der Index kleiner als 18 ist (max. Spalte Z)
                If i < 18 Then
                    cell.Offset(0, i + 1).Value = Trim(links(i)) ' Trim entfernt mögliche Leerzeichen
                End If
            Next i
        End If
    Next cell
End Sub

