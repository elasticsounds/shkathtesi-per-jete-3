"""Quiz pages (one multiple-choice question each), in the shared template."""
from lib import *

new('adt_quiz', 'Kuiz')
new('adt_how_quiz', 'Zgjidh një përgjigje. Pastaj shtyp butonin “Dërgo” për të parë nëse është e saktë.')

QUIZZES = [  # id, theme, lesson, correct option index, printed page
    ('qz001', 'pg006_n0002', 'pg004_n0007', 1, 7),
    ('qz002', 'pg030_n0002', 'pg004_n0037', 0, 31),
    ('qz003', 'pg036_n0002', 'pg005_n0011', 2, 41),
    ('qz004', 'pg048_n0002', 'pg005_n0029', 0, 53),
]
for qid, theme, lesson, ok, pg in QUIZZES:
    answers = {f'{qid}_o{k}': k == ok for k in range(3)}
    expl = {f'{qid}_o{k}': f'{qid}_o{k}_exp' for k in range(3)}
    opts = ''
    for k in range(3):
        o = f'{qid}_o{k}'
        opts += (f'<label class="activity-option bk-option bk-option--quiz" data-activity-item="{o}" '
                 f'data-explanation="{esc(tx(o + "_exp"))}" data-explanation-id="{o}_exp">'
                 f'<input type="radio" name="{qid}" value="{o}" data-activity-item="{o}" aria-labelledby="{o}-label">'
                 f'<span id="{o}-label" class="option-text" data-id="{o}">{esc(tx(o))}</span>'
                 f'<span class="validation-mark hidden"></span>'
                 f'<div class="hidden feedback-container" aria-live="polite"><span aria-hidden="true" class="feedback-icon"></span>'
                 f'<span class="feedback-text"></span></div></label>\n')
    aj, ej = json.dumps(answers), json.dumps(expl)
    page(qid, 'activity_quiz', 'Kuiz: ' + tx(qid + '_que'), f'''
{crumb(theme, lesson)}
{rubric('think', 'adt_quiz')}
<p id="{qid}-question" class="bk-question" data-id="{qid}_que">{esc(tx(qid + '_que'))}</p>
{how('adt_how_quiz')}
<div class="bk-options bk-options--list" role="radiogroup" aria-labelledby="{qid}-question">
{opts}</div>
<div data-submit-target=""></div>
<script type="application/json" id="quiz-correct-answers">{aj}</script>
<script type="application/json" id="quiz-explanations">{ej}</script>''',
         pg, attrs=f' data-id="{qid}" data-area-id="{qid}" data-correct-answers=\'{aj}\' data-option-explanations=\'{ej}\'',
         scripts=f"<script>window.correctAnswers = JSON.parse('{aj}');</script>")
