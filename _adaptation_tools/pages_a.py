"""Pages 1-12: front matter and Tematika 1, lessons 1-3."""
from lib import *

# ---------- Shared strings ----------
new('adt_think', 'Mendo dhe përgjigju')
new('adt_help', 'Ndihmë: si të punoj?')
new('adt_learn', 'Lexo dhe mëso')
new('adt_reread', 'Lexo përsëri tregimin')
new('adt_reset', 'Fshi përgjigjet e mia')
new('adt_how_write', 'Shkruaj përgjigjen tënde. Mund ta thuash edhe me zë ose t’ia tregosh dikujt që shkruan për ty. Kur të mbarosh, shtyp butonin “Dërgo”.')
new('adt_how_sort', 'Zgjidh një kartë, pastaj zgjidh kutinë ku duhet të shkojë. Për ta nxjerrë kartën nga kutia, zgjidhe përsëri. Kur të mbarosh, shtyp butonin “Dërgo”.')
new('adt_how_match', 'Zgjidh një kartë, pastaj zgjidh vendin ku duhet të shkojë. Për ta hequr kartën, zgjidhe përsëri. Kur të mbarosh, shtyp butonin “Dërgo”.')
new('adt_how_order', 'Lëvize secilën kartë me butonat “Lëviz lart” dhe “Lëviz poshtë”, derisa radha të jetë e saktë. Kur të mbarosh, shtyp butonin “Dërgo”.')
new('adt_how_select', 'Zgjidh të gjitha përgjigjet e sakta. Mund të zgjedhësh më shumë se një. Kur të mbarosh, shtyp butonin “Dërgo”.')
new('adt_cards', 'Kartat')
new('adt_help_craft', 'Kjo veprimtari bëhet me duar. Nëse e ke të vështirë të vizatosh ose të presësh, kërkoji një të rrituri të t’i përgatitë pjesët. Ti mund t’i prekësh, t’i palosësh dhe t’i ngjitësh.')
new('adt_imprint', 'Të dhëna për botimin')
new('adt_cover', 'Kopertina')

TH1 = 'pg006_n0002'   # TEMATIKA 1: MATERIALET DHE PËRPUNIMI I TYRE
L1 = ('pg004_n0007',)  # 1. Vallja e materialeve
L2 = ('pg004_n0010',)
L3 = ('pg004_n0013',)

# ---------- 1: cover ----------
page('pg001_sec001', 'front_cover', 'Kopertina', f'''
<div class="bk-cover">
<p class="bk-authors">{s('pg001_n0002')}<br>{s('pg001_n0003')}</p>
{img('pg001_im004_crop_v1')}
<h1>{s('pg001_n0006')} {s('pg001_n0005')}</h1>
{img('pg001_im001')}
{p('pg001_n0007')}
</div>''', role='article')

# ---------- 2: imprint ----------
def dl(pairs):
    out = []
    for k, vs in pairs:
        out.append(f'<dt>{s(k)}</dt>' + ''.join(f'<dd>{s(v)}</dd>' for v in vs))
    return '<dl class="bk-dl">' + ''.join(out) + '</dl>'

page('pg002_sec001', 'inside_cover', 'Të dhëna për botimin', f'''
<h1>{s('adt_imprint')}</h1>
{p('pg002_n0002')}
{dl([('pg002_n0004', ['pg002_n0005']), ('pg002_n0007', ['pg002_n0008']), ('pg002_n0010', ['pg002_n0011']),
     ('pg002_n0013', ['pg002_n0014', 'pg002_n0015', 'pg002_n0016']), ('pg002_n0018', ['pg002_n0019']),
     ('pg002_n0021', ['pg002_n0022']), ('pg002_n0024', ['pg002_n0025'])])}
<p>{s('pg002_n0027')}<br>{s('pg002_n0028')}<br>{s('pg002_n0029')}</p>
<h2>{s('pg002_n0031')}</h2>
<p>{s('pg002_n0032')}<br>{s('pg002_n0033')}<br>{s('pg002_n0034')}</p>
<p>{s('pg002_n0035')}<br>{s('pg002_n0036')}<br>{s('pg002_n0037')}</p>
<p>{s('pg002_n0038')}<br>{s('pg002_n0039')}<br>{s('pg002_n0040')}</p>
<p>{s('pg002_n0041')}<br>{s('pg002_n0042')}<br>{s('pg002_n0043')}</p>
{p('pg002_n0045', 'pg002_n0046')}''', role='article')

# ---------- 3: introduction ----------
def n(pg, *nums):
    return [f'pg{pg:03d}_n{x:04d}' for x in nums]

