"""Pages 47-68: Tematika 5, Tematika 6 and back matter."""
from lib import *
from pages_a import n
from pages_c import (TH5, TH6, L51, opener, think, infopage, written, choice, numbered, note2)

# ====================== 47: kinds of pollution ======================
infopage('pg047_sec001', 47, TH5, L51, 'Njohim llojet e ndotjes', paras([n(47, 4, 5, 6, 7), n(47, 9, 10, 11, 12, 13)]))

new('pg047_ac001', 'Për secilën figurë, zgjidh të gjitha llojet e ndotjes që shkakton.')
new('pg047_ac002', 'Shembull: Figura 1 shkakton ndotje të ajrit dhe zhurmë.')
TYPES = [('toka', 'pg047_n0038'), ('ajri', 'pg047_n0042'), ('uji', 'pg047_n0047'), ('zhurma', 'pg047_n0051')]
F47 = [(2, 'pg047_im003', 'pg047_n0025', {'ajri', 'uji'}), (3, 'pg047_im004', 'pg047_n0027', {'ajri', 'zhurma'}), (4, 'pg047_im005', 'pg047_n0029', {'toka', 'ajri'})]
key, groups = {}, ''
for num, im, cap, ok in F47:
    boxes = ''
    for t, tid in TYPES:
        item = f'f{num}-{t}'
        key[item] = t in ok
        boxes += f'<label class="activity-option bk-option"><input type="checkbox" name="fig{num}" data-activity-item="{item}">{s(tid)}</label>'
    groups += (f'<fieldset class="bk-pick bk-pick--wide"><legend><span class="bk-pick-img">{deco(f"images/{im}.png")}</span>{s(cap)}</legend>'
               f'<div class="bk-options">{boxes}</div></fieldset>\n')
page('pg047_sec002', 'activity_multi_select', 'Njohim llojet e ndotjes: puno në klasë', f'''
{crumb(TH5, L51)}
{rubric('class', 'pg047_n0015')}
{task('pg047_n0017', '<p class="bk-soft">' + s('pg047_n0018') + '</p>', p('pg047_ac001'))}
<figure class="bk-figure">{deco('images/pg047_im002.png')}<figcaption>{s('pg047_n0023')}<br>{s('pg047_ac002')}</figcaption></figure>
{how('adt_how_select')}
<div class="bk-picks bk-picks--list">
{groups}</div>''', 47, attrs=f" data-correct-answers='{json.dumps(key)}'", scripts=answers_script(key))

# ====================== 48: self test ======================
new('pg048_ac001', 'Për secilën pyetje, zgjidh përgjigjen që vlen për ty. Këtu nuk ka përgjigje të gabuara. Kur t’u përgjigjesh të gjitha pyetjeve, do të shohësh rezultatin tënd.')
new('pg048_ac002', 'Pikët e tua:')
new('pg048_ac003', 'Rezultati yt')
Q48 = [(12, (14, 16, 18), 'pg048_im002', None), (19, (21, 23, 25), 'pg048_im010', None), (26, (28, 30, 32), 'pg048_im005', None),
       (33, (35, 37, 39), 'pg048_im007', None), (40, (42, 44, 46), 'pg048_im006', None), (47, (50, 52, 54), 'pg048_im011', 48),
       (55, (57, 59, 61), 'pg048_im003', None), (62, (64, 66, 68), 'pg048_im008', None), (69, (71, 73, 75), 'pg048_im009', None),
       (76, (78, 80, 82), 'pg048_im004', None)]
picks = ''
for j, (q, opts, im, extra) in enumerate(Q48, 1):
    legend = f'<span class="bk-pick-img">{deco(f"images/{im}.png")}</span>{s(f"pg048_n{q:04d}")}' + (f' {s(f"pg048_n{extra:04d}")}' if extra else '')
    picks += choice(f'k{j}', legend, [(v, f'pg048_n{o:04d}') for v, o in zip(('2', '1', '0'), opts)], wide=True)
