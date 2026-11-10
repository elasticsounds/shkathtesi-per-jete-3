"""Pages 25-46: end of Tematika 2, Tematika 3, Tematika 4, start of Tematika 5."""
from lib import *
from pages_a import n, cat

TH2, TH3, TH4, TH5, TH6 = 'pg018_n0002', 'pg030_n0002', 'pg036_n0002', 'pg048_n0002', 'pg058_n0002'

new('adt_true', 'E saktë')
new('adt_false', 'E gabuar')
new('adt_how_choose', 'Për secilën pyetje, zgjidh një përgjigje. Kur të mbarosh, shtyp butonin “Dërgo”.')
new('adt_help_act', 'Mund ta tregosh me fjalë, me zë, me lëvizje ose me vizatim, si të vijë më lehtë. Kërko ndihmën e një shoku, një shoqeje ose të një të rrituri kur të duhet.')

# ---------- generic builders ----------
def note2(learn_h, learn_ids, kw_h=None, kw_ids=()):
    lis = ''.join(f'<li>{s(i)}</li>' for i in learn_ids)
    kw = f'<h2 data-id="{kw_h}">{esc(tx(kw_h))}</h2><p>' + ' '.join(s(i) for i in kw_ids) + '</p>' if kw_h else ''
    return (f'<aside class="bk-note" aria-labelledby="note-h"><h2 id="note-h" data-id="{learn_h}">{esc(tx(learn_h))}</h2>'
            f'<ul>{lis}</ul>{kw}</aside>')

def opener(sid, pg, theme, num, ttl, title, im, note_html, story_groups, extra='', sub=None):
    fig = figure(im) if im else ''
    subt = f'<p class="bk-task-body">{s(sub)}</p>' if sub else ''
    top = f'<div class="bk-opener bk-opener--split">\n{fig}\n{note_html}\n</div>' if fig else note_html
    page(sid, 'text_and_single_image', title, f'''
{crumb(theme)}
{lesson_title(num, ttl)}
{subt}
{top}
{story(story_groups) if story_groups else ''}
{extra}''', pg, role='article')

def think(sid, pg, theme, lesson, title, story_groups, qids, pre=''):
    page(sid, 'activity_open_ended_answer', title + ': mendo dhe përgjigju', f'''
{crumb(theme, lesson)}
{rubric('think', 'adt_think')}
{reread(story_groups) if story_groups else ''}
{pre}
{how('adt_how_write')}
<div class="bk-panel">
{''.join(question(q if isinstance(q, list) else [q]) for q in qids)}
</div>
{reset()}''', pg)

def infopage(sid, pg, theme, lesson, title, *blocks):
    page(sid, 'boxed_text', title + ': lexo dhe mëso', f'''
{crumb(theme, lesson)}
{rubric('learn', 'adt_learn')}
{info(*blocks)}''', pg, role='article')

def lettered(pg, nums):
    """Rows 'a) ____' : the letter is the visible label."""
    out = ''
    for k in nums:
        i = uid('a')
        lid = f'pg{pg:03d}_n{k:04d}'
        out += (f'<div class="bk-row bk-row--short"><label for="{i}">{s(lid)}</label>'
                f'<input type="text" id="{i}" data-aria-id="{i}" autocomplete="off"></div>\n')
    return f'<div class="bk-panel bk-fields">{out}</div>'

def numbered(count, label_id):
    out = ''
    for k in range(1, count + 1):
        i = uid('a')
        out += (f'<div class="bk-row bk-row--short"><label for="{i}">{k}.<span class="bk-sr"> {esc(tx(label_id))}</span></label>'
                f'<input type="text" id="{i}" data-aria-id="{i}" autocomplete="off"></div>\n')
    return f'<div class="bk-panel bk-fields">{out}</div>'

def written(sid, pg, theme, lesson, title, kind, rub, body, family='activity_open_ended_answer', scripts=''):
    page(sid, family, title, f'''
{crumb(theme, lesson)}
{rubric(kind, rub)}
{body}
{reset()}''', pg, scripts=scripts)

def choice(item, legend, options, wide=False):
    radios = ''.join(
        f'<label class="bk-radio"><input type="radio" name="{item}" value="{v}" data-activity-item="{item}">{s(t)}'
        f'<span class="validation-mark hidden"></span></label>' for v, t in options)
    cls = 'bk-pick bk-pick--wide' if wide else 'bk-pick'
    return f'<fieldset class="{cls}"><legend>{legend}</legend><div class="bk-radios">{radios}</div></fieldset>\n'