page('pg003_sec001', 'text_only', 'Hyrje', f'''
<h1>{s('pg003_n0002')}</h1>
{paras([n(3, 4, 5), n(3, 7, 8)])}
<h2>{s('pg003_n0010')}</h2>
{paras([n(3, 11, 12, 13, 14, 15, 16), n(3, 18, 19)])}
<h2>{s('pg003_n0021')}</h2>
{paras([n(3, 22), n(3, 24, 25), n(3, 27), n(3, 29, 30), n(3, 32)])}''', role='article')

# ---------- 4-5: table of contents ----------
def toc_block(theme_id, rows, pg):
    lis = ''.join(
        f'<li><a href="pg{target:03d}_sec001.html">{s(f"pg{pg:03d}_n{t:04d}")}</a>'
        f'<span class="bk-toc-page"><span class="bk-sr">faqja </span>{s(f"pg{pg:03d}_n{t + 1:04d}")}</span></li>'
        for t, target in rows)
    return f'<h2 class="bk-toc-theme">{s(theme_id)}</h2>\n<ol class="bk-toc">{lis}</ol>'

page('pg004_sec001', 'table_of_contents', 'Përmbajtja', f'''
<h1>{s('pg004_n0002')}</h1>
<nav aria-labelledby="toc-h">
<span id="toc-h" class="bk-sr">Përmbajtja, tematikat 1 deri 3</span>
{toc_block('pg004_n0004', [(7, 6), (10, 8), (13, 11), (16, 14)], 4)}
{toc_block('pg004_n0019', [(22, 17), (25, 19), (28, 22), (31, 25)], 4)}
{toc_block('pg004_n0034', [(37, 29), (40, 32), (43, 34)], 4)}
</nav>''', role='article')

page('pg005_sec001', 'table_of_contents', 'Përmbajtja (vazhdim)', f'''
<h1>{s('pg004_n0002')}</h1>
<nav aria-labelledby="toc-h">
<span id="toc-h" class="bk-sr">Përmbajtja, tematikat 4 deri 6</span>
{toc_block('pg005_n0002', [(5, 35), (8, 38), (11, 40), (14, 42), (17, 44)], 5)}
{toc_block('pg005_n0020', [(23, 46), (26, 49), (29, 52), (32, 54)], 5)}
{toc_block('pg005_n0035', [(38, 57), (41, 59), (44, 62), (47, 64)], 5)}
</nav>''', role='article')

# ---------- 6: lesson 1 opener ----------
STORY6 = [n(6, 20, 21, 22), n(6, 23, 24, 25, 26, 27, 28, 29, 30, 31), n(6, 32, 33)]
page('pg006_sec001', 'text_and_single_image', '1. Vallja e materialeve', f'''
{crumb(TH1)}
{lesson_title('pg006_n0004', 'pg006_n0005')}
<div class="bk-opener bk-opener--split">
{figure('pg006_im001')}
{note('pg006_n0007', n(6, 10, 12, 14, 16), 'pg006_n0017', 'pg006_n0018')}
</div>
{story(STORY6)}''', 6, role='article')

page('pg006_sec002', 'activity_open_ended_answer', 'Vallja e materialeve: mendo dhe përgjigju', f'''
{crumb(TH1, *L1)}
{rubric('think', 'adt_think')}
{reread(STORY6)}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg006_n0035'])}
{question(['pg006_n0037'])}
{question(['pg006_n0038'])}
</div>
{reset()}''', 6)

new('pg006_ac001', 'Zgjidh materialet që përmenden në ëndrrën e Diellit.')
MATS = [('dru', 1, '🌳'), ('lesh', 0, '🐑'), ('metal', 1, '🔧'), ('plastikë', 1, '🥤'), ('gomë', 0, '🎈'), ('qelq', 1, '🥛'), ('porcelan', 1, '☕'),
        ('pambuk', 1, '👕'), ('lëkurë', 0, '👞'), ('ar', 1, '🥇'), ('argjend', 1, '🥈'), ('diamant', 1, '💎')]
opts, key = [], {}
for k, (word, ok, emo) in enumerate(MATS, 1):
    i = new(f'pg006_ac{k + 1:03d}', word)
    key[f'm{k}'] = bool(ok)
    opts.append(f'<label class="activity-option bk-option bk-option--sym"><input type="checkbox" name="mats" data-activity-item="m{k}"><span class="bk-sym" aria-hidden="true">{emo}</span>{s(i)}</label>')
page('pg006_sec003', 'activity_multi_select', 'Vallja e materialeve: materialet në ëndërr', f'''
{crumb(TH1, *L1)}
{rubric('think', 'adt_think')}
<p class="bk-task-body">{s('pg006_ac001')}</p>
{reread(STORY6)}
{how('adt_how_select')}
<div class="bk-options">
{chr(10).join(opts)}
</div>''', 6, attrs=f" data-correct-answers='{json.dumps(key)}'", scripts=answers_script(key))

