# Extract Icon from EXE using Wrestool and Pillow

This Python script extracts an icon from a Windows executable (`.exe`) file on Linux by leveraging the `wrestool` utility from the icoutils package and then converts the extracted icon (ICO format) to PNG using Pillow.

## Overview

- **wrestool** (from icoutils) is used to extract icon resources from the EXE.
- **Pillow** converts the extracted ICO file to a PNG image.
- Designed primarily for Linux environments where tools like Lutris use similar methods.

## Dependencies

- **Python 3.x**
- **Pillow:** For image processing.  
  Install via pip:
  ```bash
  pip install Pillow
  ```
- **icoutils:** Provides `wrestool` to extract icons.  
  On Debian/Ubuntu:
  ```bash
  sudo apt update
  sudo apt install icoutils
  ```
  For other distributions, refer to your package manager or the [icoutils website](https://icoutils.sourceforge.net/).

## Installation

1. **Clone or Download** the repository containing `extract_icon.py` or save the script to your preferred directory.
2. **Install Dependencies** as mentioned above.

## Usage

Run the script from the terminal by passing the path to the EXE file and the desired output PNG file:

```bash
python extract_icon.py /path/to/your.exe output_icon.png
```

### What the Script Does

1. **Creates a Temporary Directory:**  
   The script uses Python’s `tempfile` module to create a temporary directory for extracted files.

2. **Extracts the Icon:**  
   It runs `wrestool` with appropriate flags to extract icon resources from the provided EXE.

3. **Converts ICO to PNG:**  
   Using Pillow, it opens the first extracted ICO file and saves it as a PNG image to the specified output path.

## Example

```bash
python extract_icon.py /home/user/apps/MyApp.exe MyAppIcon.png
```

## Troubleshooting

- **No ICO Files Extracted:**  
  Ensure the EXE actually contains icon resources. If the file lacks icons, the script will notify you.

- **Permission Issues:**  
  Check that you have read permissions for the EXE and write permissions for the output directory.

- **wrestool Not Found:**  
  Confirm that icoutils is installed correctly and that `wrestool` is in your system’s PATH.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the license terms.

## Acknowledgments

- **icoutils Project:** For providing the wrestool utility.
- **Pillow:** For enabling image processing in Python.

---

Happy extracting!