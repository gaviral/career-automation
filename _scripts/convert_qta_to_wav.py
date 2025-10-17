#!/usr/bin/env python3
"""
QTA to WAV Converter
Converts QuickTime Audio (.qta) files to WAV format using pydub library.
"""

import sys
import argparse
from pathlib import Path
from pydub import AudioSegment


def convert_qta_to_wav(qta_file: str, wav_file: str = None) -> None:
    """
    Converts a QTA (QuickTime Audio) file to WAV format.

    Args:
        qta_file (str): The path to the input QTA file.
        wav_file (str): The path to the output WAV file. If None, 
                       will generate output filename based on input filename.
    """
    qta_path = Path(qta_file)
    
    # Validate input file exists
    if not qta_path.exists():
        print(f"Error: Input file '{qta_file}' does not exist.")
        sys.exit(1)
    
    # Generate output filename if not provided
    if wav_file is None:
        wav_file = str(qta_path.with_suffix('.wav'))
    
    try:
        print(f"Loading audio file: {qta_file}")
        # Load the audio file
        audio = AudioSegment.from_file(qta_file)

        print(f"Exporting to WAV format: {wav_file}")
        # Export as WAV with optimal settings for speech transcription
        audio.export(
            wav_file, 
            format="wav",
            parameters=["-ar", "16000", "-ac", "1"]  # 16kHz mono for speech
        )
        print(f"✓ Successfully converted {qta_file} to {wav_file}")

    except Exception as e:
        print(f"✗ An error occurred: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Convert QTA (QuickTime Audio) files to WAV format"
    )
    parser.add_argument(
        "input_file",
        help="Path to the input QTA file"
    )
    parser.add_argument(
        "-o", "--output",
        help="Path to the output WAV file (optional, defaults to same name with .wav extension)"
    )
    
    args = parser.parse_args()
    
    convert_qta_to_wav(args.input_file, args.output)


if __name__ == "__main__":
    main()

