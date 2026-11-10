"""Shared helpers for rebuilding ADT pages with the accessible `bk-` template."""
import html, json, re

I18N = 'content/i18n/sq/'
T = json.load(open(I18N + 'texts.json'))
NEW = {}       # new text ids -> string (added to texts.json and speech_texts.json)
EDIT = {}      # existing ids whose display text changes (audio wording unchanged)
PAGES = {}     # section_id -> dict(html=..., title=..., family=..., page=...)

def esc(s):
    return html.escape(s, quote=True)

def tx(i):
    if i in NEW: return NEW[i]
    if i in EDIT: return EDIT[i]
    return T[i]

def new(i, text):
    NEW[i] = text
    return i

def s(i, cls=None):
    c = f' class="{cls}"' if cls else ''
    return f'<span{c} data-id="{i}">{esc(tx(i))}</span>'

def p(*ids, cls=None):
    c = f' class="{cls}"' if cls else ''
    return f'<p{c}>' + ' '.join(s(i) for i in ids) + '</p>'

def paras(groups, cls=None):
    return '\n'.join(p(*g, cls=cls) for g in groups)

def img(i, src=None, cls=None, alt=None):
    """Image whose description lives in texts.json under its data-id."""
    src = src or f'images/{i}.png'
    c = f' class="{cls}"' if cls else ''
    a = tx(i) if alt is None else alt
    return f'<img{c} data-id="{i}" src="{src}" alt="{esc(a)}">'

def deco(src, cls=None):
    """Decorative image: the meaning is carried by adjacent text."""
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="{src}" alt="">'

def figure(i, caption_id=None, src=None):
    cap = f'<figcaption data-id="{caption_id}">{esc(tx(caption_id))}</figcaption>' if caption_id else ''
    return f'<figure class="bk-figure">{img(i, src)}{cap}</figure>'

def crumb(*ids):
    # No data-id on purpose: read-aloud plays every element in the page that has one,
    # and the theme/lesson line would otherwise be spoken again on every page.
    return '<p class="bk-crumb">' + ''.join(f'<span>{esc(tx(i))}</span>' for i in ids) + '</p>'

def rubric(kind, i):
    return f'<h1 class="bk-rubric bk-rubric--{kind}" data-id="{i}">{esc(tx(i))}</h1>'

def lesson_title(num_id, title_id):
    return (f'<h1 class="bk-lesson-title"><span class="bk-lesson-num" data-id="{num_id}">{esc(tx(num_id))}</span>'
            f'<span data-id="{title_id}">{esc(tx(title_id))}</span></h1>')

def note(learn_h, learn_ids, kw_h, kw_id):
    lis = ''.join(f'<li>{s(i)}</li>' for i in learn_ids)
    return (f'<aside class="bk-note" aria-labelledby="note-h"><h2 id="note-h" data-id="{learn_h}">{esc(tx(learn_h))}</h2>'
            f'<ul>{lis}</ul><h2 data-id="{kw_h}">{esc(tx(kw_h))}</h2>{p(kw_id)}</aside>')

def story(groups):
    return f'<div class="bk-story">{paras(groups)}</div>'

def info(*blocks):
    return '<div class="bk-info">' + '\n'.join(blocks) + '</div>'

def task(num_id, *blocks):
    return (f'<div class="bk-task"><span class="bk-task-num" data-id="{num_id}">{esc(tx(num_id))}</span>'
            f'<div class="bk-task-body">' + '\n'.join(blocks) + '</div></div>')

def how(i):
    return f'<p class="bk-how">{s(i)}</p>'

def reread(groups, label='adt_reread'):
    return f'<details class="bk-reread"><summary>{s(label)}</summary><div>{paras(groups)}</div></details>'

def reset():
    return f'<p><button type="button" class="bk-reset" data-adt-reset-responses>{s("adt_reset")}</button></p>'

_n = [0]
def uid(prefix='f'):
    _n[0] += 1
    return f'{prefix}{_n[0]}'

def question(label_ids, rows=3, hint_id=None, kind='textarea', item=None, extra_label=''):
    """Labelled written answer. label_ids: text ids that make up the visible label."""
    i = uid('a')
    lab = ' '.join(s(x) for x in label_ids)
    hint = f'<span class="bk-hint" data-id="{hint_id}">{esc(tx(hint_id))}</span>' if hint_id else ''
    it = f' data-activity-item="{item}"' if item else ''
    if kind == 'textarea':
        field = f'<textarea id="{i}" data-aria-id="{i}" rows="{rows}"{it}></textarea>'
    else:
        field = f'<input type="text" id="{i}" data-aria-id="{i}" autocomplete="off"{it}>'
    return f'<div class="bk-q"><label for="{i}">{extra_label}{lab}{hint}</label>{field}</div>'

def answers_script(d):
    return '<script>window.correctAnswers = ' + json.dumps(d, ensure_ascii=False) + ';</script>'

def page(sid, family, title, body, page_no=None, role=None, attrs='', scripts=''):
    """Register a page. body = inner HTML of the section."""
    r = f' role="{role}"' if role else ''
    # Gather every instruction note into one collapsible help block placed right after the page heading.
    notes = re.findall(r'<p class="bk-how">(.*?)</p>', body, flags=re.S)
    if notes:
        body = re.sub(r'<p class="bk-how">.*?</p>\n?', '', body, flags=re.S)
        helpbox = ('<details class="bk-help"><summary><span class="bk-help-icon" aria-hidden="true">?</span>'
                   + s('adt_help') + '</summary><div class="bk-help-body">'
                   + ''.join(f'<p>{x}</p>' for x in notes) + '</div></details>')
        body = body.replace('</h1>', '</h1>\n' + helpbox, 1)
    sec = (f'<section{r} data-section-type="{family}" data-section-id="{sid}" class="bk"{attrs}>\n{body}\n</section>')
    PAGES[sid] = dict(section=sec, title=title, family=family, page=page_no, scripts=scripts)
    _n[0] = 0

def new_page_counter():
    _n[0] = 0

SHELL = '''<!DOCTYPE html>
<html lang="sq"><head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <meta name="title-id" content="{sid}">
    <!-- 1-based position of this page in content/pages.json (drives the "N of M" counter). -->
    <meta name="page-section-id" content="{pos}">
    <link href="./content/tailwind_output.css" rel="stylesheet">
    <link href="./assets/libs/fontawesome/css/all.min.css" rel="stylesheet">
    <link href="./assets/fonts.css" rel="stylesheet">
    <link href="./content/book.css" rel="stylesheet">
    </head>

<body class="min-h-screen spj-book" data-book-theme="spj-2026" data-page-family="{family}" data-adaptation="a11y-1">
    <main class="w-full" style="width:100%;min-width:0">
      <div id="content" class="opacity-0">
{section}
      </div>
    </main>
{scripts}
    <div class="relative z-50" id="interface-container"></div>
    <div class="relative z-50" id="nav-container"></div>
    <script src="./assets/offline-preloader.js"></script>
    <script src="./assets/scorm.js"></script>
    <script src="./assets/base.bundle.local.js"></script>
</body></html>
'''

def render(sid, pos):
    pg = PAGES[sid]
    return SHELL.format(title=esc(pg['title'] + ' — Shkathtësi për jetë 3'), sid=sid, pos=pos,
                        family=pg['family'], section=pg['section'], scripts=pg['scripts'])