# ====================== 25: role play ======================
L24 = 'pg004_n0031'
page('pg025_sec001', 'text_and_single_image', '4. Luajmë “profesionesh”', f'''
{crumb(TH2)}
{lesson_title('pg025_n0003', 'pg025_n0004')}
<p class="bk-task-body">{s('pg025_n0005')}</p>
{figure('pg025_im001')}
<ol class="bk-steps">
<li>{s('pg025_n0008')}</li>
<li>{s('pg025_n0009')}</li>
<li>{s('pg025_n0010')} {s('pg025_n0011')}</li>
<li>{s('pg025_n0012')} {s('pg025_n0013')} {s('pg025_n0014')}</li>
<li>{s('pg025_n0015')} {s('pg025_n0016')} {s('pg025_n0017')}</li>
<li>{s('pg025_n0018')}</li>
</ol>
{how('adt_help_act')}''', 25, role='article')

# ====================== 26: choose the profession ======================
new('pg026_ac001', 'Për secilën figurë, zgjidh profesionin e saktë.')
P26 = [  # image, new description, option ids, correct letter
    ('pg026_im011', 'Burrë me kapelë të bardhë dhe përparëse, që mban një bukë të pjekur.', (13, 15, 17), 'a'),
    ('pg026_im002', 'Grua me mantel të bardhë dhe stetoskop në qafë.', (20, 22, 24), 'c'),
    ('pg026_im015', 'Djalë që këndon me mikrofon në dorë.', (27, 29, 31), 'a'),
    ('pg026_im013', 'Burrë me helmetë dhe uniformë mbrojtëse, që mban një zorrë uji.', (35, 37, 39), 'c'),
    ('pg026_im005', 'Burrë me kapelë të bardhë deti, që shikon me dylbi.', (42, 44, 46), 'b'),
    ('pg026_im006', 'Grua që shpjegon pranë dërrasës së zezë me një shkop tregues.', (49, 51, 53), 'a'),
    ('pg026_im014', 'Njeri me kostum të bardhë hapësinor dhe helmetë, që përshëndet.', (57, 59, 61), 'a'),
    ('pg026_im009', 'Vajzë që bën fotografi me aparat.', (64, 66, 68), 'a'),
    ('pg026_im007', 'Burrë me kapelë kashte, që mban një sfurk.', (71, 73, 75), 'c'),
    ('pg026_im010', 'Burrë që riparon një këpucë në tavolinën e punës.', (79, 81, 83), 'a'),
    ('pg026_im012', 'Burrë me çantë në sup, që mban një zarf.', (86, 88, 90), 'c'),
    ('pg026_im001', 'Burrë me mantel të bardhë, që kontrollon dhëmbët e një vajze.', (93, 95, 97), 'c'),
    ('pg026_im003', 'Grua me mantel të bardhë, që kontrollon një qen me stetoskop.', (101, 103, 105), 'b'),
    ('pg026_im008', 'Burrë me veshje pune, që mban një llambë dhe tela.', (108, 110, 112), 'a'),
    ('pg026_im004', 'Vajzë me fustan rozë, që kërcen në majë të gishtave.', (115, 117, 119), 'b')]
for part in range(3):
    key, picks = {}, ''
    for j in range(part * 5, part * 5 + 5):
        im, alt, opts, ok = P26[j]
        did = new(f'{im}_d', alt)
        item = f'f{j + 1}'
        key[item] = ok
        legend = f'<span class="bk-pick-img"><img data-id="{did}" src="images/{im}.png" alt="{esc(alt)}"></span><span class="bk-sr">Figura {j + 1}</span>'
        picks += choice(item, legend, [(v, f'pg026_n{o:04d}') for v, o in zip('abc', opts)])
    page(f'pg026_sec{part + 1:03d}', 'activity_true_false', f'Luajmë “profesionesh”: zgjidh profesionin ({part + 1} nga 3)', f'''
{crumb(TH2, L24)}
{rubric('turn', 'pg026_n0004')}
{task('pg026_n0006', '<p class="bk-soft">' + s('pg026_n0007') + '</p>', p('pg026_ac001'))}
{how('adt_how_choose')}
<div class="bk-picks">
{picks}</div>''', 26, scripts=answers_script(key))

# ====================== 27: hidden professions ======================
new('pg027_ac001', 'Shkronjat e secilit profesion janë përzier. Vendosi në radhë dhe shkruaj emrin e profesionit.')
new('pg027_ac002', 'Nëse sheh mirë, mund t’i kërkosh profesionet edhe në tetëkëndëshin me shkronja.')
new('pg027_ac003', 'Shkronjat:')
new('pg027_ac004', 'Fillon me shkronjën')
W27 = [('murator', 'R O T A R U M'), ('polic', 'L I C O P'), ('mësues', 'S U M Ë S E'), ('dentist', 'T S I T N E D'),
       ('fotograf', 'F A R G O T O F'), ('postier', 'R E I T S O P'), ('kamerier', 'R E I R E M A K'),
       ('bukëpjekës', 'S Ë K E J P Ë K U B'), ('elektricist', 'T S I C I R T K E L E')]
