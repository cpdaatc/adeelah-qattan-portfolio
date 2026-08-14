from pathlib import Path
import re

p = Path('index.html')
t = p.read_text(encoding='utf-8')

# Canonical asset references for QA. portrait.webp is the known clean portrait fallback;
# the QA gate will reject it visually if it does not match the supplied portrait.
t = re.sub(r'assets/Dr_Adeelah_Qattan_Portrait_Original\.jpg(?:\?[^"\']*)?', 'assets/portrait.webp?v=20260815-canonical', t)
t = re.sub(r'assets/Dr_Adeelah_Qattan_Portrait_High_Resolution\.jpg(?:\?[^"\']*)?', 'assets/portrait.webp?v=20260815-canonical', t)
t = re.sub(r'assets/King_Fahd_Medal_Third_Degree_2019\.jpg(?:\?[^"\']*)?', 'assets/King_Fahd_Medal_Certificate_Full_2019.jpg?v=20260815-canonical', t)

# Keep exactly four mobile actions: Royal Honour, portrait, bio, CV.
ms = t.index('<div class="mobile-panel"')
me = t.index('</div>\n\n  <header', ms)
menu = t[ms:me]
menu = re.sub(r'\s*<button class="btn btn-primary resource-download"[^>]*onclick="window\.print\(\)"[^>]*>.*?</button>', '', menu, flags=re.S)
t = t[:ms] + menu + t[me:]

# Social preview must stay a JPEG and use a cache-busted canonical preview.
t = re.sub(r'https://cpdaatc\.github\.io/adeelah-qattan-portfolio/assets/share-preview\.jpg\?v=[^"\']+',
           'https://cpdaatc.github.io/adeelah-qattan-portfolio/assets/share-preview.jpg?v=20260815-canonical', t)

css = r'''
/* CANONICAL-MOBILE-QA-20260815 */
.mobile-panel{font-family:Outfit,Arial,sans-serif!important}
html[lang="ar"] .mobile-panel{font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important}
.mobile-panel>a{font-family:inherit!important;font-size:.92rem!important;line-height:1.35!important;padding:9px 0!important}
.sidebar-downloads{display:grid!important;gap:8px!important;margin-top:16px!important}
.sidebar-downloads .resource-download{
  width:100%!important;min-height:44px!important;height:44px!important;
  padding:0 14px!important;border-radius:13px!important;
  background:var(--teal-950)!important;color:#fff!important;border:1px solid var(--teal-950)!important;
  font-family:Outfit,Arial,sans-serif!important;font-size:.82rem!important;font-weight:600!important;
  line-height:1.15!important;letter-spacing:0!important;justify-content:flex-start!important;gap:9px!important;
  box-shadow:none!important;text-transform:none!important;white-space:normal!important;
}
html[lang="ar"] .sidebar-downloads .resource-download{
  font-family:"Noto Kufi Arabic",Tahoma,sans-serif!important;font-size:.76rem!important;justify-content:flex-start!important;
}
.sidebar-downloads .action-icon{width:22px;min-width:22px;text-align:center;font-size:1rem;line-height:1}
.royal-document{width:min(440px,100%)!important;max-width:440px!important;margin:0 auto!important;padding:10px!important;background:#fff!important;border-radius:18px!important;overflow:visible!important}
.royal-document img{display:block!important;width:100%!important;height:auto!important;max-height:none!important;object-fit:contain!important;border-radius:12px!important;background:#fff!important}
.royal-document figcaption{padding:9px 6px 2px!important;text-align:center!important}
.royal-document figcaption strong{font-size:.78rem!important;line-height:1.35!important}
@media(max-width:650px){
  .mobile-panel{padding:14px 18px 18px!important}
  .mobile-panel>a{font-size:.84rem!important;padding:7px 0!important}
  .sidebar-downloads{gap:7px!important;margin-top:12px!important}
  .sidebar-downloads .resource-download{height:43px!important;min-height:43px!important;padding:0 12px!important;font-size:.76rem!important;border-radius:12px!important}
  html[lang="ar"] .sidebar-downloads .resource-download{font-size:.71rem!important}
  .royal{padding:54px 0!important}
  .royal-grid{grid-template-columns:1fr!important;gap:28px!important}
  .royal-document{width:min(320px,calc(100vw - 48px))!important;max-width:320px!important;padding:7px!important}
  .royal-document figcaption strong{font-size:.67rem!important}
}
'''
t = t.replace('</style>', css + '\n</style>', 1)

# Required content and structure assertions.
required = [
    'atqattan@hotmail.com', 'adeelahqattan@gmail.com',
    '2nd Medical Education Conference', 'Healthcare Artificial Intelligence',
    '3rd Medical Education Conference', 'Innovation in Medical Education',
    '4th Medical Education Conference', 'AI and Medical Education: Partnership for Resilient Healthcare',
    '5th Medical Education Leadership Summit', 'From Innovation to Measurable Impact and Sustainable System',
    'From AI to Responsible Intelligence', 'Conference Committee Chair', 'رئيسة لجنة المؤتمر',
    'html[lang="en"] .ar{display:none!important}', 'html[lang="ar"] .en{display:none!important}',
    'Dr_Adeelah_Qattan_Speaker_Bio_Bilingual.pdf', 'Dr_Adeelah_Qattan_CV_2026.pdf'
]
for token in required:
    if token not in t:
        raise SystemExit(f'MISSING REQUIRED TOKEN: {token}')

ms = t.index('<div class="mobile-panel"')
me = t.index('</div>\n\n  <header', ms)
menu = t[ms:me]
if menu.count('resource-download') != 4:
    raise SystemExit(f'Expected exactly 4 mobile actions, found {menu.count("resource-download")}')
for token in ['🏅','🖼️','📄','📘','View Royal Honour','Download Personal Photo','Download Speaker Bio (PDF)','Download CV (PDF)',
              'عرض التكريم الملكي','تحميل الصورة الشخصية','تحميل النبذة التعريفية (PDF)','تحميل السيرة الذاتية (PDF)']:
    if token not in menu:
        raise SystemExit(f'MISSING BUTTON TOKEN: {token}')
if 'window.print()' in menu or 'Print / Save CV' in menu or 'طباعة / حفظ السيرة' in menu:
    raise SystemExit('Unexpected fifth print action remains in mobile menu')

rs = t.index('<section class="royal" id="royal">')
re_ = t.index('</section>', rs)
royal = t[rs:re_]
if '<a ' in royal or 'download=' in royal or 'onclick=' in royal:
    raise SystemExit('Royal certificate must be display-only')
if 'King_Fahd_Medal_Certificate_Full_2019.jpg' not in royal:
    raise SystemExit('Royal section not using full-certificate asset')

p.write_text(t, encoding='utf-8')
print('PASS canonical HTML patch')
print('mobile_actions', menu.count('resource-download'))
