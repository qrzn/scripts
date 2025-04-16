package main

import (
	"fmt"
	"golang.org/x/image/ico"
	"image/png"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"path/filepath"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Printf("Usage: %s <path_to_exe> <output_png>\n", os.Args[0])
		os.Exit(1)
	}
	exePath := os.Args[1]
	outputPath := os.Args[2]

	// Create a temporary directory for extraction.
	tmpDir, err := ioutil.TempDir("", "icon_extract")
	if err != nil {
		log.Fatalf("Error creating temporary directory: %v", err)
	}
	defer os.RemoveAll(tmpDir) // Clean up temp directory

	// Run wrestool to extract icon resources (type 14) from the EXE.
	cmd := exec.Command("wrestool", "-x", "-t", "14", exePath, "-o", tmpDir)
	if err := cmd.Run(); err != nil {
		log.Fatalf("Error running wrestool: %v", err)
	}

	// Look for ICO files in the temporary directory.
	files, err := ioutil.ReadDir(tmpDir)
	if err != nil {
		log.Fatalf("Error reading temporary directory: %v", err)
	}

	var icoFile string
	for _, file := range files {
		if filepath.Ext(file.Name()) == ".ico" {
			icoFile = filepath.Join(tmpDir, file.Name())
			break
		}
	}

	if icoFile == "" {
		log.Fatalf("No ICO file extracted. The executable may not contain icon resources.")
	}

	// Open the ICO file.
	f, err := os.Open(icoFile)
	if err != nil {
		log.Fatalf("Error opening ICO file: %v", err)
	}
	defer f.Close()

	// Decode the ICO image.
	img, err := ico.Decode(f)
	if err != nil {
		log.Fatalf("Error decoding ICO file: %v", err)
	}

	// Create output PNG file.
	outFile, err := os.Create(outputPath)
	if err != nil {
		log.Fatalf("Error creating output file: %v", err)
	}
	defer outFile.Close()

	// Encode image as PNG.
	if err := png.Encode(outFile, img); err != nil {
		log.Fatalf("Error encoding PNG: %v", err)
	}

	fmt.Printf("Icon saved as %s\n", outputPath)
}
