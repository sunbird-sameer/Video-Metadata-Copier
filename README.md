# Video Metadata Copier

Python script to batch copy **all metadata** (EXIF, XMP, QuickTime tags + filesystem creation/modified dates) from original videos to their encoded copies (`original.mp4` → `original_encoded.mp4`).

## Features
- Copies embedded metadata (`-all:all`) and filesystem timestamps (`FileCreateDate`, `FileModifyDate`)
- Processes entire folders automatically
- Supports MP4, MOV, and other ExifTool-compatible formats
- Safe overwrites with backup creation (ExifTool default)
- Verbose logging for verification

## Requirements
- **Python 3.6+** (uses `subprocess`, `glob`, `os`)
- **ExifTool** installed and in PATH: https://exiftool.org/

## Installation
```bash
# Install ExifTool (Ubuntu/Debian)
sudo apt install exiftool

# macOS (Homebrew)
brew install exiftool

# Windows: Download from https://exiftool.org/ and add to PATH
```

## Usage
1. Place `copy_metadata.py` in your media folder (with `original.mp4` and `original_encoded.mp4` pairs)
2. Run: `python copy_metadata.py [folder_path]`
3. **Verify**: `exiftool -time:all original.mp4` vs `exiftool -time:all original_encoded.mp4`

```bash
cd /path/to/your/videos
python copy_metadata.py
```

## What Gets Copied
| Category | Tags | Examples |
|----------|------|----------|
| **Embedded** | `-all:all` | CreateDate, GPS, CameraMake, Title, Keywords |
| **Filesystem** | `-FileCreateDate`, `-FileModifyDate` | Windows/macOS creation time |
| **QuickTime/MP4** | TrackCreateDate, MediaCreateDate | Video timeline dates |

## What Does NOT Copy
- Tags missing from original file
- Format-incompatible tags (AVI-specific → MP4)
- Pure filesystem attributes (permissions, ACLs, NTFS streams)

## Verification Commands
```bash
# Compare timestamps
exiftool -G1 -time:all original.mp4 original_encoded.mp4

# Full metadata diff
exiftool -a -u -G1 -s original.mp4 > orig.txt
exiftool -a -u -G1 -s original_encoded.mp4 > enc.txt
diff orig.txt enc.txt
```

## Troubleshooting
| Issue | Solution |
|-------|----------|
| `exiftool: command not found` | Install ExifTool and add to PATH |
| No metadata copied | Run `exiftool original.mp4` - original has no metadata |
| Permission denied | Run with `sudo` or check file locks |
| Only some tags copied | MP4 format limitation |

## License
MIT License - use freely, credit appreciated.

## Credits
Built with [ExifTool](https://exiftool.org/) by Phil Harvey