key, rows = {}, ''
for j, (w, sc) in enumerate(W27, 1):
    plain = w.replace('ë', 'e')
    key[f'item-{j}'] = w if plain == w else f'{w}|{plain}'
    fid = f'w{j}'
    rows += (f'<li><div><label for="{fid}">{j}. {s("pg027_ac003")} <span class="bk-letters">{sc}</span>'
             f'<span class="bk-hint">{s("pg027_ac004")} {w[0].upper()}.</span></label>'
             f'<input type="text" id="{fid}" data-aria-id="{fid}" data-activity-item="item-{j}" autocomplete="off" autocapitalize="none" spellcheck="false"></div></li>\n')
written('pg027_sec001', 27, TH2, L24, 'Luajmë “profesionesh”: profesionet e fshehura', 'class', 'pg027_n0004', f'''
{task('pg027_n0006', '<p class="bk-soft">' + s('pg027_n0007') + '</p>', p('pg027_ac001'))}
{how('adt_how_write')}
<ol class="bk-clues bk-clues--plain">
{rows}</ol>
{how('pg027_ac002')}
{figure('pg027_im002')}''', family='activity_fill_in_the_blank', scripts=answers_script(key))

# ====================== 28: who said it ======================
new('pg028_ac001', 'Vendos secilën fjali te profesionisti që e tha.')
Q28 = [  # quote ids, image, profession name
    ((14,), 'pg028_im002', 'Zjarrfikësi'), ((16, 17), 'pg028_im006', 'Stjuardesa'), ((19,), 'pg028_im003', 'Mjekja'), ((21,), 'pg028_im004', 'Taksisti'),
    ((23,), 'pg028_im008', 'Mësuesja'), ((25,), 'pg028_im007', 'Balerina'), ((27,), 'pg028_im005', 'Fotografi'), ((29,), 'pg028_im009', 'Sekretarja')]
for part, zone_order in ((0, [1, 3, 0, 2]), (1, [2, 0, 3, 1])):
    key, chips, zones = {}, '', {}
    for j in range(part * 4, part * 4 + 4):
        qs, im, name = Q28[j]
        nid = new(f'pg028_ac{j + 2:03d}', name)
        key[f'q{j}'] = f'z{j}'
        chips += f'<div class="activity-item bk-chip bk-chip--quote" data-activity-item="q{j}">' + ' '.join(s(f'pg028_n{q:04d}') for q in qs) + '</div>\n'
        zones[j - part * 4] = (f'<div class="dropzone bk-zone">{deco(f"images/{im}.png")}<span class="bk-zone-name" data-id="{nid}">{esc(name)}</span>'
                               f'<div class="dropzone-slot bk-slot" id="z{j}"></div></div>\n')
    page(f'pg028_sec{part + 1:03d}', 'activity_matching', f'Luajmë “profesionesh”: kush e tha? ({part + 1} nga 2)', f'''
{crumb(TH2, L24)}
{rubric('home', 'pg028_n0004')}
{task('pg028_n0006', '<p class="bk-soft">' + s('pg028_n0007') + ' ' + s('pg028_n0008') + '</p>', p('pg028_ac001'))}
<h2>{s('pg028_n0010')}</h2>
{how('adt_how_match')}
<div class="bk-pool" role="group" aria-label="{esc(tx('adt_cards'))}">
{chips}</div>
<div class="bk-zones bk-zones--2">
{''.join(zones[k] for k in zone_order)}</div>''', 28, attrs=f" data-correct-answers='{json.dumps(key)}'", scripts=answers_script(key))

# ====================== 29-31: Tematika 3, lesson 1 ======================
L31 = 'pg004_n0037'
STORY29 = [n(29, 18, 19, 20, 21), n(29, 22, 23, 24)]
opener('pg029_sec001', 29, TH3, 'pg029_n0004', 'pg029_n0005', '1. Familja e Ditës planifikon një udhëtim', 'pg029_im001',
       note('pg029_n0007', n(29, 10, 12, 14), 'pg029_n0015', 'pg029_n0016'), STORY29)
think('pg029_sec002', 29, TH3, L31, 'Familja e Ditës planifikon një udhëtim', STORY29, n(29, 27, 29))
infopage('pg030_sec001', 30, TH3, L31, 'Familja e Ditës planifikon një udhëtim',
         paras([n(30, 4, 5), n(30, 7, 8), n(30, 10, 11, 12, 13, 14, 15)]))

