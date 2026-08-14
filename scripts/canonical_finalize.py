from pathlib import Path
import re

VERSION = "canonical-20260814-v2"
PORTRAIT = f"assets/Dr_Adeelah_Qattan_Portrait_High_Resolution.jpg?v={VERSION}"
CERT = f"assets/King_Fahd_Medal_Certificate_2019.jpg?v={VERSION}"
CV = f"assets/Dr_Adeelah_Qattan_CV_2026.pdf?v={VERSION}"
BIO = f"assets/Dr_Adeelah_Qattan_Speaker_Bio_Bilingual.pdf?v={VERSION}"

p = Path("index.html")
t = p.read_text(encoding="utf-8")

# 1) Hero portrait: point to the verified standalone portrait asset.
t, n = re.subn(
    r'(<div class="portrait-frame">\s*<img\s+src=")[^"]+("[^>]*>)',
    rf'\1{PORTRAIT}\2', t, count=1, flags=re.S
)
assert n == 1, "hero portrait not found exactly once"

# 2) Hero actions: user requested only Royal Honour here; Print remains in side menu only.
hero_actions = (
    '<div class="hero-actions">'
    '<a class="btn btn-primary" href="#royal">'
    '<span class="action-icon" aria-hidden="true">🏅</span>'
    '<span class="en">View Royal Honour</span>'
    '<span class="ar">عرض التكريم الملكي</span>'
    '</a></div>'
)
t, n = re.subn(r'<div class="hero-actions">.*?</div>', hero_actions, t, count=1, flags=re.S)
assert n == 1, "hero actions not found exactly once"

# 3) Side menu: exactly five compact, bilingual actions.
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
assert n == 1, "side actions not found exactly once"

# 4) Replace the entire Royal Honour section with a stable display-only structure.
royal_section = f'''
  <section class="royal" id="royal">
    <div class="container royal-grid canonical-royal-grid">
      <figure class="royal-document" aria-label="King Fahd Medal certificate 2019">
        <img src="{CERT}" alt="King Fahd Medal — Third Degree certificate, 2019">
        <figcaption>
          <strong class="en">King Fahd Medal — Third Degree · 2019</strong>
          <strong class="ar">ميدالية الملك فهد — الدرجة الثالثة · 2019</strong>
        </figcaption>
      </figure>
      <div class="royal-copy">
        <div class="overline"><span class="en">Royal Honour · 2019</span><span class="ar">التكريم الملكي · 2019</span></div>
        <h2><span class="en">King Fahd Medal <span>Third Degree</span></span><span class="ar">ميدالية الملك فهد <span>الدرجة الثالثة</span></span></h2>
        <p class="en">Awarded by the Custodian of the Two Holy Mosques, King Salman Bin Abdul Aziz Al Saud, in recognition of excellence in service.</p>
        <p class="ar">مُنحت من خادم الحرمين الشريفين الملك سلمان بن عبدالعزيز آل سعود تقديرًا للتميز في الخدمة.</p>
        <div class="royal-line"></div>
      </div>
    </div>
  </section>'''
t, n = re.subn(r'\s*<section class="royal" id="royal">.*?</section>', '\n' + royal_section, t, count=1, flags=re.S)
assert n == 1, "royal section not found exactly once"

# 5) Remove any prior canonical override and add one final deterministic mobile/UI override.
t = re.sub(r'/\* CANONICAL-MOBILE-UI-20260814(?:-V2)? \*/.*?(?=</style>)', '', t, count=1, flags=re.S)
css = r'''
    /* CANONICAL-MOBILE-UI-20260814-V2 */
    .canonical-royal-grid{grid-template-columns:minmax(280px,430px) 1fr!important;gap:48px!important;align-items:center!important}
    .royal-document{width:min(430px,100%)!important;margin:0 auto!important;padding:9px!important;background:#fff!important;border:1px solid rgba(201,169,97,.55)!important;border-radius:20px!important;overflow:hidden!important;position:relative!important;z-index:3!important}
    .royal-document img{display:block!important;width:100%!important;height:auto!important;max-height:none!important;object-fit:contain!important;object-position:center!important;border-radius:12px!important;background:#fff!important}
    .royal-document figcaption{padding:10px 7px 5px!important;text-align:center!important;color:var(--teal-950)!important;background:#fff!important}
    .royal-document figcaption strong{font-family:Outfit,Arial,sans-serif!important;font-size:.72rem!important;line-height:1.35!important}
    html[lang="ar"] .royal-document figcaption strong{font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important}
    .sidebar-downloads .resource-download{display:flex!important;width:100%!important;background:var(--teal-950)!important;color:#fff!important;border:1px solid var(--teal-950)!important;font-family:Outfit,Arial,sans-serif!important;font-size:.78rem!important;font-weight:600!important;line-height:1.25!important;min-height:42px!important;height:auto!important;padding:9px 13px!important;border-radius:12px!important;box-shadow:0 7px 16px rgba(15,61,68,.11)!important;white-space:normal!important;text-align:center!important;justify-content:center!important;gap:8px!important}
    html[lang="ar"] .sidebar-downloads .resource-download{font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important;font-size:.72rem!important}
    .sidebar-downloads .action-icon{font-size:.9rem!important;line-height:1!important;flex:0 0 auto!important}
    @media(max-width:980px){
      .mobile-panel{padding:17px 20px 22px!important;overflow-y:auto!important}
      .mobile-panel > a{font-family:Outfit,Arial,sans-serif!important;font-size:.9rem!important;font-weight:600!important;line-height:1.35!important;padding:8px 0!important}
      html[lang="ar"] .mobile-panel > a{font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important;font-size:.84rem!important}
      .mobile-panel .sidebar-downloads{gap:7px!important;margin-top:12px!important;padding-bottom:22px!important}
      .canonical-royal-grid{grid-template-columns:1fr!important;gap:30px!important;text-align:center!important}
      .royal-document{width:min(340px,88vw)!important}
      .royal-copy p,.royal-line{margin-left:auto!important;margin-right:auto!important}
    }
    @media(max-width:650px){
      .mobile-panel{padding:15px 18px 20px!important}
      .mobile-panel > a{font-size:.84rem!important;padding:7px 0!important}
      html[lang="ar"] .mobile-panel > a{font-size:.78rem!important}
      .sidebar-downloads .resource-download{font-size:.72rem!important;min-height:40px!important;padding:8px 11px!important;border-radius:11px!important}
      html[lang="ar"] .sidebar-downloads .resource-download{font-size:.67rem!important}
      .royal-document{width:min(310px,86vw)!important;padding:7px!important}
      .royal-copy h2{font-size:clamp(2.7rem,13vw,3.7rem)!important}
    }
'''
t = t.replace('</style>', css + '\n  </style>', 1)
p.write_text(t, encoding="utf-8")

