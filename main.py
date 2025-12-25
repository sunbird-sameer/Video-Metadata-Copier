import os
import subprocess
import glob

def copy_metadata(folder_path):
    encoded_files = glob.glob(os.path.join(folder_path, "*_encoded.mp4"))
    
    for encoded_file in encoded_files:
        base_name = os.path.basename(encoded_file).replace("_encoded.mp4", ".mp4")
        original_file = os.path.join(folder_path, base_name)
        
        if os.path.exists(original_file):
            try:
                # Copy ALL metadata + filesystem dates explicitly
                cmd = [
                    "exiftool",
                    "-overwrite_original",
                    "-tagsfromfile", original_file,
                    "-all:all",
                    "-FileCreateDate",
                    "-FileModifyDate",
                    encoded_file
                ]
                subprocess.run(cmd, check=True, capture_output=True)
                print(f"Copied metadata + creation time: {base_name} -> {os.path.basename(encoded_file)}")
            except subprocess.CalledProcessError as e:
                print(f"Error: {encoded_file}: {e}")
        else:
            print(f"Original missing: {original_file}")

# Run in your folder
if __name__ == "__main__":
    folder_path = "."  # Change to your path
    copy_metadata(folder_path)
