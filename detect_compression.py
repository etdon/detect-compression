import sys
import os.path

algorithms = {
    "RAR (v1.5-4.0)": [0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 0x00],
    "RAR (v5+)": [0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 0x01, 0x00],
    "7-Zip": [0x37, 0x7A, 0xBC, 0xAF, 0x27, 0x1C],
    "cpio": [0x30, 0x37, 0x30, 0x37, 0x30, 0x37],
    "tar": [0x75, 0x73, 0x74, 0x61, 0x72],
    "Zstandard": [0x28, 0xB5, 0x2F, 0xFD],
    "ZIP (Empty)": [0x50, 0x4B, 0x05, 0x06],
    "ZIP (Spanned)": [0x50, 0x4B, 0x07, 0x08],
    "ZIP": [0x50, 0x4B, 0x03, 0x04],
    "lzip": [0x4C, 0x5A, 0x49, 0x50],
    "Bink Video": [0x4B, 0x42, 0x32],
    "bzip2": [0x42, 0x5A, 0x68],
    "LZMA": [0x5D, 0x00, 0x00],
    "gzip": [0x1F, 0x8B]
}

def handle_bytes(bytes) -> tuple[str, ...]:
    for _, (key, value) in enumerate(algorithms.items()):
        if (match_expected(value, bytes)):
            return (key, value)
    match bytes[0]:
        case 0x8C:
            match bytes[1]:
                case 0x0C:
                    return ("Oodle Leviathan", [])
                case 0x0A:
                    return ("Oodle Mermaid/Selkie/Hydra", [])
                case 0x0B:
                    return ("Oodle BitKnit", [])
                case 0x06:
                    return ("Oodle Kraken", [])
                case 0x05:
                    return ("Oodle LZNA", [])
                case 0x04:
                    return ("Oodle LZA", [])
        case 0x78:
            match bytes[1]:
                case 0x01, 0x5E, 0x9C, 0xDA:
                    return ("zlib", [])
    return ("Unknown", [])

def handle_file(file_path) -> str:
    magic = []
    with open(file_path, "rb") as bufferedReader:
        magic = bufferedReader.read(8)
    return handle_bytes(magic)

def handle_hex(hex) -> str:
    return handle_bytes(bytearray.fromhex(hex))

def match_expected(expected, actual) -> bool:
    for (index, _) in enumerate(expected):
        if (expected[index] != actual[index]):
            return False
    return True

def main(args):
    if (len(args) < 2):
        print("Please provide the target file path or the hex bytes to analyse.")
        return

    user_input = sys.argv[1]
    result = None
    if (os.path.isfile(user_input)):
        try:
          result = handle_file(user_input)
        except:
            print(f"Failed to read file: {user_input}")
            return
    else:
        try:
         result = handle_hex(user_input)
        except:
            print(f"Failed to parse the provided hex bytes: {user_input}")
            return
    print(f"Detected compression algorithm: {result[0]} ({''.join(format(x, '02x') for x in result[1])})")

main(sys.argv)