# ---------- 7 ----------
page('pg007_sec001', 'text_and_single_image', 'Vallja e materialeve: lexo dhe mëso', f'''
{crumb(TH1, *L1)}
{rubric('learn', 'adt_learn')}
{info(paras([n(7, 3, 4, 5, 6, 7), n(7, 10, 11, 12, 13, 14, 15)]), figure('pg007_im002'))}''', 7, role='article')

new('pg007_ac001', 'Radhit veprimet që duhen për të prodhuar letrën, nga i pari tek i fundit.')
for k in (22, 24, 26, 28, 30):
    EDIT[f'pg007_n{k:04d}'] = T[f'pg007_n{k:04d}'].replace('□ ', '').replace('□', '').strip()
ORDER7 = {'s1': 4, 's2': 2, 's3': 3, 's4': 1, 's5': 5}
items = ''.join(f'<li data-activity-item="s{j}">{deco(f"images/pg007_im002_{c}.png")}{s(f"pg007_n{k:04d}")}</li>' for j, (k, c) in enumerate(((22, 'e'), (24, 'c'), (26, 'd'), (28, 'b'), (30, 'f')), 1))
page('pg007_sec002', 'activity_ordering', 'Vallja e materialeve: tani radhën e ke ti', f'''
{crumb(TH1, *L1)}
{rubric('turn', 'pg007_n0017')}
{task('pg007_n0019', p('pg007_ac001'))}
{how('adt_how_order')}
<ol class="bk-order bk-order--pics" data-activity-order-list>{items}</ol>''', 7, scripts=answers_script(ORDER7))

new('pg007_ac002', 'Shkruaj cilat letra gjete dhe si i grupove.')
page('pg007_sec003', 'activity_open_ended_answer', 'Vallja e materialeve: puno në shtëpi', f'''
{crumb(TH1, *L1)}
{rubric('home', 'pg007_n0032')}
{task('pg007_n0034', p('pg007_n0035', 'pg007_n0036'))}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg007_ac002'], rows=5)}
</div>
{reset()}''', 7)

# ---------- 8 ----------
new('pg008_ac001', 'Si quhet ky objekt?')
new('pg008_ac002', 'Objekti 1')
new('pg008_ac003', 'Objekti 2')
new('pg008_ac004', 'Objekti 3')
named = ''
for j, (im, lab) in enumerate([('pg008_im001', 'pg008_ac002'), ('pg008_im003', 'pg008_ac003'), ('pg008_im002', 'pg008_ac004')], 1):
    fid = f'o{j}'
    named += (f'<li>{img(im)}<label for="{fid}">{s(lab)}<span class="bk-hint" data-id="pg008_ac001">{esc(tx("pg008_ac001"))}</span></label>'
              f'<input type="text" id="{fid}" data-aria-id="{fid}" data-activity-item="item-{j}" autocomplete="off"></li>')
KEY8 = {'item-1': 'qese letre|qese|qese prej letre|çantë letre|çantë|çantë prej letre|torbë letre|torbë|qesja|çanta',
        'item-2': 'letër higjienike|letër banje|letër tualeti|rrotull letre|letër|letra higjienike',
        'item-3': 'libër|libri|një libër|fletore|libra'}
page('pg008_sec001', 'activity_fill_in_the_blank', '2. Dita dhe Dielli në punëtori', f'''
{crumb(TH1)}
{lesson_title('pg008_n0004', 'pg008_n0005')}
{note('pg008_n0017', n(8, 20, 22, 24), 'pg008_n0025', 'pg008_n0026')}
<p class="bk-task-body">{s('pg008_n0007')}</p>
{how('adt_how_write')}
<ol class="bk-named bk-named--3">{named}</ol>
<div class="bk-panel">
{question(['pg008_n0008'])}
{question(['pg008_n0009'])}
</div>
{reset()}''', 8, scripts=answers_script(KEY8))

page('pg008_sec002', 'boxed_text', 'Dita dhe Dielli në punëtori: lexo dhe mëso', f'''
{crumb(TH1, *L2)}
{rubric('learn', 'adt_learn')}
{info(paras([n(8, 29, 30, 31, 32, 33), n(8, 35, 36)]))}''', 8, role='article')

# ---------- 9: sorting properties ----------
new('pg009_ac010', 'Vendos secilën veti në kutinë e duhur: vetitë e letrës, vetitë e përbashkëta ose vetitë e kartonit.')
KEY9 = {}
cards = ''
for k, cat in [(30, 'bashke'), (32, 'kartoni'), (34, 'bashke'), (36, 'letra'), (38, 'kartoni'), (40, 'letra'),
               (42, 'bashke'), (44, 'letra'), (46, 'kartoni'), (48, 'bashke'), (50, 'kartoni')]:
    KEY9[f'v{k}'] = cat
    cards += f'<div class="word-card bk-card bk-card--text" data-activity-item="v{k}">{s(f"pg009_n{k:04d}")}</div>\n'
