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
    """Generates a list of 64 unique hexagram line patterns."""
    hexagram_lines = []
    for i in range(64):
        binary_string = format(i, '06b') # 6-bit binary, padded with zeros
        lines = binary_string.replace('0', '6').replace('1', '7') # Replace 0 with 6, 1 with 7
        hexagram_lines.append(lines)
    return hexagram_lines

# Generate 64 Hexagram Sequences
king_wen_sequence = generate_hexagram_lines()


def generate_hexagram_data(lines: str, name: str, number: int, source_data: dict) -> dict:
    """
    Generates data for a single hexagram by extracting information from the source data.
    If source data is not found, provides default "not found" messages.
    """
    hexagram_source = source_data.get(lines)  # Safely get hexagram data, returns None if not found
    if hexagram_source:
        meaning = hexagram_source.get("meaning", "Meaning data not found in source")
        image = hexagram_source.get("image", "Image data not found in source")
        judgment = hexagram_source.get("judgment", "Judgment data not found in source")
        description = hexagram_source.get("description", "Description data not found in source")
    else:
        meaning = "Meaning data not found"
        image = "Image data not found"
        judgment = "Judgment data not found"
        description = "Description data not found"
        print(f"Warning: Hexagram '{name}' ({lines}) not found in source JSON.")

    return {
        "name": name,
        "number": str(number).zfill(2),
        "meaning": meaning,
        "image": image,
        "judgment": judgment,
        "description": description,
        "lines": lines
    }


def generate_all_hexagrams(source_data: dict) -> dict:
    """
    Generates data for all 64 hexagrams based on generated sequences and names,
    regardless of source data content. If source data is missing for a hexagram,
    default "not found" messages are used.
    """
    hexagrams = {}
    for index, lines in enumerate(king_wen_sequence):
        name = hexagram_names[index]
        hexagram_number = index + 1  # Hexagram numbers are 1-indexed
        hexagram_data = generate_hexagram_data(lines, name, hexagram_number, source_data)
        hexagrams[lines] = hexagram_data  # Use lines as key for easy lookup
    return hexagrams


def load_json_data(filename: str) -> dict or None:
    """
    Loads JSON data from the specified file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: Source JSON file not found at '{filename}'. Using default data.")
        return {} # Return empty dict if file not found so that default data is used in generate_hexagram_data
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'. Please check the file. Using default data.")
        return {} # Return empty dict for JSON decode error, to use default data
    except Exception as e:
        print(f"An unexpected error occurred while loading JSON from '{filename}': {e}. Using default data.")
        return {} # Return empty dict for other errors, to use default data


def save_to_json(data: dict, filename: str = "hexagrams.json") -> bool:
    """
    Saves the provided data to a JSON file.
    """
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
    source_filename = "source_hexagrams.json"

    source_data = load_json_data(source_filename) # load_json_data now returns {} instead of None in case of errors, to facilitate default data usage

    all_hexagrams = generate_all_hexagrams(source_data) # source_data will be {} if loading failed, so default data will be used

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