# --- Gate checks ---
def jpeg_size(path: Path):
    data = path.read_bytes()
    assert data[:2] == b'\xff\xd8' and data[-2:] == b'\xff\xd9', f"{path}: invalid JPEG"
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1; continue
        marker = data[i+1]; i += 2
        if marker in (0xD8,0xD9): continue
        if i + 2 > len(data): break
        ln = int.from_bytes(data[i:i+2], 'big')
        if marker in range(0xC0,0xC4):
            h = int.from_bytes(data[i+3:i+5], 'big')
            w = int.from_bytes(data[i+5:i+7], 'big')
            return w,h
        i += ln
    raise AssertionError(f"{path}: dimensions not found")

portrait_file = Path('assets/Dr_Adeelah_Qattan_Portrait_High_Resolution.jpg')
cert_file = Path('assets/King_Fahd_Medal_Certificate_2019.jpg')
cv_file = Path('assets/Dr_Adeelah_Qattan_CV_2026.pdf')
assert portrait_file.stat().st_size > 50000
assert cert_file.stat().st_size > 20000
assert cv_file.stat().st_size > 50000
pw,ph = jpeg_size(portrait_file); cw,ch = jpeg_size(cert_file)
assert pw >= 500 and ph >= 500, (pw,ph)
assert cw >= 500 and ch > cw, (cw,ch)

t = p.read_text(encoding='utf-8')
assert PORTRAIT in t and CERT in t and CV in t and BIO in t

hs=t.index('<header class="hero"'); he=t.index('</header>',hs); hero=t[hs:he]
assert hero.count('View Royal Honour') == 1
assert 'Print / Save CV' not in hero and 'window.print()' not in hero

ms=t.index('<div class="mobile-panel"'); me=t.index('</div>\n\n  <header',ms); menu=t[ms:me]
assert menu.count('resource-download') == 5
for token in ['🏅','View Royal Honour','عرض التكريم الملكي','🖼️','Download Personal Photo','تحميل الصورة الشخصية','📄','Download Speaker Bio (PDF)','تحميل النبذة التعريفية (PDF)','📘','Download CV (PDF)','تحميل السيرة الذاتية (PDF)','🖨️','Print / Save CV','طباعة / حفظ السيرة']:
    assert token in menu, token

rs=t.index('<section class="royal" id="royal">'); re_=t.index('</section>',rs); royal=t[rs:re_]
assert '<a ' not in royal and 'download=' not in royal and 'onclick=' not in royal

for token in ['Academic Affairs &amp; Training','الشؤون الأكاديمية والتدريب','Medical Education &amp; Training Department','إدارة التعليم الطبي والتدريب','atqattan@hotmail.com','adeelahqattan@gmail.com','2nd Medical Education Conference','Healthcare Artificial Intelligence','3rd Medical Education Conference','Innovation in Medical Education','4th Medical Education Conference','AI and Medical Education: Partnership for Resilient Healthcare','5th Medical Education Leadership Summit','From Innovation to Measurable Impact and Sustainable System','From AI to Responsible Intelligence','Conference Committee Chair','رئيسة لجنة المؤتمر','Scholarship','Human Resources','Advisory','Postgraduate','Continuing Professional Development','Weekly','Train-the-Trainer','Leadership Team','Research','Ethics','html[lang="en"] .ar{display:none!important}','html[lang="ar"] .en{display:none!important}']:
    assert token in t, token

print('PASS canonical portfolio audit')
print('portrait', portrait_file.stat().st_size, (pw,ph))
print('certificate', cert_file.stat().st_size, (cw,ch))
print('cv', cv_file.stat().st_size)
print('side_actions', menu.count('resource-download'))