SCORE_JS = '''<script>
(function () {
  var box = document.getElementById('score-box');
  if (!box) return;
  var groups = Array.from(document.querySelectorAll('fieldset.bk-pick'));
  function update() {
    var total = 0, answered = 0;
    groups.forEach(function (g) {
      var c = g.querySelector('input[type=radio]:checked');
      if (c) { answered++; total += Number(c.value); }
    });
    if (answered < groups.length) { box.hidden = true; return; }
    document.getElementById('score-num').textContent = total + ' / 20';
    var band = total >= 13 ? 'hi' : (total >= 7 ? 'mid' : 'lo');
    box.querySelectorAll('[data-band]').forEach(function (el) { el.hidden = el.getAttribute('data-band') !== band; });
    box.hidden = false;
  }
  document.addEventListener('change', function (e) { if (e.target && e.target.matches('fieldset.bk-pick input[type=radio]')) update(); });
})();
</script>'''
page('pg048_sec001', 'activity_true_false', 'Njohim llojet e ndotjes: testo veten', f'''
{crumb(TH5, L51)}
{rubric('home', 'pg048_n0004')}
{task('pg048_n0006', p('pg048_n0007', 'pg048_n0008'))}
<h2>{s('pg048_n0010')}</h2>
{p('pg048_n0011')}
{p('pg048_ac001')}
<div class="bk-picks bk-picks--list">
{picks}</div>
<div class="bk-info" id="score-box" role="status" aria-live="polite" hidden>
<h2>{s('pg048_ac003')}</h2>
<p class="bk-task-body">{s('pg048_ac002')} <span id="score-num"></span></p>
<div data-band="hi" hidden><h3>{s('pg048_n0084')}</h3>{p('pg048_n0086', 'pg048_n0087')}</div>
<div data-band="mid" hidden><h3>{s('pg048_n0089')}</h3>{p('pg048_n0091')}</div>
<div data-band="lo" hidden><h3>{s('pg048_n0093')}</h3>{p('pg048_n0095', 'pg048_n0096')}</div>
</div>''', 48, scripts=answers_script({}) + SCORE_JS)

# ====================== 49-51: lesson 2 ======================
L52 = 'pg005_n0026'
STORY49 = [n(49, 21, 22, 23, 24, 25), n(49, 27, 28), n(49, 30, 31, 32), n(49, 34)]
opener('pg049_sec001', 49, TH5, 'pg049_n0005', 'pg049_n0006', '2. Zhurmë dhe pluhur në punëtorinë e xhaxhi Burimit', 'pg049_im001',
       note('pg049_n0008', n(49, 11, 13, 15, 17), 'pg049_n0018', 'pg049_n0019'), STORY49)
think('pg049_sec002', 49, TH5, L52, 'Zhurmë dhe pluhur në punëtori', STORY49, n(49, 37, 39))
infopage('pg050_sec001', 50, TH5, L52, 'Zhurmë dhe pluhur në punëtori', paras([n(50, 4, 5, 6, 7, 8, 9), n(50, 11, 12)]))

items = ''
for j, (im, cap) in enumerate([('pg050_im002', 23), ('pg050_im004', 26), ('pg050_im003', 29), ('pg050_im005', 32)], 1):
    fid = f'c{j}'
    items += (f'<li>{img(im)}<p class="bk-task-body">{s(f"pg050_n{cap:04d}")}</p>'
              f'<label for="{fid}">{s("pg050_n0020")}</label><textarea id="{fid}" data-aria-id="{fid}" rows="3"></textarea></li>\n')
written('pg050_sec002', 50, TH5, L52, 'Zhurmë dhe pluhur në punëtori: puno në klasë', 'class', 'pg050_n0015', f'''
{task('pg050_n0017', p('pg050_n0018', 'pg050_n0019'))}
{how('adt_how_write')}
<ol class="bk-named bk-named--2">
{items}</ol>''')

