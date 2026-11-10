"""Pages 13-24: Tematika 1 lessons 3-4 and Tematika 2 lessons 1-3."""
import os
from lib import *
from pages_a import n, cat, TH1, L3

L4 = ('pg004_n0016',)
TH2 = 'pg018_n0002'
M1 = ('pg004_n0022',)
M2 = ('pg004_n0025',)
M3 = ('pg004_n0028',)

# ---------- 13: sort clothes by material ----------
new('pg013_ac001', 'Vendos veshjet prej leshi në kutinë “Prej leshi” dhe veshjet prej pambuku në kutinë “Prej pambuku”.')
new('pg013_ac007', 'Prej leshi')
new('pg013_ac008', 'Prej pambuku')
CL = [('pg013_im005', 'Triko e trashë, e thurur', 'lesh'), ('pg013_im003_a', 'Çorape të trasha, të thurura', 'lesh'),
      ('pg013_im003_b', 'Fund i hollë vere', 'pambuk'), ('pg013_im004_a', 'Bluzë e hollë me mëngë të shkurtra', 'pambuk'),
      ('pg013_im004_b', 'Shall i trashë, i thurur', 'lesh')]
KEY13, cards = {}, ''
for j, (im, label, c) in enumerate(CL, 1):
    i = new(f'pg013_ac{j + 1:03d}', label)
    KEY13[f'c{j}'] = c
    cards += f'<div class="word-card bk-card" data-activity-item="c{j}">{deco(f"images/{im}.png")}{s(i)}</div>\n'
page('pg013_sec001', 'activity_sorting', 'Dita dhe lulja e veçantë: puno në klasë', f'''
{crumb(TH1, *L3)}
{rubric('class', 'pg013_n0004')}
{task('pg013_n0006', p('pg013_ac001'))}
{how('adt_how_sort')}
<div class="bk-pool" role="group" aria-label="{esc(tx('adt_cards'))}">
{cards}</div>
<div class="bk-cats bk-cats--2">
{cat('lesh', 'pg013_ac007')}
{cat('pambuk', 'pg013_ac008')}
</div>
<p class="bk-task-body">{s('pg013_n0009')}</p>''', 13, attrs=f" data-correct-answers='{json.dumps(KEY13)}'", scripts=answers_script(KEY13))

new('pg013_ac010', 'Vendosi figurat sipas radhës së veprimeve, nga e para tek e fundit.')
ST = [('pg013_im007', 'Kreh leshin.', 3), ('pg013_im008', 'Ngjyros leshin në kazan.', 4), ('pg013_im009', 'Tjerr leshin dhe bën fije.', 5),
      ('pg013_im006', 'Thur trikon.', 6), ('pg013_im002', 'Qeth delen.', 1), ('pg013_im010', 'Lan leshin.', 2)]
KEY13b, items = {}, ''
for j, (im, label, rank) in enumerate(ST, 1):
    i = new(f'pg013_ac{j + 10:03d}', label)
    KEY13b[f's{j}'] = rank
    items += f'<li data-activity-item="s{j}">{deco(f"images/{im}.png")}{s(i)}</li>'
page('pg013_sec002', 'activity_ordering', 'Dita dhe lulja e veçantë: puno në shtëpi', f'''
{crumb(TH1, *L3)}
{rubric('home', 'pg013_n0014')}
{task('pg013_n0016', '<p class="bk-soft">' + s('pg013_n0017') + ' ' + s('pg013_n0018') + '</p>', p('pg013_ac010'))}
{how('adt_how_order')}
<ol class="bk-order bk-order--pics bk-order--big" data-activity-order-list>{items}</ol>''', 13, scripts=answers_script(KEY13b))

# ---------- 14: lesson 4 ----------
page('pg014_sec001', 'boxed_text', '4. Dita dhe Dielli i përshtaten stilit tuaj', f'''
{crumb(TH1)}
{lesson_title('pg014_n0004', 'pg014_n0005')}
{note('pg014_n0007', n(14, 10, 12), 'pg014_n0013', 'pg014_n0014')}
{story([n(14, 16, 17, 18, 19), n(14, 20, 21, 22)])}''', 14, role='article')

