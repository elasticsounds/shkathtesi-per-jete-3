"""Rebuild pages 1-24 and every index that depends on them. Run from the bundle root."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from lib import PAGES, NEW, EDIT, T, I18N, render
import pages_a, pages_b, pages_c, pages_d, pages_q  # noqa: registers pages

def dump(path, obj):
    json.dump(obj, open(path, 'w'), ensure_ascii=False, indent=2)

# ---- texts / speech ----
texts = json.load(open(I18N + 'texts.json'))
speech = json.load(open(I18N + 'speech_texts.json'))
for k, v in NEW.items():
    texts[k] = v
    speech[k] = v
for k, v in EDIT.items():
    texts[k] = v
    speech[k] = v
dump(I18N + 'texts.json', texts)
dump(I18N + 'speech_texts.json', speech)

# ---- reading order ----
old = json.load(open('content/pages.json'))
def num(sid):
    m = re.match(r'pg(\d+)_', sid)
    return int(m.group(1)) if m else None
order = ['pg001_sec001', 'pg002_sec001', 'pg003_sec001', 'pg004_sec001', 'pg005_sec001',
         'pg006_sec001', 'pg006_sec002', 'pg006_sec003', 'pg007_sec001', 'pg007_sec002', 'pg007_sec003', 'qz001',
         'pg008_sec001', 'pg008_sec002', 'pg009_sec001', 'pg010_sec001', 'pg011_sec001', 'pg011_sec002',
         'pg012_sec001', 'pg012_sec002', 'pg013_sec001', 'pg013_sec002', 'pg014_sec001', 'pg014_sec002',
         'pg015_sec001', 'pg015_sec002', 'pg016_sec001', 'pg017_sec001', 'pg017_sec002',
         'pg018_sec001', 'pg018_sec002', 'pg018_sec003', 'pg018_sec004', 'pg018_sec005',
         'pg019_sec001', 'pg019_sec002', 'pg020_sec001', 'pg020_sec002', 'pg021_sec001',
         'pg022_sec001', 'pg022_sec002', 'pg022_sec003', 'pg023_sec001', 'pg024_sec001', 'pg024_sec002']
order += ['pg025_sec001', 'pg026_sec001', 'pg026_sec002', 'pg026_sec003', 'pg027_sec001', 'pg028_sec001', 'pg028_sec002',
          'pg029_sec001', 'pg029_sec002', 'pg030_sec001', 'pg030_sec002', 'pg031_sec001', 'qz002',
          'pg032_sec001', 'pg032_sec002', 'pg033_sec001', 'pg033_sec002', 'pg033_sec003', 'pg034_sec001',
          'pg035_sec001', 'pg035_sec002', 'pg035_sec003', 'pg036_sec001', 'pg036_sec002', 'pg036_sec003', 'pg037_sec001',
          'pg038_sec001', 'pg038_sec002', 'pg039_sec001', 'pg039_sec002', 'pg039_sec003',
          'pg040_sec001', 'pg040_sec002', 'pg041_sec001', 'pg041_sec002', 'qz003',
          'pg042_sec001', 'pg042_sec002', 'pg043_sec001', 'pg043_sec002', 'pg043_sec003',
          'pg044_sec001', 'pg044_sec002', 'pg045_sec001', 'pg045_sec002', 'pg045_sec003',
          'pg046_sec001', 'pg046_sec002', 'pg047_sec001', 'pg047_sec002', 'pg048_sec001',
          'pg049_sec001', 'pg049_sec002', 'pg050_sec001', 'pg050_sec002', 'pg051_sec001', 'pg051_sec002',
          'pg052_sec001', 'pg052_sec002', 'pg053_sec001', 'pg053_sec002', 'pg053_sec003', 'qz004',
          'pg054_sec001', 'pg054_sec002', 'pg055_sec001', 'pg055_sec002', 'pg056_sec001',
          'pg057_sec001', 'pg057_sec002', 'pg058_sec001', 'pg058_sec002', 'pg058_sec003',
          'pg059_sec001', 'pg059_sec002', 'pg060_sec001', 'pg061_sec001', 'pg061_sec002',
          'pg062_sec001', 'pg062_sec002', 'pg062_sec003', 'pg063_sec002', 'pg063_sec003',
          'pg064_sec001', 'pg064_sec002', 'pg065_sec001', 'pg066_sec001', 'pg068_sec001']
rest = []
assert set(order) == set(PAGES), set(order) ^ set(PAGES)
assert len(order) == len(set(order))
pages = []
for sid in order:
    e = {'section_id': sid, 'href': sid + '.html'}
    if sid in PAGES and PAGES[sid]['page'] and not sid.startswith('qz'):
        e['page_number'] = PAGES[sid]['page']
    pages.append(e)
pages += rest
dump('content/pages.json', pages)

# ---- write pages + renumber every page's position meta ----
for pos, e in enumerate(pages, 1):
    sid = e['section_id']
    if sid in PAGES:
        open(e['href'], 'w').write(render(sid, pos))
    else:
        h = open(e['href']).read()
        h2, c = re.subn(r'(<meta name="page-section-id" content=")\d+(")', rf'\g<1>{pos}\g<2>', h)
        assert c == 1, e['href']
        if h2 != h: open(e['href'], 'w').write(h2)

# ---- table of contents ----
def t(sid, cid, level):
    return {'section_id': sid, 'href': sid + '.html', 'title': texts[cid], 'chapter_id': cid, 'level': level}
toc_new = [
    t('pg001_sec001', 'adt_cover', 1), t('pg003_sec001', 'pg003_n0002', 1), t('pg004_sec001', 'pg004_n0002', 1),
    t('pg006_sec001', 'pg006_n0002', 1),
    t('pg006_sec001', 'pg004_n0007', 2), t('pg007_sec002', 'pg007_n0017', 3), t('pg007_sec003', 'pg007_n0032', 3),
    t('pg008_sec001', 'pg004_n0010', 2), t('pg009_sec001', 'pg009_n0003', 3), t('pg010_sec001', 'pg010_n0005', 3),
    t('pg011_sec001', 'pg004_n0013', 2), t('pg012_sec002', 'pg012_n0011', 3), t('pg013_sec001', 'pg013_n0004', 3), t('pg013_sec002', 'pg013_n0014', 3),
    t('pg014_sec001', 'pg004_n0016', 2), t('pg015_sec001', 'pg015_n0003', 3), t('pg015_sec002', 'pg015_n0009', 3), t('pg016_sec001', 'pg016_n0004', 3),
    t('pg017_sec001', 'pg018_n0002', 1),
    t('pg017_sec001', 'pg004_n0022', 2), t('pg018_sec002', 'pg018_n0009', 3), t('pg018_sec005', 'pg018_n0017', 3),
    t('pg019_sec001', 'pg004_n0025', 2), t('pg020_sec002', 'pg020_n0014', 3), t('pg021_sec001', 'pg021_n0004', 3),
    t('pg022_sec001', 'pg004_n0028', 2), t('pg023_sec001', 'pg023_n0003', 3), t('pg024_sec001', 'pg024_n0004', 3), t('pg024_sec002', 'pg024_n0021', 3),
]
toc_new += [
    t('pg025_sec001', 'pg004_n0031', 2), t('pg026_sec001', 'pg026_n0004', 3), t('pg027_sec001', 'pg027_n0004', 3), t('pg028_sec001', 'pg028_n0004', 3),
    t('pg029_sec001', 'pg030_n0002', 1),
    t('pg029_sec001', 'pg004_n0037', 2), t('pg030_sec002', 'pg030_n0018', 3), t('pg031_sec001', 'pg031_n0003', 3),
    t('pg032_sec001', 'pg004_n0040', 2), t('pg033_sec002', 'pg033_n0018', 3), t('pg033_sec003', 'pg033_n0033', 3),
    t('pg034_sec001', 'pg004_n0043', 2),
    t('pg035_sec001', 'pg036_n0002', 1),
    t('pg035_sec001', 'pg005_n0005', 2), t('pg036_sec001', 'pg036_n0004', 3), t('pg036_sec002', 'pg036_n0022', 3), t('pg037_sec001', 'pg037_n0004', 3),
    t('pg038_sec001', 'pg005_n0008', 2), t('pg039_sec002', 'pg039_n0014', 3), t('pg039_sec003', 'pg039_n0022', 3),
    t('pg040_sec001', 'pg005_n0011', 2), t('pg041_sec002', 'pg041_n0011', 3),
    t('pg042_sec001', 'pg005_n0014', 2), t('pg043_sec002', 'pg043_n0011', 3), t('pg043_sec003', 'pg043_n0022', 3),
    t('pg044_sec001', 'pg005_n0017', 2), t('pg045_sec002', 'pg045_n0010', 3), t('pg045_sec003', 'pg045_n0021', 3),
    t('pg046_sec001', 'pg048_n0002', 1),
    t('pg046_sec001', 'pg005_n0023', 2), t('pg047_sec002', 'pg047_n0015', 3), t('pg048_sec001', 'pg048_n0004', 3),
    t('pg049_sec001', 'pg005_n0026', 2), t('pg050_sec002', 'pg050_n0015', 3), t('pg051_sec002', 'pg051_n0012', 3),
    t('pg052_sec001', 'pg005_n0029', 2), t('pg053_sec002', 'pg053_n0008', 3),
    t('pg054_sec001', 'pg005_n0032', 2), t('pg055_sec002', 'pg055_n0021', 3), t('pg056_sec001', 'pg056_n0003', 3),
    t('pg057_sec001', 'pg058_n0002', 1),
    t('pg057_sec001', 'pg005_n0038', 2), t('pg058_sec002', 'pg058_n0017', 3), t('pg058_sec003', 'pg058_n0027', 3),
    t('pg059_sec001', 'pg005_n0041', 2), t('pg061_sec001', 'pg061_n0005', 3), t('pg061_sec002', 'pg061_n0013', 3),
    t('pg062_sec001', 'pg005_n0044', 2), t('pg063_sec002', 'pg063_n0013', 3), t('pg063_sec003', 'pg063_n0021', 3),
    t('pg064_sec001', 'pg005_n0047', 2),
    t('pg066_sec001', 'pg066_n0002', 1),
]
toc = toc_new
dump('content/toc.json', toc)

# ---- sign language: one clip per page, reusing the clips in content/i18n/sq/video/ in rotation ----
VID = I18N + 'video/'
clips = sorted(f for f in os.listdir(VID) if f.endswith('.mp4')) if os.path.isdir(VID) else []
if clips:
    dump(I18N + 'videos.json', {e['section_id']: clips[k % len(clips)] for k, e in enumerate(pages)})
    cfg = json.load(open('assets/config.json'))
    cfg['features']['signLanguage'] = True
    dump('assets/config.json', cfg)

# ---- interface translations (screen-reader announcements) ----
ITP = 'assets/interface_translations/sq/interface_translations.json'
it = json.load(open(ITP))
it.update(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sq_ui.json'))))
dump(ITP, it)

# ---- SCORM manifest: list new files ----
man = open('imsmanifest.xml').read()
want = [e['href'] for e in pages] + ['content/book.css'] + sorted('images/' + f for f in os.listdir('images')) + [VID + f for f in clips]
add = [f for f in want if f'href="{f}"' not in man]
if add:
    man = man.replace('</resource>', ''.join(f'<file href="{f}"/>' for f in add) + '</resource>', 1)
    open('imsmanifest.xml', 'w').write(man)

# ---- offline preloader: re-embed JSON and pages ----
PL = 'assets/offline-preloader.js'
src = open(PL).read()
i = src.index('var INLINE = ') + len('var INLINE = ')
inline, end = json.JSONDecoder().raw_decode(src, i)
out = {}
for k in inline:
    path = k[2:]
    if k.endswith('.json'):
        out[k] = json.load(open(path))
    elif k.endswith('.html') and re.match(r'\./(pg|qz)', k):
        continue  # re-added below in reading order
    else:
        out[k] = open(path).read() if os.path.exists(path) else inline[k]
for e in pages:
    out['./' + e['href']] = open(e['href']).read()
open(PL, 'w').write(src[:i] + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + src[end:])

print('pages', len(pages), 'rebuilt', len(PAGES), 'new texts', len(NEW), 'edited texts', len(EDIT), 'manifest +', len(add))
json.dump({'new': NEW, 'edit': EDIT}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'text_changes.json'), 'w'), ensure_ascii=False, indent=1)
