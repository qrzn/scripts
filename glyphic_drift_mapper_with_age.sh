#!/bin/bash

# === CONFIGURATION ===
START_DIR="${1:-.}"
OUTPUT_FILE="glyphic_drift_map_with_age.txt"

# Glyphs
GLYPH_FOLDER="📂"
GLYPH_FILE_NEW="🟢"   # Recent file
GLYPH_FILE_OLD="🔴"   # Old file
GLYPH_COLLAPSE="⚡"

# Thresholds
COLLAPSE_THRESHOLD=10
AGE_THRESHOLD_DAYS=30  # Files modified within 30 days = "new"

# === FUNCTIONAL MODULES ===

build_glyph_map() {
    local current_dir="$1"
    local prefix="$2"

    local entries=()
    while IFS= read -r entry; do
        entries+=("$entry")
    done < <(find "$current_dir" -mindepth 1 -maxdepth 1 | sort)

    local total="${#entries[@]}"
    local count=0

    if [[ $total -ge $COLLAPSE_THRESHOLD ]]; then
        echo "${prefix}${GLYPH_COLLAPSE} $(basename "$current_dir") [$total]" >> "$OUTPUT_FILE"
    else
        echo "${prefix}${GLYPH_FOLDER} $(basename "$current_dir") [$total]" >> "$OUTPUT_FILE"
    fi

    for entry in "${entries[@]}"; do
        ((count++))
        local name=$(basename "$entry")
        local connector="├──"
        local next_prefix="$prefix│   "

        if [[ $count -eq $total ]]; then
            connector="└──"
            next_prefix="$prefix    "
        fi

        if [[ -d "$entry" ]]; then
            build_glyph_map "$entry" "$next_prefix"
        else
            # Check file modification time
            local mtime_days=$(( ( $(date +%s) - $(stat -c %Y "$entry") ) / 86400 ))
            if [[ $mtime_days -le $AGE_THRESHOLD_DAYS ]]; then
                glyph="$GLYPH_FILE_NEW"
            else
                glyph="$GLYPH_FILE_OLD"
            fi
            echo "${prefix}${connector} ${glyph} $name" >> "$OUTPUT_FILE"
        fi
    done
}

# === EXECUTION FLOW ===

echo "[+] Building glyphic drift map with age entropy from: $START_DIR"
echo "" > "$OUTPUT_FILE"

build_glyph_map "$START_DIR" ""

echo "[✔] Glyphic drift map saved to: $OUTPUT_FILE"
