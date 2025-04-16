import sys
import subprocess
import os
import tempfile
from PIL import Image

def extract_icon_using_wrestool(exe_path, output_png):
    # Create a temporary directory to hold extracted icon files.
    with tempfile.TemporaryDirectory() as tmpdir:
        # Call wrestool to extract icon group (type 14) resources.
        # The "-o" option tells wrestool to output files to the specified directory.
        command = ["wrestool", "-x", "-t", "14", exe_path, "-o", tmpdir]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print("Error extracting icon with wrestool:", e)
            return

        # Find .ico files in the temporary directory.
        ico_files = [os.path.join(tmpdir, f) for f in os.listdir(tmpdir) if f.endswith('.ico')]
        if not ico_files:
            print("No ICO files were extracted. The executable may not contain icon resources.")
            return

        # Use the first extracted ICO file.
        ico_path = ico_files[0]
        try:
            with Image.open(ico_path) as img:
                # Optionally, you can choose a specific frame/size here.
                img.save(output_png)
            print(f"Icon saved as {output_png}")
        except Exception as e:
            print("Error processing the ICO file:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_icon.py <path_to_exe> <output_image.png>")
    else:
        exe_path = sys.argv[1]
        output_png = sys.argv[2]
        extract_icon_using_wrestool(exe_path, output_png)
