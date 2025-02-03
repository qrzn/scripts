#!/bin/bash

echo "Überprüfe, ob pacman oder ein anderer Paketmanager-Prozess läuft..."

# Überprüfen, ob pacman oder ein anderer Paketmanager-Prozess läuft
running_processes=$(pgrep -x "pacman" -o "yay" -o "trizen")

if [ -n "$running_processes" ]; then
    echo "Es läuft bereits ein Paketmanager-Prozess (PID: $running_processes). Bitte beende ihn und versuche es erneut."
    exit 1
else
    echo "Kein laufender Paketmanager-Prozess gefunden."
    
    # Überprüfen, ob die Sperrdatei existiert
    if [ -f /var/lib/pacman/db.lck ]; then
        echo "Sperrdatei gefunden. Versuche, sie zu entfernen..."
        
        # Entferne die Sperrdatei
        sudo rm /var/lib/pacman/db.lck
        
        if [ $? -eq 0 ]; then
            echo "Sperrdatei erfolgreich entfernt. Du kannst nun die Paketdatenbanken synchronisieren."
        else
            echo "Konnte die Sperrdatei nicht entfernen. Überprüfe die Berechtigungen oder starte das System neu."
            exit 1
        fi
    else
        echo "Keine Sperrdatei gefunden. Du kannst nun die Paketdatenbanken synchronisieren."
    fi
fi

