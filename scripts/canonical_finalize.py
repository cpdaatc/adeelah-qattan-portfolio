from pathlib import Path
import re

VERSION = "canonical-20260814"
PORTRAIT = f"assets/Dr_Adeelah_Qattan_Portrait_High_Resolution.jpg?v={VERSION}"
CERT = f"assets/King_Fahd_Medal_Certificate_2019.jpg?v={VERSION}"
CV = f"assets/Dr_Adeelah_Qattan_CV_2026.pdf?v={VERSION}"
BIO = f"assets/Dr_Adeelah_Qattan_Speaker_Bio_Bilingual.pdf?v={VERSION}"

p = Path("index.html")
t = p.read_text(encoding="utf-8")

# Correct hero portrait source. The screen may crop it into the circular visual,
# but the downloadable file itself is the standalone original JPEG.
t, n = re.subn(
    r'(<div class="portrait-frame">\s*<img\s+src=")[^"]+("[^>]*>)',
    rf'\1{PORTRAIT}\2',
    t,
    count=1,
    flags=re.S,
)
assert n == 1, "Hero portrait element not found exactly once"

# User requested no print button in the hero. Keep only the Royal Honour jump.
hero_actions = (
    '<div class="hero-actions">'
    '<a class="btn btn-primary" href="#royal">'
    '<span class="action-icon" aria-hidden="true">🏅</span>'
    '<span class="en">View Royal Honour</span>'
    '<span class="ar">عرض التكريم الملكي</span>'
    '</a></div>'
)
t, n = re.subn(r'<div class="hero-actions">.*?</div>', hero_actions, t, count=1, flags=re.S)
assert n == 1, "Hero actions block not found exactly once"

# Exactly five compact actions in the mobile side menu.
side_actions = (
    '<div class="sidebar-downloads">'
    '<a class="btn btn-primary resource-download" href="#royal">'
    '<span class="action-icon" aria-hidden="true">🏅</span>'
    '<span class="en">View Royal Honour</span><span class="ar">عرض التكريم الملكي</span></a>'
    f'<a class="btn btn-primary resource-download" href="{PORTRAIT}" download="Dr_Adeelah_Qattan_Portrait_High_Resolution.jpg">'
    '<span class="action-icon" aria-hidden="true">🖼️</span>'
    '<span class="en">Download Personal Photo</span><span class="ar">تحميل الصورة الشخصية</span></a>'
    f'<a class="btn btn-primary resource-download" href="{BIO}" download>'
    '<span class="action-icon" aria-hidden="true">📄</span>'
    '<span class="en">Download Speaker Bio (PDF)</span><span class="ar">تحميل النبذة التعريفية (PDF)</span></a>'
    f'<a class="btn btn-primary resource-download" href="{CV}" download>'
    '<span class="action-icon" aria-hidden="true">📘</span>'
    '<span class="en">Download CV (PDF)</span><span class="ar">تحميل السيرة الذاتية (PDF)</span></a>'
    '<button class="btn btn-primary resource-download" type="button" onclick="window.print()">'
    '<span class="action-icon" aria-hidden="true">🖨️</span>'
    '<span class="en">Print / Save CV</span><span class="ar">طباعة / حفظ السيرة</span></button>'
    '</div>'
)
t, n = re.subn(r'<div class="sidebar-downloads">.*?</div>', side_actions, t, count=1, flags=re.S)
assert n == 1, "Sidebar actions block not found exactly once"

# The complete royal certificate is display-only: no link, click, or download.
royal_start = t.index('<section class="royal" id="royal">')
royal_end = t.index('</section>', royal_start) + len('</section>')
royal = t[royal_start:royal_end]
figure = (
    '<figure class="royal-document" aria-label="King Fahd Medal certificate 2019">'
    f'<img src="{CERT}" alt="King Fahd Medal — Third Degree certificate, 2019">'
    '<figcaption>'
    '<strong class="en">King Fahd Medal — Third Degree · 2019</strong>'
    '<strong class="ar">ميدالية الملك فهد — الدرجة الثالثة · 2019</strong>'
    '</figcaption></figure>'
)
royal, n = re.subn(r'<figure class="royal-document".*?</figure>', figure, royal, count=1, flags=re.S)
assert n == 1, "Royal certificate figure not found exactly once"
assert '<a ' not in royal and 'download=' not in royal and 'onclick=' not in royal

t = t[:royal_start] + royal + t[royal_end:]