new('pg051_ac001', 'Zgjidh të gjitha objektet që e shqetësojnë Tokën me zhurmën e tyre.')
N51 = [('Helikopteri', 1), ('Libri', 0), ('Kositësja e barit', 1), ('Autoambulanca me sirenë', 1), ('Lulja', 0), ('Vetura', 1),
       ('Radioja me zë të lartë', 1), ('Altoparlanti', 1), ('Flutura', 0), ('Sharra elektrike', 1), ('Aeroplani', 1), ('Lapsi', 0)]
key, opts = {}, ''
for j, (label, ok) in enumerate(N51, 1):
    i = new(f'pg051_ac{j + 1:03d}', label)
    key[f'z{j}'] = bool(ok)
    opts += f'<label class="activity-option bk-option"><input type="checkbox" name="noise" data-activity-item="z{j}">{s(i)}</label>\n'
page('pg051_sec001', 'activity_multi_select', 'Zhurmë dhe pluhur në punëtori: çfarë e shqetëson Tokën', f'''
{crumb(TH5, L52)}
{rubric('class', 'pg051_n0005')}
{task('pg051_n0007', '<p class="bk-soft">' + s('pg051_n0008') + ' ' + s('pg051_n0009') + '</p>', p('pg051_ac001'))}
{figure('pg051_im001')}
{how('adt_how_select')}
<div class="bk-options">
{opts}</div>''', 51, attrs=f" data-correct-answers='{json.dumps(key)}'", scripts=answers_script(key))

new('pg051_ac020', 'Për secilin send, zgjidh PO nëse shkakton zhurmë ose JO nëse nuk shkakton.')
S51 = [('pg051_im013', 18, 'po'), ('pg051_im014', 21, 'po'), ('pg051_im008', 24, 'jo'), ('pg051_im009', 27, 'po'), ('pg051_im003', 30, 'po'),
       ('pg051_im010', 33, 'jo'), ('pg051_im011', 36, 'jo'), ('pg051_im004', 39, 'po'), ('pg051_im012', 42, 'jo'), ('pg051_im005', 45, 'po'),
       ('pg051_im006', 48, 'po'), ('pg051_im007', 51, 'po')]
key, picks = {}, ''
for j, (im, k, ok) in enumerate(S51, 1):
    key[f'y{j}'] = ok
    legend = f'<span class="bk-pick-img">{deco(f"images/{im}.png")}</span>{s(im)}'
    picks += choice(f'y{j}', legend, [('po', f'pg051_n{k:04d}'), ('jo', f'pg051_n{k + 1:04d}')])
page('pg051_sec002', 'activity_true_false', 'Zhurmë dhe pluhur në punëtori: puno në shtëpi', f'''
{crumb(TH5, L52)}
{rubric('home', 'pg051_n0012')}
{task('pg051_n0014', p('pg051_n0015'), p('pg051_ac020'))}
{how('adt_how_choose')}
<div class="bk-picks">
{picks}</div>''', 51, scripts=answers_script(key))

# ====================== 52-53: lesson 3 ======================
L53 = 'pg005_n0029'
EDIT['pg052_n0024'] = T['pg052_n0024'].lstrip('• ').strip()
STORY52 = [n(52, 18), n(52, 19, 20, 21, 22, 23)]
opener('pg052_sec001', 52, TH5, 'pg052_n0004', 'pg052_n0005', '3. Gëzuar ditën tënde, Tokë!', 'pg052_im001',
       note('pg052_n0007', n(52, 10, 12, 14), 'pg052_n0015', 'pg052_n0016'), STORY52)
think('pg052_sec002', 52, TH5, L53, 'Gëzuar ditën tënde, Tokë!', STORY52, ['pg052_n0024'])
infopage('pg053_sec001', 53, TH5, L53, 'Gëzuar ditën tënde, Tokë!',
         paras([n(52, 27, 28, 29), n(52, 31), n(52, 32) + n(53, 4), n(53, 5, 6)]))

