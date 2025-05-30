#!/usr/bin/env python3
import os
import argparse
from colorama import Fore, Style, init

# Inisialisasi warna (untuk Windows)
init(autoreset=True)

# Ekstensi berdasarkan jenis file
CODE_EXT = {'.php', '.html', '.css', '.js', '.py', '.java', '.cpp', '.c'}
DOC_EXT = {'.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx'}
MEDIA_EXT = {'.mp3', '.wav', '.mp4', '.mkv', '.jpg', '.png', '.jpeg', '.gif'}
EXE_EXT = {'.exe', '.msi', '.bat', '.sh'}

def get_color_for_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in CODE_EXT:
        return Fore.CYAN  # coding: biru muda
    elif ext in DOC_EXT:
        return Fore.YELLOW  # dokumen: kuning
    elif ext in MEDIA_EXT:
        return Fore.MAGENTA  # media: ungu
    elif ext in EXE_EXT:
        return Fore.RED  # executable: merah
    else:
        return Fore.WHITE  # default putih

def print_tree(root, prefix="", show_files=False):
    try:
        entries = sorted(os.listdir(root))
    except PermissionError:
        print(prefix + "└── " + Fore.RED + "[Permission Denied]" + Style.RESET_ALL)
        return

    for idx, entry in enumerate(entries):
        path = os.path.join(root, entry)
        connector = "├── " if idx < len(entries) - 1 else "└── "
        if os.path.isdir(path):
            print(prefix + connector + Fore.GREEN + entry + "/" + Style.RESET_ALL)
            new_prefix = prefix + ("│   " if idx < len(entries) - 1 else "    ")
            print_tree(path, new_prefix, show_files)
        elif show_files:
            color = get_color_for_file(entry)
            print(prefix + connector + color + entry + Style.RESET_ALL)

def main():
    parser = argparse.ArgumentParser(
        description="Baca struktur folder seperti pohon.",
        usage="bacaf [path] [-L]"
    )
    parser.add_argument("path", nargs="?", help="Folder yang ingin dibaca")
    parser.add_argument("-L", "--level", action="store_true", help="Tampilkan file juga (bukan hanya folder)")

    args = parser.parse_args()

    if not args.path:
        parser.print_help()
        return

    if not os.path.isdir(args.path):
        print(Fore.RED + f"Path '{args.path}' bukan direktori yang valid." + Style.RESET_ALL)
        return

    print(Fore.GREEN + f"{args.path}/" + Style.RESET_ALL)
    print_tree(args.path, show_files=args.level)

if __name__ == "__main__":
    main()
