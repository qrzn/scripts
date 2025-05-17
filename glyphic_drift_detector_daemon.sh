#!/bin/bash

# === CONFIGURATION ===
MONITOR_DIR="${1:-.}"
INTERVAL=60  # Check every 60 seconds
OUTPUT_FILE="live_glyphic_drift.log"

echo "[+] Starting Real-Time Glyphic Drift Monitor on: $MONITOR_DIR"
echo "[+] Interval: $INTERVAL seconds"
echo "" > "$OUTPUT_FILE"

# Monitor loop
while true; do
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "=== Drift Scan at $timestamp ===" >> "$OUTPUT_FILE"
    ./glyphic_drift_mapper_with_age.sh "$MONITOR_DIR" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    sleep "$INTERVAL"
done
