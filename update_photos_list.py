#!/usr/bin/env python3
"""
Photo JSON Generator for Workshop Website

This script scans a directory for image files and creates a photos.json file 
that can be used by the SPADE workshop website carousel.

Usage:
    python generate_photos_json.py --photo_folder path/to/wksp-photos
"""

import os
import json
import argparse
import sys
from pathlib import Path

# Image file extensions to look for
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.JPEG', '.PNG', '.GIF', '.WEBP'}

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate photos.json for workshop website')
    parser.add_argument('--photo_folder', required=True, help='Path to the folder containing photos')
    args = parser.parse_args()
    
    photo_folder = Path(args.photo_folder)
    
    # Check if the folder exists
    if not photo_folder.exists() or not photo_folder.is_dir():
        print(f"Error: The folder '{photo_folder}' does not exist or is not a directory")
        sys.exit(1)
    
    # Scan for image files
    image_files = []
    for file in photo_folder.iterdir():
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS:
            image_files.append(file.name)
    
    # Sort the files to ensure consistent ordering
    image_files.sort()
    
    if not image_files:
        print(f"Warning: No image files found in '{photo_folder}'")
        print("The JSON file will be created but it will be empty.")
    
    # Create the JSON file
    json_path = photo_folder / 'photos.json'
    
    try:
        with open(json_path, 'w') as f:
            json.dump(image_files, f, indent=2)
        
        print(f"Successfully created photos.json with {len(image_files)} images:")
        for img in image_files:
            print(f"  - {img}")
        print(f"JSON file location: {json_path}")
        
    except Exception as e:
        print(f"Error creating JSON file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()