new('pg053_ac001', 'Plotëso fjalitë me fjalët që mungojnë. Zgjidh një fjalë nga lista, pastaj zgjidh vendin bosh ku duhet të shkojë. Mund ta shkruash fjalën edhe vetë.')
new('pg053_ac002', 'Fjalët')
SENT = [  # sentence pieces: text or (item, accepted answers, hint image, hint alt id)
    ['Në vend të', (1, 'makinës|makines|veturës|vetures', 'pg053_im002'), 'së prindërve, ne zgjedhim të ecim më këmbë së bashku apo të përdorim',
     (2, 'biçikletën|bicikleten|biçikleten|biciklete', 'pg053_im003'), 'sa herë që mundemi.'],
    ['Unë e kursej', (3, 'ujin|ujë|uje', 'pg053_im004'), 'kur laj dhëmbët, duke e mbyllur rubinetin.'],
    ['Ne mbjellim sa më shumë', (4, 'pemë|peme', 'pg053_im005'), '.'],
    ['Unë përdor qese', (5, 'letre|prej letre', 'pg053_im006'), 'në vend të qeseve', (6, 'plastike|prej plastike', 'pg053_im007'), '.'],
    ['Unë e fik', (7, 'dritën|driten|llambën|llamben', None), 'kur dal nga dhoma.'],
    ['Unë dhe familja ime i hedhim mbeturinat nëpër', (8, 'koshat|kosha', 'pg053_im009'),
     'e caktuar, në vend që t’i hedhim ato të gjitha në një vend apo t’i djegim.']]
BANK = ['dritën', 'pemë', 'makinës', 'plastike', 'ujin', 'koshat', 'biçikletën', 'letre']
key, lis, seg = {}, '', 0
for si, pieces in enumerate(SENT, 1):
    out = ''
    for pc in pieces:
        if isinstance(pc, str):
            seg += 1
            out += s(new(f'pg053_ac{seg + 10:03d}', pc)) + ' '
        else:
            item, ans, im = pc
            key[f'item-{item}'] = ans
            hint = img(im, cls='bk-hintimg') if im else ''
            out += (f'<input type="text" class="bk-blank" id="b{item}" data-aria-id="b{item}" data-activity-item="item-{item}" data-word-bank-target '
                    f'aria-label="Fjala që mungon {item}" autocomplete="off" autocapitalize="none" spellcheck="false">{hint} ')
    lis += f'<li>{out}</li>\n'
chips = ''.join(f'<button type="button" class="bk-wchip" data-word-bank-chip="{w}" aria-pressed="false">{s(new(f"pg053_ac{k + 40:03d}", w))}</button>' for k, w in enumerate(BANK))
BANK_JS = '''<script>
(function () {
  // Tap-to-place for the word bank (the reader itself only places a chosen word on Enter or drag).
  document.querySelectorAll('input[data-word-bank-target]').forEach(function (inp) {
    inp.addEventListener('click', function () {
      var chip = document.querySelector('[data-word-bank-chip][aria-pressed="true"]');
      if (!chip || inp.value) return;
      inp.value = chip.getAttribute('data-word-bank-chip');
      inp.dispatchEvent(new Event('input', { bubbles: true }));
      chip.setAttribute('aria-pressed', 'false');
    });
  });
})();
</script>'''
written('pg053_sec002', 53, TH5, L53, 'Gëzuar ditën tënde, Tokë!: puno në klasë', 'class', 'pg053_n0008', f'''
{task('pg053_n0009', p('pg053_n0010'), p('pg053_ac001'))}
<div class="bk-group" role="group" aria-labelledby="bank-h"><h2 id="bank-h">{s('pg053_ac002')}</h2>
<div class="bk-wbank">{chips}</div><p class="bk-sr" data-word-bank-status role="status" aria-live="polite"></p></div>
<ol class="bk-steps bk-sentences">
{lis}</ol>''', family='activity_fill_in_the_blank', scripts=answers_script(key) + BANK_JS)

