import json

# Hexagram Names (Correct list of 64 names)
hexagram_names = [
    "Qian (乾)", "Kun (坤)", "Tun (屯)", "Meng (蒙)", "Xu (需)", "Song (訟)", "Shi (師)", "Bi (比)",
    "Xiao Chu (小畜)", "Lu (履)", "Tai (泰)", "Pi (否)", "Tong Ren (同人)", "Da You (大有)", "Qian (謙)", "Yu (豫)",
    "Sui (隨)", "Gu (蠱)", "Lin (臨)", "Guan (觀)", "Shi He (噬嗑)", "Bi (賁)", "Bo (剝)", "Fu (復)",
    "Wu Wang (无妄)", "Da Chu (大畜)", "Yi (頤)", "Da Guo (大過)", "Kan (坎)", "Li (離)", "Xian (咸)", "Heng (恆)",
    "Dun (遯)", "Da Zhuang (大壯)", "Jin (晉)", "Ming Yi (明夷)", "Jia Ren (家人)", "Kui (睽)", "Jian (蹇)", "Xie (解)",
    "Sun (損)", "Yi (益)", "Guai (夬)", "Gou (姤)", "Cui (萃)", "Sheng (升)", "Kun (困)", "Jing (井)",
    "Ge (革)", "Ding (鼎)", "Zhen (震)", "Gen (艮)", "Jian (漸)", "Gui Mei (歸妹)", "Feng (豐)", "Lu (旅)",
    "Sun (巽)", "Dui (兌)", "Huan (渙)", "Jie (節)", "Zhong Fu (中孚)", "Xiao Guo (小過)", "Ji Ji (既濟)", "Wei Ji (未濟)"
]

def generate_hexagram_lines():
    """Generates a list of 64 unique hexagram line patterns using '6' and '7'."""
    hexagram_lines = []
    for i in range(64):
        binary_string = format(i, '06b')  # 6-bit binary, padded with zeros
        lines = binary_string.replace('0', '6').replace('1', '7')  # Replace 0 with 6, 1 with 7
        hexagram_lines.append(lines)
    return hexagram_lines

# Generate 64 Hexagram Sequences
king_wen_sequence = generate_hexagram_lines()


def generate_all_hexagrams() -> dict:
    hexagrams = {}
    for index, lines in enumerate(king_wen_sequence):
        name = hexagram_names[index]
        hexagram_number = index + 1

        line_interpretations_data = {}
        for line_number in range(1, 7): # Lines 1 to 6
            line_interpretations_data[str(line_number)] = {
                "line_number": line_number,
                "text": f"Interpretation for Line {line_number} of {name}. Replace with actual interpretation."
            }

        hexagram_data = {  # Always create the hexagram data
            "name": name,
            "number": str(hexagram_number).zfill(2),
            "meaning": "Meaning data not found",  # Default values here
            "image": "Image data not found",
            "judgment": "Judgment data not found",
            "description": "Description data not found",
            "lines": lines,
            "line_interpretations": line_interpretations_data
        }
        hexagrams[lines] = hexagram_data
    return hexagrams


def save_to_json(data: dict, filename: str = "hexagrams.json") -> bool:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError:
        print(f"Error: Could not save data to JSON file '{filename}'.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while saving JSON to '{filename}': {e}")
        return False


if __name__ == "__main__":
    all_hexagrams = generate_all_hexagrams()

    if save_to_json(all_hexagrams):
        print(f"Successfully generated and saved {len(all_hexagrams)} hexagrams to hexagrams.json")

        # Example access: Look up a hexagram by its lines
        lines_to_lookup = "677667"
        if lines_to_lookup in all_hexagrams:
            hexagram_info = all_hexagrams[lines_to_lookup]
            print(f"\nHexagram data for lines '{lines_to_lookup}':")
            print(json.dumps(hexagram_info, indent=4, ensure_ascii=False))
        else:
            print(f"Hexagram with lines '{lines_to_lookup}' not found in generated data.")
    else:
        print("Hexagram generation process completed but saving to file failed.")