# Remove any previous canonical block before adding one deterministic override.
t = re.sub(
    r'/\* CANONICAL-MOBILE-UI-20260814 \*/.*?(?=</style>)',
    '',
    t,
    count=1,
    flags=re.S,
)
css = r'''
    /* CANONICAL-MOBILE-UI-20260814 */
    .sidebar-downloads .resource-download{background:var(--teal-950)!important;color:#fff!important;border:1px solid var(--teal-950)!important;font-family:Outfit,Arial,sans-serif!important;font-size:.78rem!important;font-weight:600!important;line-height:1.25!important;min-height:42px!important;height:auto!important;padding:9px 13px!important;border-radius:12px!important;box-shadow:0 7px 16px rgba(15,61,68,.11)!important;white-space:normal!important;text-align:center!important}
    html[lang="ar"] .sidebar-downloads .resource-download{font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important;font-size:.72rem!important}
    .sidebar-downloads .action-icon{font-size:.9rem!important;line-height:1!important;flex:0 0 auto}
    .royal-document{width:min(430px,100%)!important;margin:0 auto!important;padding:9px!important;background:#fff!important;border:1px solid rgba(201,169,97,.55)!important;border-radius:20px!important;overflow:hidden!important}
    .royal-document img{display:block!important;width:100%!important;height:auto!important;max-height:none!important;object-fit:contain!important;object-position:center!important;border-radius:12px!important}
    .royal-document figcaption{padding:10px 7px 5px!important;text-align:center!important;color:var(--teal-950)!important}
    .royal-document figcaption strong{font-size:.72rem!important;line-height:1.35!important}
    @media(max-width:980px){
      .mobile-panel{padding:17px 20px 22px!important;overflow-y:auto!important}
      .mobile-panel > a{font-family:Outfit,Arial,sans-serif!important;font-size:.9rem!important;font-weight:600!important;line-height:1.35!important;padding:8px 0!important}
      html[lang="ar"] .mobile-panel > a{font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important;font-size:.84rem!important}
      .mobile-panel .sidebar-downloads{gap:7px!important;margin-top:12px!important;padding-bottom:22px!important}
      .royal-document{width:min(340px,88vw)!important}
    }
    @media(max-width:650px){
      .mobile-panel{padding:15px 18px 20px!important}
      .mobile-panel > a{font-size:.84rem!important;padding:7px 0!important}
      html[lang="ar"] .mobile-panel > a{font-size:.78rem!important}
      .sidebar-downloads .resource-download{font-size:.72rem!important;min-height:40px!important;padding:8px 11px!important;border-radius:11px!important}
      html[lang="ar"] .sidebar-downloads .resource-download{font-size:.67rem!important}
      .royal-document{width:min(310px,86vw)!important;padding:7px!important}
    }
'''
t = t.replace('</style>', css + '\n  </style>', 1)
p.write_text(t, encoding="utf-8")


def jpeg_size(path: Path):
    data = path.read_bytes()
    assert data[:2] == b'\xff\xd8' and data[-2:] == b'\xff\xd9', f"{path}: invalid JPEG"
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        i += 2
        if marker in (0xD8, 0xD9):
            continue
        if i + 2 > len(data):
            break
        ln = int.from_bytes(data[i:i+2], "big")
        if marker in range(0xC0, 0xC4):
            h = int.from_bytes(data[i+3:i+5], "big")
            w = int.from_bytes(data[i+5:i+7], "big")
            return w, h
        i += ln
    raise AssertionError(f"{path}: dimensions not found")

portrait_file = Path('assets/Dr_Adeelah_Qattan_Portrait_High_Resolution.jpg')
cert_file = Path('assets/King_Fahd_Medal_Certificate_2019.jpg')
cv_file = Path('assets/Dr_Adeelah_Qattan_CV_2026.pdf')
assert portrait_file.stat().st_size > 50000
assert cert_file.stat().st_size > 20000
assert cv_file.stat().st_size > 50000
pw, ph = jpeg_size(portrait_file)
cw, ch = jpeg_size(cert_file)
assert pw >= 500 and ph >= 500, (pw, ph)
assert cw >= 500 and ch > cw, (cw, ch)

t = p.read_text(encoding="utf-8")
assert PORTRAIT in t and CERT in t and CV in t

hs = t.index('<header class="hero"')
he = t.index('</header>', hs)
hero = t[hs:he]
assert hero.count('View Royal Honour') == 1
assert 'Print / Save CV' not in hero and 'window.print()' not in hero

ms = t.index('<div class="mobile-panel"')
me = t.index('</div>\n\n  <header', ms)
menu = t[ms:me]
assert menu.count('resource-download') == 5
for token in [
    '🏅','View Royal Honour','عرض التكريم الملكي',
    '🖼️','Download Personal Photo','تحميل الصورة الشخصية',
    '📄','Download Speaker Bio (PDF)','تحميل النبذة التعريفية (PDF)',
    '📘','Download CV (PDF)','تحميل السيرة الذاتية (PDF)',
    '🖨️','Print / Save CV','طباعة / حفظ السيرة'
]:
    assert token in menu, token

rs = t.index('<section class="royal" id="royal">')
re_ = t.index('</section>', rs)
royal = t[rs:re_]
assert '<a ' not in royal and 'download=' not in royal and 'onclick=' not in royal

for token in [
    'Academic Affairs &amp; Training','الشؤون الأكاديمية والتدريب',
    'Medical Education &amp; Training Department','إدارة التعليم الطبي والتدريب',
    'atqattan@hotmail.com','adeelahqattan@gmail.com','Mumaris+','ممارس+',
    '2nd Medical Education Conference','Healthcare Artificial Intelligence',
    '3rd Medical Education Conference','Innovation in Medical Education',
    '4th Medical Education Conference','AI and Medical Education: Partnership for Resilient Healthcare',
    '5th Medical Education Leadership Summit','From Innovation to Measurable Impact and Sustainable System',
    'From AI to Responsible Intelligence','Conference Committee Chair','رئيسة لجنة المؤتمر',
    'Scholarship','Human Resources','Advisory','Postgraduate',
    'Continuing Professional Development','Weekly','Train-the-Trainer',
    'Leadership Team','Research','Ethics',
    'html[lang="en"] .ar{display:none!important}',
    'html[lang="ar"] .en{display:none!important}'
]:
    assert token in t, token

print('PASS canonical portfolio audit')
print('portrait', portrait_file.stat().st_size, (pw, ph))
print('certificate', cert_file.stat().st_size, (cw, ch))
print('cv', cv_file.stat().st_size)
print('side_actions', menu.count('resource-download'))
