import os
import pprint
from pathlib import Path

def write(path: Path, text:str):
    with path.open("w") as f:
        f.write(text)

def read(path: Path) -> str:
    with path.open() as f:
        return f.read()

def copy(fromPath: Path, toPath:Path):
    text = read(fromPath)
    write(toPath, text)

def insert_subs_filter(path:Path):

    def subs_filter(prefix: str, key: str, value: str) -> str:
        return f"{prefix}subs_filter \"{{{{ {key.upper()} }}}}\" {value};"

    keys = [x for x in os.environ.keys() if x.upper()[:6] == 'WEMPL_']
    confs = []
    first = True
    for key in keys:
        prefix = "" if first else "        "
        confs.append(subs_filter(prefix, key, os.environ[key]))
        first = False
    text = read(workPath)
    write(workPath, text.replace("## SUBS ##", "\n".join(confs)))

path = Path('my-default.conf')
workPath = Path('work.conf')
copy(path, workPath)

insert_subs_filter(workPath)
print("------------------------------")
print(f"Result in {workPath.absolute()}")