new('pg053_ac060', 'Gjëja që do të bëj')
written('pg053_sec003', 53, TH5, L53, 'Gëzuar ditën tënde, Tokë!: pesë gjëra për Tokën', 'class', 'pg053_n0008', f'''
{task('pg053_n0031', p('pg053_n0032'))}
{how('adt_how_write')}
{numbered(5, 'pg053_ac060')}''')

# ====================== 54-56: lesson 4 ======================
L54 = 'pg005_n0032'
STORY54 = [n(54, 19, 20), n(54, 21, 22)]
opener('pg054_sec001', 54, TH5, 'pg054_n0004', 'pg054_n0005', '4. Piknik në natyrë', 'pg054_im001',
       note('pg054_n0007', n(54, 10, 12, 14), 'pg054_n0015', 'pg054_n0017'), STORY54)
think('pg054_sec002', 54, TH5, L54, 'Piknik në natyrë', STORY54, n(54, 25, 27))
infopage('pg055_sec001', 55, TH5, L54, 'Piknik në natyrë',
         paras([n(54, 30, 31, 32), n(54, 33, 34, 35, 36, 37), n(54, 38) + n(54, 39) + n(55, 5), n(55, 6, 7, 8)]),
         p('pg055_n0009'), '<ol class="bk-steps">' + ''.join(f'<li>{s(x)}</li>' for x in n(55, 12, 14, 16, 18)) + '</ol>', figure('pg055_im004'))
written('pg055_sec002', 55, TH5, L54, 'Piknik në natyrë: puno në klasë', 'class', 'pg055_n0021', f'''
{task('pg055_n0023', p('pg055_n0024'))}
{figure('pg055_im003')}
{figure('pg055_im002')}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg055_n0025'])}
{question(['pg055_n0026'])}
</div>''')

STANZAS = [n(56, 13, 14, 15, 16), n(56, 17, 18, 19, 20), n(56, 21, 22, 23, 24, 25), n(56, 26, 27, 28, 29), n(56, 30, 31, 32)]
poem = ''.join('<p class="bk-stanza">' + '<br>'.join(s(x) for x in st) + '</p>' for st in STANZAS)
written('pg056_sec001', 56, TH5, L54, 'Piknik në natyrë: puno në shtëpi', 'home', 'pg056_n0003', f'''
{task('pg056_n0005', p('pg056_n0006', 'pg056_n0007'))}
<section class="bk-group bk-poem" aria-labelledby="poem-h"><h2 id="poem-h" data-id="pg056_n0011">{esc(tx('pg056_n0011'))}</h2>
{poem}
{figure('pg056_im004')}</section>
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg056_n0008'])}
{question(['pg056_n0009'], rows=6)}
</div>''')

# ====================== 57-58: Tematika 6, lesson 1 ======================
L61 = 'pg005_n0038'
STORY57 = [n(57, 19, 20), n(57, 22), n(57, 24)]
opener('pg057_sec001', 57, TH6, 'pg057_n0005', 'pg057_n0006', '1. Dita përdor kompjuterin', 'pg057_im001',
       note('pg057_n0008', n(57, 11, 13, 15), 'pg057_n0016', 'pg057_n0017'), STORY57)
think('pg057_sec002', 57, TH6, L61, 'Dita përdor kompjuterin', STORY57, n(57, 27, 29))
infopage('pg058_sec001', 58, TH6, L61, 'Dita përdor kompjuterin',
         paras([n(57, 32, 33), n(57, 35, 36), n(58, 5, 6), n(58, 7, 8, 9)]),
         f'<div class="bk-note"><h2 data-id="pg058_n0011">{esc(tx("pg058_n0011"))}</h2>{p("pg058_n0013", "pg058_n0014")}</div>')
