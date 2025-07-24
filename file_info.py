import os
import datetime
import json
from tqdm import tqdm

def get_file_info_single(input_file, iec_standard=False):
    try:
        st = os.stat(input_file)
    except FileNotFoundError:
        return {"error": f"File not found: {input_file}"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

    size = st.st_size

    count = 0
    if not iec_standard: # SI standard
        step = 1000
        byte_types = [
            "Bytes",
            "KB",
            "MB",
            "GB",
            "TB",
            "PB",
            "EB"
        ]
    else: # IEC standard
        step = 1024
        byte_types = [
            "Bytes",
            "KiB",
            "MiB",
            "GiB",
            "TiB",
            "PiB",
            "EiB"
        ]
    while size > step and not count == len(byte_types) - 1:
        size = size / step
        count += 1

    byte_type = byte_types[count]
    size = str(size) + " " + byte_type

    last_modification = datetime.datetime.fromtimestamp(st.st_mtime).isoformat()
    last_access = datetime.datetime.fromtimestamp(st.st_atime).isoformat()
    since_creation = datetime.datetime.fromtimestamp(st.st_ctime).isoformat()

    try:
        with open(input_file, 'r') as file:
            content = file.read()
            character_count = len(content)
            line_count = 1
            for _ in file:
                line_count += 1
    except FileNotFoundError:
        return {"error": f"File not found: {input_file}"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

    file_info = {
        "size": size,
        "path": input_file,
        "extension": os.path.splitext(input_file)[1],
        "last_modification": last_modification,
        "last_access": last_access,
        "since_creation (windows) since_metadata_change (unix)": since_creation,
        "permissions": oct(st.st_mode),
        "hard_links": st.st_nlink,
        "device": st.st_dev,
        "inode": st.st_ino,
        "uid": st.st_uid,
        "gid": st.st_gid,
        "character_count": character_count,
        "line_count": line_count
    }
    return file_info

def get_file_info_multi(directory, iec_standard=False):
    try:
        results = []
        all_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                all_files.append(filepath)

        for filepath in tqdm(all_files, desc="Processing files"):
            info = get_file_info_single(filepath, iec_standard)
            results.append(info)

    except FileNotFoundError:
        return {"error": f"Directory not found: {directory}"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}
    return results

def save_info_to_json(data, output_file):
    try:
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        return {"error": f"An error occurred: {e}"}