#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Build deterministic skills from canonical modules; --check detects any drift."""
from __future__ import annotations
import argparse
import io
import posixpath
import re
import zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
MODULES = {
    'financial-living-system': 'moon-financial-living-system',
    'social-support-navigation-system': 'moon-social-support-navigation',
    'probability-calibration-system': 'moon-probability-calibration',
    'moon-image-cortex': 'moon-image-cortex',
}

def portable_markdown(source: Path, module_dir: Path) -> bytes:
    """Keep module-internal links local; route cross-repository links to GitHub.

    Paths in the source are interpreted before packaging. Never turn a missing
    internal target into an apparently working URL.
    """
    text = source.read_text(encoding='utf-8')
    pattern = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)')
    def rewrite(match: re.Match[str]) -> str:
        label, target = match.groups()
        path, sep, fragment = target.partition('#')
        if not path or ':' in path or path.startswith('/') or ' ' in path:
            return match.group(0)
        resolved = (source.parent / path).resolve()
        if resolved.is_relative_to(module_dir.resolve()):
            return match.group(0)
        expected_skill_zips = {ROOT / 'downloads' / 'skills' / f'{slug}.zip' for slug in MODULES.values()}
        if not resolved.is_relative_to(ROOT.resolve()) or (not resolved.exists() and resolved not in expected_skill_zips):
            raise ValueError(f'{source}: missing or outside-repository link {target}')
        relative = resolved.relative_to(ROOT.resolve()).as_posix()
        kind = 'raw/refs/heads/main' if resolved.suffix == '.zip' else ('tree/main' if resolved.is_dir() else 'blob/main')
        url = f'https://github.com/luahelenammc/Moon-Cortex/{kind}/{relative}'
        return f'[{label}]({url}{sep}{fragment})'
    return pattern.sub(rewrite, text).encode('utf-8')

def check_local_links(files: dict[str, bytes]) -> None:
    for filename, data in files.items():
        if not filename.endswith('.md'):
            continue
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', data.decode('utf-8')):
            path = target.split('#', 1)[0].strip().split(' ', 1)[0]
            if not path or ':' in path or path.startswith('/'):
                continue
            dest = posixpath.normpath(posixpath.join(posixpath.dirname(filename), path))
            if dest not in files and not any(x.startswith(dest.rstrip('/') + '/') for x in files):
                raise ValueError(f'{filename}: broken local link {target}')

def payload(module: str, name: str) -> dict[str, bytes]:
    skill = ROOT / 'skills' / module / 'SKILL.md'
    raw = skill.read_bytes()
    if not re.search(r'^name: ' + re.escape(name) + r'$', raw.decode(), re.M):
        raise ValueError(f'{skill}: skill name mismatch')
    files = {f'{name}/SKILL.md': raw}
    module_dir = ROOT / 'modules' / module
    for p in sorted(module_dir.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
            files[f'{name}/references/{p.relative_to(module_dir).as_posix()}'] = portable_markdown(p, module_dir) if p.suffix == '.md' else p.read_bytes()
    for p in ['NOTICE', 'LICENSING.md', 'LICENSES/CC-BY-4.0.txt', 'LICENSES/Apache-2.0.txt']:
        files[f'{name}/{p}'] = (ROOT / p).read_bytes()
    check_local_links(files)
    return files

def build(module: str, name: str) -> bytes:
    out = io.BytesIO()
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, data in sorted(payload(module, name).items()):
            info = zipfile.ZipInfo(path, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return out.getvalue()

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for module, name in MODULES.items():
        path = ROOT / 'downloads' / 'skills' / f'{name}.zip'
        expected = build(module, name)
        if args.check:
            if not path.exists() or path.read_bytes() != expected:
                raise SystemExit(f'stale or missing {path.relative_to(ROOT)}; run python scripts/build_skill_packages.py')
            with zipfile.ZipFile(path) as archive:
                assert archive.testzip() is None
                assert f'{name}/SKILL.md' in archive.namelist()
            print(f'OK {path.relative_to(ROOT)}')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(expected)
            print(f'built {path.relative_to(ROOT)} ({len(expected)} bytes)')
if __name__ == '__main__':
    main()
