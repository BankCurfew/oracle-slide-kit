"""T3503 cinematic sample (designer direction 21acc9bd) · fe · PREVIEW ONLY.
Called by build.py when CINE_SAMPLE=1: takes the built T5 slides, keeps the sample's 4 (cover, s3 concept, the s5/s6
compare pair = one scene), adds the cine kit markup (data-cam / data-depth / data-fly / data-sweep / data-keep /
data-exit / data-enter), and returns them. Text is not touched; the full T5 build is not changed by this file.
"""
import re

def _one(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)

def transform(slides):
    cover, concept, cmp_a, cmp_b = slides[0], slides[2], slides[4], slides[5]
    # 1 · cover: camera push 1.06 / 8 s once (E1), dot layer at 0.4x, fixed vignette, the title flies + gets the sweep
    cover = _one(cover, '<section class="slide img cover" data-bg="cover">',
                 '<section class="slide img cover" data-bg="cover" data-cam="push:1.06:8000">\n'
                 '  <div class="cine-layer cine-dots" data-depth="0.4" aria-hidden="true"></div><div class="cine-layer cine-vig" aria-hidden="true"></div>')
    cover = _one(cover, '<span class="aurora">Need Approach</span>', '<span class="aurora" data-fly="title" data-sweep="900">Need Approach</span>')
    # 2 · s3: receives the title as its kick; TEXT block pans -24 px while the line draws through the 3 pills (E2)
    concept = _one(concept, '<section class="slide dots ans">', '<section class="slide ans" data-cam="pan:y:-24:1600:500">\n'
                   '  <div class="cine-layer cine-dots" data-depth="0.4" aria-hidden="true"></div>\n  <div class="cine-cam">')
    concept = _one(concept, '<div class="kick rv">Need Approach</div>', '<div class="kick rv" data-fly="title">Need Approach</div>')
    concept = _one(concept, '<ul class="flow">', '<ul class="flow cine-flow"><li class="cine-line" aria-hidden="true"></li>')
    concept = re.sub(r'\n</section>$', '\n  </div>\n</section>', concept.rstrip())
    # 3 · s5 -> s6: the h2 stays put, rows 1-3 leave, rows 4-5 arrive, then the verdict gets the sweep
    cmp_a = _one(cmp_a, '<h2 class="rv">Product vs Need Approach</h2>', '<h2 class="rv" data-keep="cmp">Product vs Need Approach</h2>')
    cmp_a = _one(cmp_a, '<table class="tb cmp rv">', '<table class="tb cmp rv" data-exit>')
    cmp_a = _one(cmp_a, '<div class="rcards cmp"', '<div data-exit class="rcards cmp"')
    cmp_b = _one(cmp_b, '<h2 class="rv">Product vs Need Approach</h2>', '<h2 class="rv" data-keep="cmp">Product vs Need Approach</h2>')
    cmp_b = _one(cmp_b, '<table class="tb cmp rv">', '<table class="tb cmp rv" data-enter>')
    cmp_b = _one(cmp_b, '<div class="rcards cmp"', '<div data-enter class="rcards cmp"')
    cmp_b = _one(cmp_b, '<div class="foot rv center">', '<div class="foot rv center" data-sweep="700">')
    return [cover, concept, cmp_a, cmp_b]
