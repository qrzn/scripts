#!/bin/bash

# === CONFIGURATION ===
START_DIR="${1:-.}"
OUTPUT_FILE="glyphic_drift_map.txt"

# Glyphs
GLYPH_FOLDER="📂"
GLYPH_FILE="📄"
GLYPH_COLLAPSE="⚡"   # Symbol for collapse points (e.g., folder with heavy file density)

# Thresholds
COLLAPSE_THRESHOLD=10  # Collapse if directory has more than N items

# === FUNCTIONAL MODULES ===

# Recursive glyph drift builder
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
            echo "${prefix}${connector} ${GLYPH_FILE} $name" >> "$OUTPUT_FILE"
        fi
    done
}

# === EXECUTION FLOW ===

echo "[+] Building glyphic drift field from: $START_DIR"
echo "" > "$OUTPUT_FILE"

build_glyph_map "$START_DIR" ""

echo "[✔] Glyphic drift map saved to: $OUTPUT_FILE"