new('pg030_ac001', 'Për secilën fjali, zgjidh “E saktë” ose “E gabuar”.')
key, picks = {}, ''
for j, (k, ok) in enumerate([(28, 'gabuar'), (30, 'sakte'), (32, 'gabuar'), (34, 'gabuar')], 1):
    tid = f'pg030_n{k:04d}'
    EDIT[tid] = T[tid].replace('□ ', '').replace('□', '').strip()
    key[f't{j}'] = ok
    picks += choice(f't{j}', s(tid), [('sakte', 'adt_true'), ('gabuar', 'adt_false')], wide=True)
page('pg030_sec002', 'activity_true_false', 'Familja e Ditës planifikon një udhëtim: puno në klasë', f'''
{crumb(TH3, L31)}
{rubric('class', 'pg030_n0018')}
{task('pg030_n0020', '<p class="bk-soft">' + ' '.join(s(x) for x in n(30, 22, 23, 24, 25)) + '</p>', p('pg030_ac001'))}
{figure('pg030_im001')}
{how('adt_how_choose')}
<div class="bk-picks bk-picks--list">
{picks}</div>''', 30, scripts=answers_script(key))

written('pg031_sec001', 31, TH3, L31, 'Familja e Ditës planifikon një udhëtim: puno në shtëpi', 'home', 'pg031_n0003', f'''
{task('pg031_n0005', p('pg031_n0006'))}
{figure('pg031_im001')}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg031_n0010'], kind='input')}
{question(['pg031_n0013'])}
{question(['pg031_n0015'])}
{question(['pg031_n0017'])}
</div>''')

# ====================== 32-33: lesson 2 ======================
L32 = 'pg004_n0040'
STORY32 = [n(32, 17, 18, 19), n(32, 20, 21)]
opener('pg032_sec001', 32, TH3, 'pg032_n0004', 'pg032_n0005', '2. Unë ndihmoj në familje', 'pg032_im001',
       note('pg032_n0007', n(32, 10, 12), 'pg032_n0013', 'pg032_n0015'), STORY32)
think('pg032_sec002', 32, TH3, L32, 'Unë ndihmoj në familje', STORY32, n(32, 24, 26, 28))
infopage('pg033_sec001', 33, TH3, L32, 'Unë ndihmoj në familje',
         paras([n(32, 31, 32, 33), n(33, 4, 5), n(33, 7)]),
         '<ul class="bk-plainlist">' + ''.join(f'<li>{s(x)}</li>' for x in n(33, 8, 9, 10, 11, 12)) + '</ul>',
         p('pg033_n0014'))

rows = ''
for k in range(24, 32):
    tid = f'pg033_n{k:04d}'
    EDIT[tid] = T[tid].lstrip('–- ').strip()
    rows += question([tid], kind='input')
written('pg033_sec002', 33, TH3, L32, 'Unë ndihmoj në familje: puno në klasë', 'class', 'pg033_n0018', f'''
{task('pg033_n0020', p('pg033_n0021', 'pg033_n0022'), p('pg033_n0023'))}
{how('adt_how_write')}
<div class="bk-panel">
{rows}
</div>''')

new('pg033_ac001', 'Veprimi')
written('pg033_sec003', 33, TH3, L32, 'Unë ndihmoj në familje: puno në shtëpi', 'home', 'pg033_n0033', f'''
{task('pg033_n0035', p('pg033_n0036'))}
{how('adt_how_write')}
{numbered(5, 'pg033_ac001')}''')

# ====================== 34: savings box ======================
page('pg034_sec001', 'text_and_images', '3. Ndërtimi i arkës së kursimeve', f'''
{crumb(TH3)}
{lesson_title('pg034_n0004', 'pg034_n0005')}
<p class="bk-task-body">{s('pg034_n0006')}</p>
<aside class="bk-note" aria-labelledby="note-h"><h2 id="note-h" data-id="pg034_n0009">{esc(tx('pg034_n0009'))}</h2>
<ul>{''.join(f'<li>{s(x)}</li>' for x in n(34, 12, 14, 16))}</ul>
<h2 data-id="pg034_n0018">{esc(tx('pg034_n0018'))}</h2>{p('pg034_n0019')}</aside>
{figure('pg034_im001')}
{story([n(34, 21, 22, 23, 24)])}
<ol class="bk-steps">
<li>{s('pg034_n0026')}</li>
<li>{s('pg034_n0027')}</li>
<li>{s('pg034_n0029')}</li>
<li>{s('pg034_n0030')}</li>
</ol>
{figure('pg034_im002')}
<p class="bk-task-body">{s('pg034_n0031')}</p>
{how('adt_help_craft')}''', 34, role='article')