new('adt_dita', 'Dita')
new('adt_dielli', 'Dielli')
new('adt_any_ok', 'Zgjidh si të duash. Çdo zgjedhje është e mirë.')
new('pg014_ac001', 'Për secilën veshje, zgjidh kush do ta veshë: Dita apo Dielli.')

def pick(item, src, label_id, color=False):
    radios = ''.join(
        f'<label class="bk-radio"><input type="radio" name="{item}" value="{v}" data-activity-item="{item}">{s(t)}'
        f'<span class="validation-mark hidden"></span></label>' for v, t in (('dita', 'adt_dita'), ('dielli', 'adt_dielli')))
    col = ''
    if color:
        opts = ''.join(f'<option value="{hx}" data-id="{cid}">{esc(tx(cid))}</option>' for cid, hx in COLORS)
        col = (f'<label class="bk-label" for="col-{item}">{s("pg015_ac002")}<span class="bk-sr"> — {esc(tx(label_id))}</span></label>'
               f'<select id="col-{item}" data-color-for="img-{item}">{opts}</select>')
    return (f'<fieldset class="bk-pick"><legend><span class="bk-pick-img" id="img-{item}">{deco(src)}</span>{s(label_id)}</legend>'
            f'<div class="bk-radios">{radios}</div>{col}</fieldset>')

W14 = [('a', 'Xhaketë xhins'), ('b', 'Bluzë e kuqe'), ('c', 'Pantallona xhins'), ('d', 'Atlete të kaltra'),
       ('e', 'Fustan me vija'), ('f', 'Këpucë kafe'), ('g', 'Shall')]
picks = ''
for j, (c, label) in enumerate(W14, 1):
    picks += pick(f'w{j}', f'images/pg014_im001_{c}.png', new(f'pg014_ac{j + 1:03d}', label)) + '\n'
KIDS = (f'<div class="bk-kids"><figure>{img("pg014_im002")}<figcaption>{s("adt_dita")}</figcaption></figure>'
        f'<figure>{img("pg014_im003")}<figcaption>{s("adt_dielli")}</figcaption></figure></div>')
page('pg014_sec002', 'activity_true_false', 'Dita dhe Dielli i përshtaten stilit tuaj: vishi fëmijët', f'''
{crumb(TH1, *L4)}
{rubric('turn', 'pg015_n0003')}
<p>{s('pg014_n0024')} {s('pg014_n0025')}</p>
<p class="bk-task-body">{s('pg014_ac001')}</p>
{p('adt_any_ok')}
{KIDS}
<div class="bk-picks">
{picks}</div>''', 14, scripts=answers_script({}))

# ---------- 15 ----------
new('pg015_ac001', 'Për secilën veshje, zgjidh kush do ta veshë dhe me çfarë ngjyre do ta ngjyrosësh.')
new('pg015_ac002', 'Ngjyra')
COLORS = [(new(f'pg015_ac{k + 20:03d}', name), hx) for k, (name, hx) in enumerate([
    ('pa ngjyrë', ''), ('e kuqe', '#f87171'), ('e kaltër', '#7dd3fc'), ('e gjelbër', '#86efac'), ('e verdhë', '#fde047'),
    ('portokalli', '#fdba74'), ('rozë', '#f9a8d4'), ('vjollcë', '#c4b5fd'), ('kafe', '#c8a27a'), ('gri', '#cbd5e1')])]
W15 = [('a', 'Karfica flokësh'), ('b', 'Fjongo'), ('c', 'Pantallona të shkurtra'), ('d', 'Kapelë me strehë'), ('e', 'Jelek'),
       ('f', 'Fund'), ('g', 'Bluzë me mëngë të shkurtra'), ('h', 'Triko me vija'), ('i', 'Këmishë'), ('j', 'Çizme'),
       ('k', 'Pantallona të gjata'), ('l', 'Këpucë të sheshta'), ('m', 'Atlete')]
picks = ''
for j, (c, label) in enumerate(W15, 1):
    picks += pick(f'x{j}', f'images/pg015_im001_{c}.png', new(f'pg015_ac{j + 2:03d}', label), color=True) + '\n'