new('pg058_ac001', 'Arsyeja')
written('pg058_sec002', 58, TH6, L61, 'Dita përdor kompjuterin: puno në klasë', 'class', 'pg058_n0017', f'''
{how('adt_how_write')}
<div class="bk-task"><span class="bk-task-num" data-id="pg058_n0019">{esc(tx('pg058_n0019'))}</span><div class="bk-panel">
{question(['pg058_n0020'], kind='input')}
{question(['pg058_n0021'])}
</div></div>
{task('pg058_n0023', p('pg058_n0024'), '<p class="bk-soft">' + s('pg058_n0025') + '</p>')}
{numbered(4, 'pg058_ac001')}''')
new('pg058_ac002', 'Tri gjëra të dobishme që ka interneti për fëmijët')
new('pg058_ac003', 'Tri gjëra të dëmshme që ka interneti për fëmijët')
written('pg058_sec003', 58, TH6, L61, 'Dita përdor kompjuterin: puno në shtëpi', 'home', 'pg058_n0027', f'''
{task('pg058_n0029', p('pg058_n0030'))}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg058_ac002'], rows=4)}
{question(['pg058_ac003'], rows=4)}
</div>''')

# ====================== 59-61: lesson 2 ======================
L62 = 'pg005_n0041'
STORY59 = [n(59, 18), n(59, 19), n(59, 20), n(59, 21, 22, 23)]
opener('pg059_sec001', 59, TH6, 'pg059_n0004', 'pg059_n0005', '2. Dita dhe Dielli prezantojnë projektin', 'pg059_im001',
       note('pg059_n0007', n(59, 10, 12, 14), 'pg059_n0015', 'pg059_n0016'), STORY59)
think('pg059_sec002', 59, TH6, L62, 'Dita dhe Dielli prezantojnë projektin', STORY59, n(59, 26, 28))
infopage('pg060_sec001', 60, TH6, L62, 'Dita dhe Dielli prezantojnë projektin',
         paras([n(60, 5, 6, 7, 8, 9, 10), n(60, 11, 12, 13, 14, 15), n(60, 17, 18)]), figure('pg060_im001'))

new('pg061_ac001', 'Emri')
new('pg061_ac002', 'Mbiemri')
new('pg061_ac003', 'Datëlindja')
new('pg061_ac004', 'Shkolla')
new('pg061_ac005', 'Klasa')
new('pg061_ac006', 'Të dhënat që shkruan këtu ruhen vetëm në këtë pajisje.')
written('pg061_sec001', 61, TH6, L62, 'Dita dhe Dielli prezantojnë projektin: puno në klasë', 'class', 'pg061_n0005', f'''
{task('pg061_n0007', p('pg061_n0008'), '<p class="bk-soft">' + s('pg061_n0009') + ' ' + s('pg061_n0010') + '</p>')}
{figure('pg061_im001')}
{how('pg061_ac006')}
<div class="bk-panel">
{''.join(question([f'pg061_ac{k:03d}'], kind='input') for k in range(1, 6))}
</div>''')
page('pg061_sec002', 'text_and_images', 'Dita dhe Dielli prezantojnë projektin: puno në shtëpi', f'''
{crumb(TH6, L62)}
{rubric('home', 'pg061_n0013')}
{task('pg061_n0015', p('pg061_n0016'), '<p class="bk-soft">' + s('pg061_n0017') + ' ' + s('pg061_n0018') + '</p>')}
{how('adt_help_act')}
<div class="bk-fields bk-fields--2">{figure('pg061_im003')}{figure('pg061_im004')}</div>''', 61, role='article')

# ====================== 62-63: lesson 3 ======================
L63 = 'pg005_n0044'
STORY62 = [n(62, 7, 8), n(62, 10, 11)]
opener('pg062_sec001', 62, TH6, 'pg062_n0004', 'pg062_n0005', '3. Festa jonë', 'pg062_im001',
       note('pg062_n0019', n(62, 22, 24), 'pg062_n0025', 'pg062_n0026'), STORY62)