# ====================== 35-37: Tematika 4, lesson 1 ======================
L41 = 'pg005_n0005'
STORY35 = [n(35, 22, 23, 24, 25, 26), n(35, 27, 28)]
opener('pg035_sec001', 35, TH4, 'pg035_n0004', 'pg035_n0005', '1. Ki kujdes, Dielli!', 'pg035_im001',
       note('pg035_n0008', n(35, 11, 13, 15, 17), 'pg035_n0019', 'pg035_n0020'), STORY35)
think('pg035_sec002', 35, TH4, L41, 'Ki kujdes, Dielli!', STORY35, ['pg035_n0029'])
infopage('pg035_sec003', 35, TH4, L41, 'Ki kujdes, Dielli!',
         paras([n(35, 32, 33, 34), n(35, 35), n(35, 36, 37)]), '<p class="bk-task-body">' + s('pg035_n0038') + '</p>')

new('pg036_ac001', 'Cili është rreziku? Çfarë duhet bërë?')
R36 = [('pg036_im002', 'Makinë që udhëton me shumë valixhe të lidhura mbi çati.'),
       ('pg036_im006', 'Vajzë që lan dyshemenë; në dysheme ka ujë të derdhur.'),
       ('pg036_im008', 'Fëmijë pranë sobës, ku një tenxhere po zien.'),
       ('pg036_im005', 'Vajzë që hekuros rroba me hekur të nxehtë.'),
       ('pg036_im007', 'Dorë që mban një spinë pranë prizës elektrike.'),
       ('pg036_im009', 'Grua dhe fëmijë që kalojnë rrugën te vendkalimi i këmbësorëve, me semafor të gjelbër.')]
items = ''
for j, (im, alt) in enumerate(R36, 1):
    did = new(f'{im}_d', alt)
    fid = f'r{j}'
    items += (f'<li><img data-id="{did}" src="images/{im}.png" alt="{esc(alt)}">'
              f'<label for="{fid}"><span class="bk-sr">Figura {j}. </span>{s("pg036_ac001")}</label>'
              f'<textarea id="{fid}" data-aria-id="{fid}" rows="3"></textarea></li>\n')
written('pg036_sec001', 36, TH4, L41, 'Ki kujdes, Dielli!: puno në klasë', 'class', 'pg036_n0004', f'''
{task('pg036_n0006', p('pg036_n0007', 'pg036_n0008'))}
{how('adt_how_write')}
<ol class="bk-named bk-named--2">
{items}</ol>''')

new('pg036_ac002', 'Vendos secilin kuptim poshtë shenjës së duhur.')
new('pg036_ac008', 'Ku mund të vendoset kjo shenjë?')
S36 = [('pg036_im010_crop_v1', 'Trekëndësh i verdhë me një flakë në mes.', 'Mund të ketë zjarr.'),
       ('pg036_im011', 'Trekëndësh i verdhë me një send që shpërthen në copa.', 'Mund të shpërthejë.'),
       ('pg036_im003_crop_v1', 'Trekëndësh i verdhë me një kafkë dhe dy kocka të kryqëzuara.', 'Mund të sëmurem.'),
       ('pg036_im004', 'Trekëndësh i verdhë me një njeri që rrëshqet dhe rrëzohet.', 'Mund të rrëshqas.')]
key, chips, zones, ex = {}, {}, '', ''
for j, (im, alt, meaning) in enumerate(S36, 1):
    did = new(f'{im}_d', alt)
    mid = new(f'pg036_ac{j + 2:03d}', meaning)
    key[f'm{j}'] = f'z{j}'
    chips[j] = f'<div class="activity-item bk-chip" data-activity-item="m{j}">{s(mid)}</div>\n'
    zones += f'<div class="dropzone bk-zone"><img data-id="{did}" src="images/{im}.png" alt="{esc(alt)}"><div class="dropzone-slot bk-slot" id="z{j}"></div></div>\n'
    fid = f'e{j}'
    ex += (f'<li><img data-id="{did}" src="images/{im}.png" alt="{esc(alt)}"><p>{s(mid)}</p>'
           f'<label for="{fid}">{s("pg036_ac008")}</label><input type="text" id="{fid}" data-aria-id="{fid}" autocomplete="off"></li>\n')
