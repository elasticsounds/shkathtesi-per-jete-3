"""Build the SCORM 1.2 package from the file list in imsmanifest.xml. Run from the bundle root, after build.py.

    python3 _adaptation_tools/make_scorm.py [output.zip]
"""
import os, sys, zipfile
import xml.dom.minidom as minidom

out = sys.argv[1] if len(sys.argv) > 1 else 'Shkathtesi-per-jete-3-SCORM-1.2.zip'
files = [f.getAttribute('href') for f in minidom.parse('imsmanifest.xml').getElementsByTagName('file')]
missing = [f for f in files if not os.path.exists(f)]
if missing:
    sys.exit(f'{len(missing)} files listed in imsmanifest.xml are missing, e.g. {missing[:3]}. Run build.py first.')
ALREADY_COMPRESSED = {'.mp3', '.mp4', '.png', '.jpg', '.jpeg', '.webp', '.woff', '.woff2'}
if os.path.exists(out):
    os.remove(out)
with zipfile.ZipFile(out, 'w') as z:
    z.write('imsmanifest.xml', compress_type=zipfile.ZIP_DEFLATED)   # must sit at the root of the package
    for f in files:
        stored = os.path.splitext(f)[1].lower() in ALREADY_COMPRESSED
        z.write(f, compress_type=zipfile.ZIP_STORED if stored else zipfile.ZIP_DEFLATED)
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    print(f'{out}: {len(z.namelist())} files, {os.path.getsize(out) / 1e6:.1f} MB')