COLOR_JS = '''<script>
(function () {
  document.querySelectorAll('select[data-color-for]').forEach(function (sel) {
    var box = document.getElementById(sel.getAttribute('data-color-for'));
    var key = 'pg015_sec001_' + sel.id;
    try { var saved = localStorage.getItem(key); if (saved !== null) sel.value = saved; } catch (e) {}
    function paint() { if (box) box.style.backgroundColor = sel.value || '#ffffff'; }
    sel.addEventListener('change', function () { paint(); try { localStorage.setItem(key, sel.value); } catch (e) {} });
    paint();
  });
})();
</script>'''
page('pg015_sec001', 'activity_true_false', 'Dita dhe Dielli i përshtaten stilit tuaj: tani radhën e ke ti', f'''
{crumb(TH1, *L4)}
{rubric('turn', 'pg015_n0003')}
{task('pg015_n0004', p('pg015_n0005'), p('pg015_ac001'))}
{p('adt_any_ok')}
{figure('pg015_im001')}
<div class="bk-picks">
{picks}</div>''', 15, scripts=answers_script({}) + COLOR_JS)

groups = ''
for k in (19, 21, 23, 25, 27):
    h = f'pg015_n{k:04d}'
    a, b = uid('a'), uid('a')
    groups += (f'<section class="bk-group" aria-labelledby="g{k}"><h2 id="g{k}" data-id="{h}">{esc(tx(h))}</h2>'
               f'<div class="bk-fields bk-fields--2">'
               f'<div><label id="l{a}" for="{a}">{s("pg015_n0030")}</label><input type="text" id="{a}" data-aria-id="{a}" aria-labelledby="g{k} l{a}" autocomplete="off"></div>'
               f'<div><label id="l{b}" for="{b}">{s("pg015_n0038")}</label><input type="text" id="{b}" data-aria-id="{b}" aria-labelledby="g{k} l{b}" autocomplete="off"></div>'
               f'</div></section>\n')
page('pg015_sec002', 'activity_open_ended_answer', 'Dita dhe Dielli i përshtaten stilit tuaj: puno në klasë', f'''
{crumb(TH1, *L4)}
{rubric('class', 'pg015_n0009')}
{task('pg015_n0010', p('pg015_n0011', 'pg015_n0012'), p('pg015_n0013'), p('pg015_n0014'))}
{how('adt_how_write')}
{groups}
{reset()}''', 15)

# ---------- 16 ----------
new('pg016_ac001', 'Nëse nuk mund t’i ngjyrosësh, trego me fjalë çfarë ngjyre do t’i jepje secilës orendi.')
new('pg016_ac002', 'Orendia')
new('pg016_ac003', 'Materiali')
trs = f'<tr><td>{s("pg016_n0018")}</td><td>{s("pg016_n0020")}</td></tr>'
for r in range(2, 7):
    a, b = uid('a'), uid('a')
    trs += (f'<tr><td><input type="text" id="{a}" data-aria-id="{a}" aria-label="{esc(tx("pg016_ac002"))} {r}" autocomplete="off"></td>'
            f'<td><input type="text" id="{b}" data-aria-id="{b}" aria-label="{esc(tx("pg016_ac003"))} {r}" autocomplete="off"></td></tr>')
new('pg016_ac010', 'Për të ngjyrosur: zgjidh një ngjyrë, pastaj prek pjesën e figurës që do të ngjyrosësh. Me tastierë: shko te figura, lëvize shenjën me shigjetat dhe shtyp Enter për të ngjyrosur.')
new('pg016_ac011', 'Zgjidh ngjyrën')
new('pg016_ac012', 'Zhbëj')
new('pg016_ac013', 'Fshi ngjyrat')
new('pg016_ac014', 'Figura për ngjyrosje. Lëvize shenjën me shigjetat dhe shtyp Enter për të ngjyrosur.')
PAL = [(new(f'pg016_ac{k + 20:03d}', name), hx) for k, (name, hx) in enumerate([
    ('e kuqe', '#ef4444'), ('portokalli', '#fb923c'), ('e verdhë', '#facc15'), ('e gjelbër', '#4ade80'), ('e kaltër', '#38bdf8'),
    ('blu', '#3b6fd8'), ('vjollcë', '#a78bfa'), ('rozë', '#f472b6'), ('kafe', '#a9744f'), ('gri', '#9ca3af'), ('e bardhë', '#ffffff')])]