page('pg036_sec002', 'activity_matching', 'Ki kujdes, Dielli!: shenjat e rrezikut', f'''
{crumb(TH4, L41)}
{rubric('home', 'pg036_n0022')}
{task('pg036_n0024', p('pg036_n0025'), p('pg036_ac002'))}
{how('adt_how_match')}
<div class="bk-pool" role="group" aria-label="{esc(tx('adt_cards'))}">
{chips[3]}{chips[1]}{chips[4]}{chips[2]}</div>
<div class="bk-zones">
{zones}</div>''', 36, attrs=f" data-correct-answers='{json.dumps(key)}'", scripts=answers_script(key))
written('pg036_sec003', 36, TH4, L41, 'Ki kujdes, Dielli!: ku vendosen shenjat', 'home', 'pg036_n0022', f'''
<p class="bk-task-body">{s('pg036_n0026')}</p>
{p('pg036_n0027')}
{how('adt_how_write')}
<ol class="bk-named bk-named--2">
{ex}</ol>''')

new('pg037_ac001', 'Zgjidh të gjitha burimet e rrezikut që Dielli duhet t’i shmangë rrugës për në shtëpi.')
H37 = [('Shkallë e lëkundur', 1), ('Trotuari', 0), ('Shiringë e hedhur në tokë', 1), ('Kabllo dhe priza elektrike', 1), ('Vendkalimi i këmbësorëve', 0),
       ('Fuçi me lëndë helmuese', 1), ('Sharrë elektrike', 1), ('Stoli në park', 0), ('Pirun ngarkues që lëviz', 1), ('Kuti të rënda të vëna njëra mbi tjetrën', 1)]
key, opts = {}, ''
for j, (label, ok) in enumerate(H37, 1):
    i = new(f'pg037_ac{j + 1:03d}', label)
    key[f'h{j}'] = bool(ok)
    opts += f'<label class="activity-option bk-option"><input type="checkbox" name="haz" data-activity-item="h{j}">{s(i)}</label>\n'
page('pg037_sec001', 'activity_multi_select', 'Ki kujdes, Dielli!: rruga për në shtëpi', f'''
{crumb(TH4, L41)}
{rubric('home', 'pg037_n0004')}
{task('pg037_n0006', '<p class="bk-soft">' + s('pg037_n0007') + '</p>', p('pg037_ac001'))}
{figure('pg037_im001')}
{how('adt_how_select')}
<div class="bk-options bk-options--wide">
{opts}</div>''', 37, attrs=f" data-correct-answers='{json.dumps(key)}'", scripts=answers_script(key))

# ====================== 38-39: lesson 2 ======================
L42 = 'pg005_n0008'
STORY38 = [n(38, 22, 23, 24)]
opener('pg038_sec001', 38, TH4, 'pg038_n0004', 'pg038_n0005', '2. Dielli pastron shtëpinë', 'pg038_im001',
       note2('pg038_n0008', n(38, 11, 13, 15), 'pg038_n0016', n(38, 18, 19, 20)), STORY38, extra=figure('pg038_im002'))
think('pg038_sec002', 38, TH4, L42, 'Dielli pastron shtëpinë', STORY38, n(38, 27, 29))
infopage('pg039_sec001', 39, TH4, L42, 'Dielli pastron shtëpinë',
         paras([n(38, 32, 33, 34), n(38, 35)]),
         '<ul class="bk-plainlist"><li>' + ' '.join(s(x) for x in n(39, 5, 6, 7, 8)) + f'</li><li>{s("pg039_n0010")}</li><li>{s("pg039_n0012")}</li></ul>')

new('pg039_ac001', 'Vendos lëngjet e rrezikshme në kutinë “Lëngje të rrezikshme” dhe të tjerat në kutinë “Lëngje jo të rrezikshme”.')
new('pg039_ac002', 'Lëngje të rrezikshme')
new('pg039_ac003', 'Lëngje jo të rrezikshme')
LQ = [('a', 'Qumësht në kuti', 'jo'), ('b', 'Ilaç i derdhur në lugë', 'po'), ('c', 'Sprej për pastrim', 'po'), ('d', 'Ujë nga rubineti', 'jo'),
      ('e', 'Lëngje në enë laboratori', 'po'), ('f', 'Zbardhues', 'po'), ('g', 'Lëng portokalli', 'jo'), ('h', 'Lëng i kaltër në shishe Cola', 'po')]
key, cards = {}, ''
for j, (c, label, k) in enumerate(LQ, 1):
    i = new(f'pg039_ac{j + 3:03d}', label)
    key[f'l{c}'] = k
    cards += f'<div class="word-card bk-card" data-activity-item="l{c}">{deco(f"images/pg039_im002_{c}.png")}{s(i)}</div>\n'
