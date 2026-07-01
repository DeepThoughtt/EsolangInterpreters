# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

project_root = os.path.abspath(".")

import sys
sys.path.insert(0, project_root)

datas = []
datas += collect_data_files(os.path.join(project_root, "assets"))

a = Analysis(
    [os.path.join(project_root, 'src/ticker.py')],
    pathex=[project_root],
    binaries=[],
    datas=datas,
    hiddenimports=collect_submodules(os.path.join(project_root, 'src')),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ticker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    icon=os.path.join(project_root, 'assets', 'icons', 'esolangs.ico'),
)