swatches = ''.join(
    f'<label class="bk-swatch"><input type="radio" name="paint" value="{hx}"{" checked" if k == 0 else ""}>'
    f'<span class="bk-swatch-dot" style="background:{hx}" aria-hidden="true"></span>{s(cid)}</label>' for k, (cid, hx) in enumerate(PAL))
COLORING = f'''<div class="bk-paint" id="paint">
<fieldset class="bk-paint-palette"><legend>{s('pg016_ac011')}</legend>{swatches}</fieldset>
<div class="bk-paint-stage"><canvas id="paint-canvas" tabindex="0" role="application" aria-label="{esc(tx('pg016_ac014'))}" aria-describedby="paint-alt"></canvas>
<span class="bk-paint-cursor" id="paint-cursor" aria-hidden="true"></span></div>
<p id="paint-alt" class="bk-sr" data-id="pg016_im001">{esc(tx('pg016_im001'))}</p>
<p class="bk-paint-tools"><button type="button" class="bk-reset" id="paint-undo">{s('pg016_ac012')}</button>
<button type="button" class="bk-reset" id="paint-clear">{s('pg016_ac013')}</button></p>
<p class="bk-sr" id="paint-status" role="status" aria-live="polite"></p>
</div>'''
PAINT_JS = '<script>\n(function () {\n  var SRC = "' + open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'color_img.txt')).read() + '";\n' + open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paint.js')).read() + '\n})();\n</script>'
page('pg016_sec001', 'activity_fill_in_a_table', 'Dita dhe Dielli i përshtaten stilit tuaj: puno në shtëpi', f'''
{crumb(TH1, *L4)}
{rubric('home', 'pg016_n0004')}
{task('pg016_n0006', p('pg016_n0007'), p('pg016_n0008', 'pg016_n0009'))}
{how('pg016_ac010')}
{how('pg016_ac001')}
{COLORING}
{how('adt_how_write')}
<table class="bk-table">
<thead><tr><th scope="col">{s('pg016_n0013')}</th><th scope="col">{s('pg016_n0015')}</th></tr></thead>
<tbody>{trs}</tbody>
</table>
{reset()}''', 16, scripts=answers_script({}) + PAINT_JS)

# ---------- 17 ----------
STORY17 = [n(17, 21), n(17, 22), n(17, 23, 24, 25), n(17, 26, 27, 28, 29), n(17, 30)]
page('pg017_sec001', 'text_and_single_image', '1. Dita e Dielli bisedojnë për profesionet', f'''
{crumb(TH2)}
{lesson_title('pg017_n0005', 'pg017_n0004')}
<div class="bk-opener bk-opener--split">
{figure('pg017_im001')}
{note('pg017_n0008', n(17, 11, 13, 15), 'pg017_n0017', 'pg017_n0019')}
</div>
{story(STORY17)}''', 17, role='article')

page('pg017_sec002', 'activity_open_ended_answer', 'Dita e Dielli bisedojnë për profesionet: mendo dhe përgjigju', f'''
{crumb(TH2, *M1)}
{rubric('think', 'adt_think')}
{reread(STORY17)}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg017_n0039'])}
{question(['pg017_n0040'])}
</div>
{reset()}''', 17)

# ---------- 18 ----------
page('pg018_sec001', 'boxed_text', 'Dita e Dielli bisedojnë për profesionet: lexo dhe mëso', f'''
{crumb(TH2, *M1)}
{rubric('learn', 'adt_learn')}
{info(paras([n(17, 33, 34), n(17, 35), n(17, 36), n(18, 5)]))}''', 18, role='article')