page('pg039_sec002', 'activity_sorting', 'Dielli pastron shtëpinë: puno në klasë', f'''
{crumb(TH4, L42)}
{rubric('class', 'pg039_n0014')}
{task('pg039_n0016', p('pg039_ac001'))}
<h2>{s('pg039_n0020')}</h2>
{how('adt_how_sort')}
<div class="bk-pool" role="group" aria-label="{esc(tx('adt_cards'))}">
{cards}</div>
<div class="bk-cats bk-cats--2">
{cat('po', 'pg039_ac002')}
{cat('jo', 'pg039_ac003')}
</div>''', 39, attrs=f" data-correct-answers='{json.dumps(key)}'", scripts=answers_script(key))

written('pg039_sec003', 39, TH4, L42, 'Dielli pastron shtëpinë: puno në shtëpi', 'home', 'pg039_n0022', f'''
{task('pg039_n0024', p('pg039_n0025', 'pg039_n0026'))}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg039_n0030'])}
{question(['pg039_n0032'])}
</div>''')

# ====================== 40-41: lesson 3 ======================
L43 = 'pg005_n0011'
STORY40 = [n(40, 23, 24, 25, 26, 27)]
opener('pg040_sec001', 40, TH4, 'pg040_n0005', 'pg040_n0006', '3. Babai i Ditës është zjarrfikës', 'pg040_im001',
       note('pg040_n0009', n(40, 12, 14, 16, 18), 'pg040_n0020', 'pg040_n0021'), STORY40)
think('pg040_sec002', 40, TH4, L43, 'Babai i Ditës është zjarrfikës', STORY40, n(40, 30, 32, 34), pre=figure('pg040_im001'))
infopage('pg041_sec001', 41, TH4, L43, 'Babai i Ditës është zjarrfikës',
         paras([n(40, 37, 38, 39), n(40, 40), n(40, 41) + n(41, 5, 6), n(41, 7, 8, 9)]))

new('pg041_ac001', 'Zgjidh të gjitha vendet ku mund të ketë rrezik nga energjia elektrike.')
R41 = [('a', 'pg041_n0019', 'Kuzhinë: një hekur i ndezur mbi dërrasën e hekurosjes, me kabllon e shtrirë deri te priza; mbi banak janë një çajnik dhe një thekëse në prizë.'),
       ('b', 'pg041_n0020', 'Dhomë ndenjjeje: një kabllo e gjatë shtrihet nëpër dysheme nga priza deri te një lodër; pranë televizorit ka shumë spina në një prizë.'),
       ('c', 'pg041_n0021', 'Dhomë fjetjeje: në dysheme ka një tastierë muzikore me kabllo; në priza janë futur shumë spina.'),
       ('d', 'pg041_n0022', 'Banjë: një pajisje elektrike me kabllo është lënë në dysheme pranë vaskës me ujë; një radio është mbi tualet.')]
rooms = ''
for c, cap, alt in R41:
    did = new(f'pg041_im002_{c}', alt)
    rooms += f'<figure class="bk-figure">{img(did)}<figcaption data-id="{cap}">{esc(tx(cap))}</figcaption></figure>\n'
H41 = [('Hekuri i ndezur i lënë mbi dërrasën e hekurosjes', 1), ('Jastëku mbi divan', 0), ('Kabllo e gjatë e shtrirë nëpër dysheme', 1),
       ('Shumë spina të futura në një prizë', 1), ('Arushi prej pelushi mbi shtrat', 0), ('Pajisje elektrike pranë vaskës me ujë', 1),
       ('Peshqiri i varur në banjë', 0), ('Ora në mur', 0)]
key, opts = {}, ''
for j, (label, ok) in enumerate(H41, 1):
    i = new(f'pg041_ac{j + 1:03d}', label)
    key[f'e{j}'] = bool(ok)
    opts += f'<label class="activity-option bk-option"><input type="checkbox" name="el" data-activity-item="e{j}">{s(i)}</label>\n'
page('pg041_sec002', 'activity_multi_select', 'Babai i Ditës është zjarrfikës: puno në shtëpi', f'''
{crumb(TH4, L43)}
{rubric('home', 'pg041_n0011')}
{task('pg041_n0013', '<p class="bk-soft">' + s('pg041_n0014') + '</p>', p('pg041_ac001'))}
<div class="bk-fields bk-fields--2">
{rooms}</div>
{how('adt_how_select')}
<div class="bk-options bk-options--wide">
{opts}</div>
<p class="bk-task-body">{s('pg041_n0016')}</p>''', 41, attrs=f" data-correct-answers='{json.dumps(key)}'", scripts=answers_script(key))

