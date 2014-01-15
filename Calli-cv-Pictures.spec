# -*- mode: python -*-
a = Analysis(['Calli-cv-Pictures.py'],
             pathex=['C:\\Users\\Manuel\\Documents\\GitHub\\Calli-cv'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Calli-cv-Pictures.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