new('pg018_ac001', 'Vendos emrin e profesionit poshtë figurës së duhur.')
def match_page(sid, title, people, base, first):
    key, chips, zones = {}, '', ''
    order = [2, 4, 0, 3, 1]  # chips are shown in a different order from the pictures
    for j, (c, name, alt) in enumerate(people):
        new(f'{base}_{c}', alt)
        key[f'p{c}'] = f'z{c}'
        zones += f'<div class="dropzone bk-zone">{img(f"{base}_{c}")}<div class="dropzone-slot bk-slot" id="z{c}"></div></div>\n'
    for j in order:
        c, name, alt = people[j]
        i = new(f'pg018_ac{first + j:03d}', name)
        chips += f'<div class="activity-item bk-chip" data-activity-item="p{c}">{s(i)}</div>\n'
    page(sid, 'activity_matching', title, f'''
{crumb(TH2, *M1)}
{rubric('class', 'pg018_n0009')}
{task('pg018_n0011', p('pg018_n0012'), p('pg018_ac001'))}
{how('adt_how_match')}
<div class="bk-pool" role="group" aria-label="{esc(tx('adt_cards'))}">
{chips}</div>
<div class="bk-zones">
{zones}</div>''', 18, attrs=f" data-correct-answers='{json.dumps(key)}'", scripts=answers_script(key))

match_page('pg018_sec002', 'Dita e Dielli bisedojnë për profesionet: emërto profesionet (1)', [
    ('a', 'menaxher', 'Burrë me kostum dhe kravatë, me një çantë pune në dorë.'),
    ('b', 'ndërtues', 'Punëtor me helmetë të verdhë mbrojtëse, që mban një plan pune.'),
    ('c', 'kuzhiniere', 'Grua me kapelë të bardhë kuzhine dhe përparëse, që mban një tabaka me ushqim.'),
    ('d', 'mësues', 'Burrë me syze, që mban një shkop tregues dhe një glob.'),
    ('e', 'infermiere', 'Grua me uniformë të bardhë, me kapelë me kryq të kuq dhe një shiringë në dorë.')], 'pg018_im002', 2)
match_page('pg018_sec003', 'Dita e Dielli bisedojnë për profesionet: emërto profesionet (2)', [
    ('a', 'polic', 'Burrë me këmishë të kaltër, kravatë dhe kapelë me stemë.'),
    ('b', 'pilot', 'Burrë me uniformë blu të errët me kopsa të arta dhe kapelë me strehë.'),
    ('c', 'zjarrfikës', 'Burrë me uniformë portokalli me shirita të verdhë dhe helmetë të kuqe.'),
    ('d', 'pastrues', 'Punëtor me kominoshe të kaltra dhe kapelë, që mban një shishe me spërkatës dhe një leckë.'),
    ('e', 'piktore', 'Grua me përparëse, që mban një penel dhe një paletë me ngjyra.')], 'pg018_im003', 7)

page('pg018_sec004', 'activity_open_ended_answer', 'Dita e Dielli bisedojnë për profesionet: fol për profesionet', f'''
{crumb(TH2, *M1)}
{rubric('class', 'pg018_n0009')}
{figure('pg018_im002')}
{figure('pg018_im003')}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg018_n0013'])}
{question(['pg018_n0014'])}
</div>
{reset()}''', 18)

page('pg018_sec005', 'text_and_single_image', 'Dita e Dielli bisedojnë për profesionet: puno në shtëpi', f'''
{crumb(TH2, *M1)}
{rubric('home', 'pg018_n0017')}
{task('pg018_n0019', p('pg018_n0020'), '<p class="bk-soft">' + s('pg018_n0021') + ' ' + s('pg018_n0022') + '</p>')}
{how('adt_help_craft')}
{figure('pg018_im004')}''', 18, role='article')

# ---------- 19 ----------
STORY19 = [n(19, 19, 20, 21, 22, 23, 24)]
page('pg019_sec001', 'text_and_single_image', '2. Nëna e Ditës është mjeke', f'''
{crumb(TH2)}
{lesson_title('pg019_n0003', 'pg019_n0004')}
<div class="bk-opener bk-opener--split">
{figure('pg019_im001')}
{note('pg019_n0007', n(19, 10, 12, 14), 'pg019_n0016', 'pg019_n0017')}
</div>
{story(STORY19)}''', 19, role='article')

page('pg019_sec002', 'activity_open_ended_answer', 'Nëna e Ditës është mjeke: mendo dhe përgjigju', f'''
{crumb(TH2, *M2)}
{rubric('think', 'adt_think')}
{reread(STORY19)}
{how('adt_how_write')}
<div class="bk-panel">
{''.join(question([f'pg019_n{k:04d}']) for k in (28, 30, 32, 34, 36))}
</div>
{reset()}''', 19)

