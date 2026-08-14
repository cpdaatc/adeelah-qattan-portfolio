from pathlib import Path
import re

VERSION = "release-20260815-final"
PORTRAIT = f"assets/Dr_Adeelah_Qattan_Personal_Photo.jpg?v={VERSION}"
CERT = f"assets/King_Fahd_Medal_Certificate_2019_Final.jpg?v={VERSION}"
CV = f"assets/Dr_Adeelah_Qattan_CV_2026.pdf?v={VERSION}"
BIO = f"assets/Dr_Adeelah_Qattan_Speaker_Bio_Bilingual.pdf?v={VERSION}"
SHARE = f"assets/share-preview.jpg?v={VERSION}"

p = Path("index.html")
t = p.read_text(encoding="utf-8")

# Verified portrait in hero. Download uses the same clean, frame-free JPEG asset.
t, n = re.subn(
    r'(<div class="portrait-frame">\s*<img\s+src=")[^"]+("[^>]*>)',
    rf'\1{PORTRAIT}\2', t, count=1, flags=re.S
)
assert n == 1, "hero portrait not found exactly once"

# Main hero: only the requested Royal Honour navigation action.
hero_actions = '''<div class="hero-actions">
          <a class="btn btn-primary" href="#royal">
            <span class="action-icon" aria-hidden="true">🏅</span>
            <span class="en">View Royal Honour</span>
            <span class="ar">عرض التكريم الملكي</span>
          </a>
        </div>'''
t, n = re.subn(r'<div class="hero-actions">.*?</div>', hero_actions, t, count=1, flags=re.S)
assert n == 1, "hero actions not found exactly once"

# Side menu: four requested resource/navigation actions + Print/Save, compact and bilingual.
side_actions = f'''<div class="sidebar-downloads">
      <a class="btn resource-download" href="#royal">
        <span class="action-icon" aria-hidden="true">🏅</span>
        <span class="en">View Royal Honour</span><span class="ar">عرض التكريم الملكي</span>
      </a>
      <a class="btn resource-download" href="{PORTRAIT}" download="Dr_Adeelah_Qattan_Personal_Photo.jpg">
        <span class="action-icon" aria-hidden="true">🖼️</span>
        <span class="en">Download Personal Photo</span><span class="ar">تحميل الصورة الشخصية</span>
      </a>
      <a class="btn resource-download" href="{BIO}" download>
        <span class="action-icon" aria-hidden="true">📄</span>
        <span class="en">Download Speaker Bio (PDF)</span><span class="ar">تحميل النبذة التعريفية (PDF)</span>
      </a>
      <a class="btn resource-download" href="{CV}" download>
        <span class="action-icon" aria-hidden="true">📘</span>
        <span class="en">Download CV (PDF)</span><span class="ar">تحميل السيرة الذاتية (PDF)</span>
      </a>
      <button class="btn resource-download" type="button" onclick="window.print()">
        <span class="action-icon" aria-hidden="true">🖨️</span>
        <span class="en">Print / Save CV</span><span class="ar">طباعة / حفظ السيرة</span>
      </button>
    </div>'''
t, n = re.subn(r'<div class="sidebar-downloads">.*?</div>', side_actions, t, count=1, flags=re.S)
assert n == 1, "sidebar-downloads not found exactly once"

