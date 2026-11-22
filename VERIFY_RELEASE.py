from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile
BASE=Path(__file__).resolve().parent
lines=(BASE/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines()
expected={}
for line in lines:
    h,rel=line.split('  ',1)
    assert rel not in expected and not rel.startswith('/') and '..' not in Path(rel).parts
    expected[rel]=h
actual={p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()}-{'SHA256SUMS.txt','VERIFY_RELEASE.py'}
assert actual==set(expected), f'file set mismatch: extra={actual-set(expected)}, missing={set(expected)-actual}'
for rel,h in expected.items():
    assert sha256((BASE/rel).read_bytes()).hexdigest()==h, rel
    if rel.endswith('.zip'):
        with ZipFile(BASE/rel) as z:
            assert z.testzip() is None, rel+' bad CRC'
print(f'PASS: release manifest {len(expected)}/{len(expected)} and ZIP CRC')