# ---------- 20 ----------
page('pg020_sec001', 'boxed_text', 'Nëna e Ditës është mjeke: lexo dhe mëso', f'''
{crumb(TH2, *M2)}
{rubric('learn', 'adt_learn')}
{info(paras([n(20, 4), n(20, 5, 6), n(20, 8, 9, 10), n(20, 12)]))}''', 20, role='article')

new('pg020_ac001', 'Shkruaj emrin e profesionit për secilën figurë. Shkronjat shfaqen edhe në fjalëkryq.')
new('pg020_ac002', 'vertikalisht')
new('pg020_ac003', 'horizontalisht')
new('pg020_ac004', 'shkronja')
new('pg020_ac005', 'Fjala')
CW = [  # number, image, new description (must not name the profession), answer, direction, col, row
    (1, 'pg020_im003', 'Burrë që këndon me mikrofon në dorë.', 'këngëtar', 'v', 1, 1),
    (2, 'pg020_im004', 'Vajzë me fustan rozë, që kërcen në majë të gishtave.', 'balerinë', 'v', 6, 1),
    (3, 'pg020_im005', 'Djalë me veshje sportive, që vrapon.', 'sportist', 'v', 9, 3),
    (4, 'pg020_im008', 'Burrë me mantel të bardhë dhe stetoskop në qafë.', 'mjek', 'h', 4, 4),
    (5, 'pg020_im002', 'Grua me mantel të bardhë, që kontrollon një qen.', 'veteriner', 'v', 3, 5),
    (6, 'pg020_im006', 'Njeri me kostum të bardhë hapësinor dhe helmetë.', 'astronaut', 'h', 1, 7),
    (7, 'pg020_im007', 'Burrë me uniformë të kaltër dhe kapelë me stemë.', 'polic', 'h', 0, 10)]
KEY20, clues, cells, words = {}, '', {}, {}
for num, im, alt, ans, d, c, r in CW:
    did = new(f'{im}_d', alt)
    plain = ans.replace('ë', 'e')
    KEY20[f'item-{num}'] = ans if plain == ans else f'{ans}|{plain}'
    dirid = 'pg020_ac002' if d == 'v' else 'pg020_ac003'
    fid = f'cw{num}'
    clues += (f'<li><img data-id="{did}" src="images/{im}.png" alt="{esc(alt)}">'
              f'<div><label for="{fid}">{s("pg020_ac005")} {num} <span class="bk-hint">({s(dirid)}, {len(ans)} {s("pg020_ac004")})</span></label>'
              f'<input type="text" id="{fid}" data-aria-id="{fid}" data-activity-item="item-{num}" maxlength="{len(ans)}" '
              f'autocomplete="off" autocapitalize="none" spellcheck="false" data-cw="{num}"></div></li>\n')
    words[num] = []
    for k in range(len(ans)):
        cc, rr = (c, r + k) if d == 'v' else (c + k, r)
        words[num].append(f'{cc}-{rr}')
        cells.setdefault((cc, rr), None)
        if k == 0: cells[(cc, rr)] = num
grid = ''.join(f'<span id="cwc-{c}-{r}" style="grid-column:{c + 1};grid-row:{r}">{"<i>%d</i>" % v if v else ""}<b></b></span>'
               for (c, r), v in sorted(cells.items(), key=lambda kv: (kv[0][1], kv[0][0])))
CW_JS = '''<script>
(function () {
  var WORDS = %s;
  var inputs = document.querySelectorAll('input[data-cw]');
  function paint() {
    var letters = {};
    inputs.forEach(function (inp) {
      var cells = WORDS[inp.getAttribute('data-cw')] || [];
      Array.from(inp.value.trim()).forEach(function (ch, k) { if (cells[k] && !letters[cells[k]]) letters[cells[k]] = ch; });
    });
    document.querySelectorAll('#cw-grid > span').forEach(function (cell) {
      var b = cell.querySelector('b'); if (b) b.textContent = letters[cell.id.slice(4)] || '';
    });
  }
  inputs.forEach(function (inp) { inp.addEventListener('input', paint); });
  setTimeout(paint, 400);
})();
</script>''' % json.dumps({str(k): v for k, v in words.items()})
page('pg020_sec002', 'activity_fill_in_the_blank', 'Nëna e Ditës është mjeke: puno në klasë', f'''
{crumb(TH2, *M2)}
{rubric('class', 'pg020_n0014')}
{task('pg020_n0016', p('pg020_ac001'))}
{how('adt_how_write')}
<div class="bk-cwlayout">
<ol class="bk-clues bk-clues--big">
{clues}</ol>
<div class="bk-cwside"><div class="bk-cw" id="cw-grid" aria-hidden="true">{grid}</div></div>
</div>
{reset()}''', 20, scripts=answers_script(KEY20) + CW_JS)