think('pg062_sec002', 62, TH6, L63, 'Festa jonë', STORY62, n(62, 14, 16))
page('pg062_sec003', 'boxed_text', 'Festa jonë: pak historik për 1 Qershorin', f'''
{crumb(TH6, L63)}
{rubric('learn', 'pg062_n0028')}
{info(paras([n(62, 30, 31), n(62, 32) + n(63, 4), n(63, 5, 6, 7, 8), n(63, 9), n(63, 11)]))}''', 62, role='article')
new('pg063_ac001', 'Loja')
written('pg063_sec002', 63, TH6, L63, 'Festa jonë: puno në klasë', 'class', 'pg063_n0013', f'''
{task('pg063_n0015', p('pg063_n0016'))}
<figure class="bk-figure">{deco('images/pg063_im001.png')}</figure>
{how('adt_how_write')}
{numbered(3, 'pg063_ac001')}''')
new('pg063_ac002', 'Nëse nuk mund të vizatosh, përshkruaje vizatimin tënd me fjalë ose tregoja dikujt që vizaton për ty.')
new('pg063_ac003', 'Përshkruaj vizatimin ose mesazhin tënd.')
written('pg063_sec003', 63, TH6, L63, 'Festa jonë: puno në shtëpi', 'home', 'pg063_n0021', f'''
{task('pg063_n0023', p('pg063_n0024'), '<p class="bk-soft">' + s('pg063_n0025') + '</p>')}
{how('pg063_ac002')}
<div class="bk-panel">
{question(['pg063_ac003'], rows=5)}
</div>''')

# ====================== 64-65: lesson 4 (practical) ======================
L64 = 'pg005_n0047'
opener('pg064_sec001', 64, TH6, 'pg064_n0004', 'pg064_n0005', '4. Fletushka jonë', 'pg064_im001',
       note('pg064_n0008', n(64, 11, 13, 15), 'pg064_n0016', 'pg064_n0017'), [n(64, 19, 20)], sub='pg064_n0006')
page('pg064_sec002', 'text_only', 'Fletushka jonë: hapat e punës', f'''
{crumb(TH6, L64)}
{rubric('class', 'pg064_n0005')}
<ol class="bk-steps">
<li>{s('pg064_n0022')} {s('pg064_n0023')}</li>
<li>{s('pg064_n0024')}</li>
<li>{s('pg064_n0025')}</li>
<li>{s('pg064_n0026')}</li>
<li>{s('pg064_n0027')} {s('pg065_n0004')}</li>
</ol>
{how('adt_help_act')}''', 64, role='article')
page('pg065_sec001', 'text_and_images', 'Fletushka jonë: lexo dhe mëso', f'''
{crumb(TH6, L64)}
{rubric('learn', 'adt_learn')}
{info(paras([n(65, 6), n(65, 8, 9), n(65, 11, 12), n(65, 14)]), '<p class="bk-task-body">' + s('pg065_n0016') + '</p>')}
{p('pg065_n0018')}
<div class="bk-fields bk-fields--2">{figure('pg065_im001')}{figure('pg065_im002')}</div>
<p class="bk-task-body">{s('pg065_n0019')}</p>''', 65, role='article')

# ====================== 66, 68: back matter ======================
page('pg066_sec001', 'text_only', 'Bibliografi', f'''
<h1>{s('pg066_n0002')}</h1>
<ul class="bk-plainlist">{''.join(f'<li>{s(x)}</li>' for x in n(66, 5, 7, 9, 11))}</ul>''', 66, role='article')
page('pg068_sec001', 'inside_cover', 'Katalogimi në botim', f'''
<h1>{s('pg068_n0003')}</h1>
{p('pg068_n0004')}
{p('pg068_n0005')}
<p>{s('pg068_n0007')}<br>{s('pg068_n0008')}<br>{s('pg068_n0009')}</p>
{p('pg068_n0010')}
{p('pg068_n0011')}''', 68, role='article')