# Full Royal Honour certificate, display-only. No link, download, click or crop.
royal_section = f'''
  <section class="royal" id="royal">
    <div class="container royal-grid canonical-royal-grid">
      <figure class="royal-document" aria-label="King Fahd Medal certificate 2019">
        <img src="{CERT}" alt="King Fahd Medal — Third Degree certificate, 2019" loading="eager">
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

# Social sharing preview uses the freshly rebuilt portrait-based card.
t = re.sub(r'assets/share-preview\.jpg\?v=[^"\']+', SHARE, t)

# Remove old final override blocks, then append one deterministic responsive override.
t = re.sub(r'/\* FINAL-PORTFOLIO-RELEASE-20260815 .*? /\* END-FINAL-PORTFOLIO-RELEASE-20260815 \*/', '', t, flags=re.S)
css = r'''
    /* FINAL-PORTFOLIO-RELEASE-20260815 */
    html[lang="en"] .ar{display:none!important}
    html[lang="ar"] .en{display:none!important}
    html[lang="ar"] .ar{display:initial!important}
    html[lang="ar"] .block.ar{display:block!important}
    html[lang="ar"] .inline.ar{display:inline!important}

    .sidebar-downloads{display:grid!important;gap:8px!important;margin-top:16px!important}
    .sidebar-downloads .resource-download{
      width:100%!important;min-height:42px!important;height:auto!important;
      padding:9px 13px!important;border:1px solid var(--teal-950)!important;
      border-radius:12px!important;background:var(--teal-950)!important;color:#fff!important;
      box-shadow:0 7px 16px rgba(15,61,68,.11)!important;
      font-family:Outfit,Arial,sans-serif!important;font-size:.78rem!important;font-weight:600!important;
      line-height:1.25!important;letter-spacing:0!important;text-transform:none!important;
      white-space:normal!important;text-align:center!important;justify-content:center!important;gap:8px!important;
    }
    html[lang="ar"] .sidebar-downloads .resource-download{
      font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important;font-size:.72rem!important;
    }
    .sidebar-downloads .action-icon{font-size:.92rem!important;line-height:1!important;flex:0 0 auto!important}

    .canonical-royal-grid{grid-template-columns:minmax(280px,420px) 1fr!important;gap:48px!important;align-items:center!important}
    .royal-document{width:min(420px,100%)!important;margin:0 auto!important;padding:9px!important;background:#fff!important;
      border:1px solid rgba(201,169,97,.55)!important;border-radius:20px!important;overflow:hidden!important;position:relative!important;z-index:3!important}
    .royal-document img{display:block!important;width:100%!important;height:auto!important;max-height:none!important;
      object-fit:contain!important;object-position:center!important;border-radius:12px!important;background:#fff!important}
    .royal-document figcaption{padding:10px 7px 5px!important;text-align:center!important;color:var(--teal-950)!important;background:#fff!important}
    .royal-document figcaption strong{font-family:Outfit,Arial,sans-serif!important;font-size:.72rem!important;line-height:1.35!important}
    html[lang="ar"] .royal-document figcaption strong{font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important}

    @media(max-width:980px){
      .mobile-panel{padding:17px 20px 22px!important;overflow-y:auto!important}
      .mobile-panel > a{font-family:Outfit,Arial,sans-serif!important;font-size:.90rem!important;font-weight:600!important;
        line-height:1.35!important;padding:8px 0!important;letter-spacing:0!important;text-transform:none!important}
      html[lang="ar"] .mobile-panel > a{font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important;font-size:.84rem!important}
      .mobile-panel .sidebar-downloads{gap:7px!important;margin-top:12px!important;padding-bottom:22px!important}
      .canonical-royal-grid{grid-template-columns:1fr!important;gap:30px!important;text-align:center!important}
      .royal-document{width:min(340px,88vw)!important}
      .royal-copy p,.royal-line{margin-left:auto!important;margin-right:auto!important}
      .hero h1{font-size:clamp(3rem,12vw,4.6rem)!important;line-height:.92!important}
      .role{font-size:.94rem!important}
      .institution{font-size:.86rem!important}
    }
    @media(max-width:650px){
      nav{height:70px!important}
      .brand{font-size:1.12rem!important}
      .container{width:min(100% - 32px,1180px)!important}
      .hero{padding-top:98px!important;padding-bottom:58px!important}
      .hero-grid{gap:34px!important}
      .hero h1{font-size:clamp(2.75rem,11.8vw,4.15rem)!important;line-height:.92!important}
      .kicker{font-size:.64rem!important;margin-bottom:14px!important}
      .role-stack{margin:24px 0 20px!important;padding-left:16px!important;gap:7px!important}
      html[dir="rtl"] .role-stack{padding-left:0!important;padding-right:16px!important}
      .role{font-size:.86rem!important;line-height:1.55!important}
      .institution{font-size:.80rem!important;line-height:1.65!important;margin-bottom:22px!important}
      .hero-actions .btn{min-height:42px!important;padding:0 15px!important;font-size:.76rem!important;border-radius:12px!important}
      .portrait-shell{width:min(330px,82vw)!important}
      .portrait-note{padding:12px 14px!important;max-width:178px!important;right:0!important}
      .portrait-note b{font-size:.92rem!important}
      .mobile-panel{padding:15px 18px 20px!important}
      .mobile-panel > a{font-size:.84rem!important;padding:7px 0!important}
      html[lang="ar"] .mobile-panel > a{font-size:.78rem!important}
      .sidebar-downloads .resource-download{font-size:.72rem!important;min-height:40px!important;padding:8px 11px!important;border-radius:11px!important}
      html[lang="ar"] .sidebar-downloads .resource-download{font-size:.67rem!important}
      .royal{padding:72px 0!important}
      .royal-document{width:min(315px,86vw)!important;padding:7px!important}
      .royal-copy h2{font-size:clamp(2.55rem,12vw,3.55rem)!important}
      .royal-copy p{font-size:.84rem!important;line-height:1.7!important}
    }
    /* END-FINAL-PORTFOLIO-RELEASE-20260815 */
'''
t = t.replace('</style>', css + '\n  </style>', 1)

p.write_text(t, encoding="utf-8")

# Static release gates.
t = p.read_text(encoding="utf-8")
for token in [PORTRAIT, CERT, CV, BIO, SHARE]:
    assert token in t, token

hs=t.index('<header class="hero"'); he=t.index('</header>',hs); hero=t[hs:he]
assert hero.count('View Royal Honour') == 1
assert 'Print / Save CV' not in hero and 'window.print()' not in hero

ms=t.index('<div class="mobile-panel"'); me=t.index('</div>\n\n  <header',ms); menu=t[ms:me]
assert menu.count('resource-download') == 5
for token in ['🏅','View Royal Honour','عرض التكريم الملكي','🖼️','Download Personal Photo','تحميل الصورة الشخصية',
              '📄','Download Speaker Bio (PDF)','تحميل النبذة التعريفية (PDF)','📘','Download CV (PDF)',
              'تحميل السيرة الذاتية (PDF)','🖨️','Print / Save CV','طباعة / حفظ السيرة']:
    assert token in menu, token

rs=t.index('<section class="royal" id="royal">'); re_=t.index('</section>',rs); royal=t[rs:re_]
assert '<a ' not in royal and 'download=' not in royal and 'onclick=' not in royal

required = [
 'Academic Affairs &amp; Training','الشؤون الأكاديمية والتدريب',
 'Medical Education &amp; Training Department','إدارة التعليم الطبي والتدريب',
 'atqattan@hotmail.com','adeelahqattan@gmail.com',
 '2nd Medical Education Conference','Healthcare Artificial Intelligence',
 '3rd Medical Education Conference','Innovation in Medical Education',
 '4th Medical Education Conference','AI and Medical Education: Partnership for Resilient Healthcare',
 '5th Medical Education Leadership Summit','From Innovation to Measurable Impact and Sustainable System',
 'From AI to Responsible Intelligence','Conference Committee Chair','رئيسة لجنة المؤتمر',
 'Scholarship','Human Resources','Advisory','Postgraduate','Continuing Professional Development','Weekly',
 'Train-the-Trainer','Leadership Team','Research','Ethics',
 'html[lang="en"] .ar{display:none!important}','html[lang="ar"] .en{display:none!important}'
]
for token in required:
    assert token in t, token

print('PASS static canonical release audit')