# ---------- 21: person <-> workplace ----------
new('pg021_ac001', 'Lidh secilin person me vendin ku punon.')
PEOPLE = [('m', 'pg021_im008', 'Mjeku', 'spital'), ('n', 'pg021_im010', 'Punëtori i ndërtimit', 'kantier'),
          ('p', 'pg021_im004', 'Polici', 'polici'), ('k', 'pg021_im009', 'Mekaniku', 'garazh'), ('a', 'pg021_im007', 'Piktori', 'atelie')]
PLACES = [('garazh', 'pg021_im011', 'Autogarazhi'), ('spital', 'pg021_im006', 'Spitali'), ('polici', 'pg021_im003', 'Stacioni i policisë'),
          ('atelie', 'pg021_im005', 'Atelieja e pikturës'), ('kantier', 'pg021_im012', 'Kantieri i ndërtimit')]
KEY21, chips, zones = {}, '', ''
for j, (c, im, name, place) in enumerate(PEOPLE, 1):
    i = new(f'pg021_ac{j + 1:03d}', name)
    KEY21[f'q{c}'] = f'z-{place}'
    chips += f'<div class="activity-item bk-chip" data-activity-item="q{c}">{deco(f"images/{im}.png")}{s(i)}</div>\n'
for j, (pid, im, name) in enumerate(PLACES, 1):
    i = new(f'pg021_ac{j + 6:03d}', name)
    zones += (f'<div class="dropzone bk-zone">{deco(f"images/{im}.png")}<span class="bk-zone-name" data-id="{i}">{esc(name)}</span>'
              f'<div class="dropzone-slot bk-slot" id="z-{pid}"></div></div>\n')
page('pg021_sec001', 'activity_matching', 'Nëna e Ditës është mjeke: puno në shtëpi', f'''
{crumb(TH2, *M2)}
{rubric('home', 'pg021_n0004')}
{task('pg021_n0006', p('pg021_ac001'))}
{how('adt_how_match')}
<div class="bk-pool" role="group" aria-label="{esc(tx('adt_cards'))}">
{chips}</div>
<div class="bk-zones">
{zones}</div>
<p class="bk-task-body">{s('pg021_n0008')}</p>''', 21, attrs=f" data-correct-answers='{json.dumps(KEY21)}'", scripts=answers_script(KEY21))

# ---------- 22 ----------
STORY22 = [n(22, 20), n(22, 21, 22, 23, 24, 25, 26, 27, 28)]
page('pg022_sec001', 'text_and_single_image', '3. Kur të rritem do të bëhem', f'''
{crumb(TH2)}
{lesson_title('pg022_n0004', 'pg022_n0005')}
<div class="bk-opener bk-opener--split">
{figure('pg022_im001')}
{note('pg022_n0008', n(22, 11, 13, 15), 'pg022_n0017', 'pg022_n0018')}
</div>
{story(STORY22)}''', 22, role='article')

page('pg022_sec002', 'activity_open_ended_answer', 'Kur të rritem do të bëhem: mendo dhe përgjigju', f'''
{crumb(TH2, *M3)}
{rubric('think', 'adt_think')}
{reread(STORY22)}
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg022_n0031'])}
{question(['pg022_n0033'])}
</div>
{reset()}''', 22)

page('pg022_sec003', 'boxed_text', 'Kur të rritem do të bëhem: lexo dhe mëso', f'''
{crumb(TH2, *M3)}
{rubric('learn', 'adt_learn')}
{info(paras([n(22, 37, 38, 39, 40, 41), n(22, 43, 44, 45, 46)]))}''', 22, role='article')

