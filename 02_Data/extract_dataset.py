from pathlib import Path
import gzip
import shutil

ROOT=Path(__file__).resolve().parent
for folder in [ROOT/"raw", ROOT/"processed"]:
    for src in folder.glob("*.csv.gz"):
        dest=src.with_suffix("")
        print(f"Extracting {src.name} -> {dest.name}")
        with gzip.open(src,"rb") as fin, open(dest,"wb") as fout:
            shutil.copyfileobj(fin,fout)
print("Dataset extraction complete.")