def cat(cid, label_id, extra=''):
    return (f'<div class="category bk-cat" data-activity-category="{cid}" aria-label="{esc(tx(label_id))}">'
            f'<h2 class="font-semibold" data-id="{label_id}">{esc(tx(label_id))}</h2>{extra}<div class="word-list"></div></div>')
page('pg009_sec001', 'activity_sorting', 'Dita dhe Dielli në punëtori: tani radhën e ke ti', f'''
{crumb(TH1, *L2)}
{rubric('turn', 'pg009_n0003')}
{task('pg009_n0005', '<p class="bk-soft">' + ' '.join(s(x) for x in n(9, 6, 7, 8, 9)) + '</p>', p('pg009_ac010'))}
<div class="bk-talk">
<figure>{img('pg009_im001')}<figcaption>{s('pg009_n0023')}</figcaption></figure>
<figure>{img('pg009_im002')}<figcaption>{s('pg009_n0027')}</figcaption></figure>
</div>
{how('adt_how_sort')}
<div class="bk-pool" role="group" aria-label="{esc(tx('adt_cards'))}">
{cards}</div>
<div class="bk-cats bk-cats--3">
{cat('letra', 'pg009_n0022')}
{cat('bashke', 'pg009_n0015', '<p class="bk-cat-example">' + s('pg009_n0016') + '</p>')}
{cat('kartoni', 'pg009_n0026')}
</div>''', 9, attrs=f" data-correct-answers='{json.dumps(KEY9)}'", scripts=answers_script(KEY9))

# ---------- 10: craft ----------
page('pg010_sec001', 'text_and_single_image', 'Dita dhe Dielli në punëtori: puno në shtëpi', f'''
{crumb(TH1, *L2)}
{rubric('home', 'pg010_n0005')}
{task('pg010_n0007', p('pg010_n0008', 'pg010_n0009'))}
{p('pg010_n0010')}
<ol class="bk-steps">
<li>{s('pg010_n0011')} {s('pg010_n0012')}</li>
<li>{s('pg010_n0013')}</li>
<li>{s('pg010_n0014')}</li>
<li>{s('pg010_n0015')}</li>
<li>{s('pg010_n0016')}</li>
</ol>
{how('adt_help_craft')}
{figure('pg010_im002')}''', 10, role='article')

# ---------- 11 ----------
STORY11 = [n(11, 21, 22, 23, 24, 25, 26)]
page('pg011_sec001', 'text_and_single_image', '3. Dita dhe lulja e veçantë', f'''
{crumb(TH1)}
{lesson_title('pg011_n0004', 'pg011_n0005')}
<div class="bk-opener bk-opener--split">
{figure('pg011_im001')}
{note('pg011_n0008', n(11, 11, 13, 15), 'pg011_n0017', 'pg011_n0019')}
</div>
{story(STORY11)}''', 11, role='article')

page('pg011_sec002', 'activity_open_ended_answer', 'Dita dhe lulja e veçantë: mendo dhe përgjigju', f'''
{crumb(TH1, *L3)}
{rubric('think', 'adt_think')}
{reread(STORY11)}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg011_n0029'])}
{question(['pg011_n0031'])}
</div>
{reset()}''', 11)

# ---------- 12 ----------
page('pg012_sec001', 'boxed_text', 'Dita dhe lulja e veçantë: lexo dhe mëso', f'''
{crumb(TH1, *L3)}
{rubric('learn', 'adt_learn')}
{info(paras([n(11, 34, 35, 36, 37), n(11, 39, 40, 41), n(12, 5, 6)]), figure('pg012_im001', 'pg012_n0008'))}''', 12, role='article')

new('pg012_ac001', 'Shkruaj dy sende.')
rows = ''
for k in range(15, 23):
    i = uid('a')
    rows += (f'<div class="bk-row"><label for="{i}">{s(f"pg012_n{k:04d}")}<span class="bk-sr"> {esc(tx("pg012_ac001"))}</span></label>'
             f'<input type="text" id="{i}" data-aria-id="{i}" autocomplete="off"></div>\n')
page('pg012_sec002', 'activity_open_ended_answer', 'Dita dhe lulja e veçantë: tani radhën e ke ti', f'''
{crumb(TH1, *L3)}
{rubric('turn', 'pg012_n0011')}
{task('pg012_n0013', p('pg012_n0014'))}
{how('adt_how_write')}
<div class="bk-panel bk-fields">
{rows}</div>
{reset()}''', 12)