# ====================== 42-43: lesson 4 ======================
L44 = 'pg005_n0014'
STORY42 = [n(42, 23, 24, 25, 26)]
opener('pg042_sec001', 42, TH4, 'pg042_n0005', 'pg042_n0006', '4. Kujdes, këtu punohet!', 'pg042_im001',
       note('pg042_n0009', n(42, 12, 14, 16, 18), 'pg042_n0020', 'pg042_n0021'), STORY42)
think('pg042_sec002', 42, TH4, L44, 'Kujdes, këtu punohet!', STORY42, n(42, 29, 31))
RULES43 = [n(42, 33, 34, 35), n(42, 37, 38), n(42, 39) + n(43, 5, 6, 7, 8, 9)]
infopage('pg043_sec001', 43, TH4, L44, 'Kujdes, këtu punohet!', paras(RULES43), figure('pg043_im002'))
written('pg043_sec002', 43, TH4, L44, 'Kujdes, këtu punohet!: puno në klasë', 'class', 'pg043_n0011', f'''
{task('pg043_n0013', p('pg043_n0014'))}
{how('adt_how_write')}
{lettered(43, range(15, 21))}''')
written('pg043_sec003', 43, TH4, L44, 'Kujdes, këtu punohet!: puno në shtëpi', 'home', 'pg043_n0022', f'''
{task('pg043_n0024', p('pg043_n0025'), p('pg043_n0026'))}
{reread(RULES43, 'pg043_n0025')}
{how('adt_how_write')}
{lettered(43, range(27, 33))}''')

# ====================== 44-45: lesson 5 ======================
L45 = 'pg005_n0017'
STORY44 = [n(44, 25, 26, 27)]
opener('pg044_sec001', 44, TH4, 'pg044_n0004', 'pg044_n0005', '5. Udhëtimi i çuditshëm i Ditës', 'pg044_im001',
       note2('pg044_n0008', n(44, 11, 13, 15, 17), 'pg044_n0019', n(44, 21, 22, 23)), STORY44)
think('pg044_sec002', 44, TH4, L45, 'Udhëtimi i çuditshëm i Ditës', STORY44, n(44, 30, 32))
infopage('pg045_sec001', 45, TH4, L45, 'Udhëtimi i çuditshëm i Ditës',
         paras([n(44, 35, 36), n(44, 37, 38, 39, 40), n(44, 41) + n(45, 4, 5, 6), n(45, 7)]),
         '<div class="bk-fields bk-fields--3">' + figure('pg045_im002') + figure('pg045_im003_crop_v1') + figure('pg045_im001') + '</div>')
written('pg045_sec002', 45, TH4, L45, 'Udhëtimi i çuditshëm i Ditës: puno në klasë', 'class', 'pg045_n0010', f'''
{task('pg045_n0012', p('pg045_n0013'))}
{how('adt_how_write')}
{lettered(45, range(14, 20))}''')
written('pg045_sec003', 45, TH4, L45, 'Udhëtimi i çuditshëm i Ditës: puno në shtëpi', 'home', 'pg045_n0021', f'''
{how('adt_how_write')}
{task('pg045_n0023', p('pg045_n0024'))}
{lettered(45, range(25, 28))}
{task('pg045_n0028', p('pg045_n0029'))}
{lettered(45, range(30, 33))}''')

# ====================== 46: Tematika 5, lesson 1 opener ======================
L51 = 'pg005_n0023'
EDIT['pg046_n0028'] = T['pg046_n0028'].lstrip('• ').strip()
STORY46 = [n(46, 20, 21)]
POLL = (f'<section class="bk-group" aria-labelledby="poll-h"><h2 id="poll-h" data-id="pg046_n0023">{esc(tx("pg046_n0023"))}</h2>'
        f'{figure("pg046_im005")}<ul class="bk-chips">' + ''.join(f'<li>{s(x)}</li>' for x in n(46, 24, 25, 26, 27)) + '</ul></section>')
opener('pg046_sec001', 46, TH5, 'pg046_n0005', 'pg046_n0006', '1. Njohim llojet e ndotjes dhe i parandalojmë ato', None,
       note('pg046_n0008', n(46, 11, 13, 15), 'pg046_n0016', 'pg046_n0017'), STORY46,
       extra='<div class="bk-fields bk-fields--2">' + ''.join(figure(f'pg046_im00{k}') for k in (1, 2, 3, 4)) + '</div>\n' + POLL)
think('pg046_sec002', 46, TH5, L51, 'Njohim llojet e ndotjes', None, ['pg046_n0028'], pre=POLL.replace('id="poll-h"', 'id="poll-h2"').replace('"poll-h"', '"poll-h2"'))