# ---------- 23 ----------
new('pg023_ac001', 'Për shkathtësinë time')
new('pg023_ac002', 'Për shkathtësitë që thanë shokët')
new('pg023_ac003', 'Shkathtësia e parë')
new('pg023_ac004', 'Shkathtësia e dytë')
def field(label_id, group_id=None, hint_id=None):
    i = uid('a')
    hint = f'<span class="bk-hint" data-id="{hint_id}">{esc(tx(hint_id))}</span>' if hint_id else ''
    lb = f' aria-labelledby="{group_id} l{i}"' if group_id else ''
    return (f'<div><label id="l{i}" for="{i}">{s(label_id)}{hint}</label>'
            f'<input type="text" id="{i}" data-aria-id="{i}"{lb} autocomplete="off"></div>')
page('pg023_sec001', 'activity_open_ended_answer', 'Kur të rritem do të bëhem: tani radhën e ke ti', f'''
{crumb(TH2, *M3)}
{rubric('turn', 'pg023_n0003')}
<ol class="bk-steps">
<li>{s('pg023_n0006')} {s('pg023_n0007')}</li>
<li>{s('pg023_n0008')}</li>
<li>{s('pg023_n0009')}</li>
<li>{s('pg023_n0010')}</li>
<li>{s('pg023_n0011')} {s('pg023_n0012')}</li>
</ol>
{how('adt_how_write')}
<div class="bk-panel">
{question(['pg023_n0017'], kind='input', hint_id='pg023_n0024')}
</div>
<section class="bk-group" aria-labelledby="g2"><h2 id="g2" data-id="pg023_n0019">{esc(tx('pg023_n0019'))}</h2>
<div class="bk-fields bk-fields--2">{field('pg023_ac003', 'g2')}{field('pg023_ac004', 'g2')}</div></section>
<section class="bk-group" aria-labelledby="g3"><h2 id="g3" data-id="pg023_n0022">{esc(tx('pg023_n0022'))}</h2>
<div class="bk-fields bk-fields--2">{field('pg023_ac001', 'g3', 'pg023_n0029')}{field('pg023_ac002', 'g3')}</div></section>
<div class="bk-panel">
{question(n(23, 31, 32, 33), rows=4)}
</div>
{reset()}''', 23)

# ---------- 24 ----------
new('adt_prof1', 'Profesioni i parë')
new('adt_prof2', 'Profesioni i dytë')
new('adt_prof3', 'Profesioni i tretë')
def child(gid, name_id, about):
    return (f'<section class="bk-group" aria-labelledby="{gid}"><h2 id="{gid}" data-id="{name_id}">{esc(tx(name_id))}</h2>'
            f'{p(*about)}<div class="bk-fields bk-fields--3">'
            + ''.join(field(x, gid) for x in ('adt_prof1', 'adt_prof2', 'adt_prof3')) + '</div></section>')
page('pg024_sec001', 'activity_open_ended_answer', 'Kur të rritem do të bëhem: puno në klasë', f'''
{crumb(TH2, *M3)}
{rubric('class', 'pg024_n0004')}
{task('pg024_n0006', '<p class="bk-soft">' + s('pg024_n0008') + ' ' + s('pg024_n0009') + '</p>', p('pg024_n0015'))}
{figure('pg024_im002')}
{how('adt_how_write')}
{child('k1', 'pg024_n0017', n(24, 10, 11))}
{child('k2', 'pg024_n0018', n(24, 12))}
{child('k3', 'pg024_n0019', n(24, 13, 14))}
{reset()}''', 24)

def pair(gid, label_id):
    return (f'<section class="bk-group" aria-labelledby="{gid}"><h2 id="{gid}" data-id="{label_id}">{esc(tx(label_id))}</h2>'
            f'<div class="bk-fields bk-fields--2">{field("adt_prof1", gid)}{field("adt_prof2", gid)}</div></section>')
page('pg024_sec002', 'activity_open_ended_answer', 'Kur të rritem do të bëhem: puno në shtëpi', f'''
{crumb(TH2, *M3)}
{rubric('home', 'pg024_n0021')}
{task('pg024_n0023', p('pg024_n0024'))}
{figure('pg024_im003')}
{how('adt_how_write')}
{pair('h1', 'pg024_n0026')}
{pair('h2', 'pg024_n0027')}
{reset()}''', 24)
