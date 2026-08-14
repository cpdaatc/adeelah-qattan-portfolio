from pathlib import Path

p = Path('index.html')
t = p.read_text(encoding='utf-8')

# Metadata / social description.
t = t.replace(
    'Consultant in Restorative Dentistry, Assistant Hospital Director for Academic Affairs, and Director of Medical Education and Training.',
    'Consultant in Restorative Dentistry, Assistant Hospital Director for Academic Affairs & Training, and Director of Medical Education and Training.'
)

# Desktop: no duplicate CV control. Resources are kept in the side panel.
desktop_print = '''        <button class="control print-top" onclick="window.print()" aria-label="Print CV"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M7 8V3h10v5M7 17H5a2 2 0 0 1-2-2v-4a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v4a2 2 0 0 1-2 2h-2M7 14h10v7H7z"/></svg><span class="en">Print CV</span><span class="ar">طباعة السيرة</span></button>\n'''
if desktop_print in t:
    t = t.replace(desktop_print, '', 1)

# Side-panel downloads: every action has semantically matched EN/AR labels.
old_side = '''    <button class="btn btn-primary" style="margin-top:22px;width:100%" onclick="window.print()"><span class="en">Print / Save CV as PDF</span><span class="ar">طباعة / حفظ السيرة PDF</span></button>'''
new_side = '''    <div class="sidebar-downloads">
      <a class="btn btn-primary resource-download" href="assets/Dr_Adeelah_Qattan_CV_2026.pdf" download><span class="en">Download CV (PDF)</span><span class="ar">تحميل السيرة الذاتية (PDF)</span></a>
      <a class="btn btn-ghost resource-download" href="assets/Dr_Adeelah_Qattan_Portrait_High_Resolution.jpg" download><span class="en">Download Personal Photo</span><span class="ar">تحميل الصورة الشخصية</span></a>
      <a class="btn btn-ghost resource-download" href="assets/Dr_Adeelah_Qattan_Speaker_Bio_Bilingual.pdf" download><span class="en">Download Speaker Bio (PDF)</span><span class="ar">تحميل النبذة التعريفية (PDF)</span></a>
    </div>'''
if old_side not in t:
    raise SystemExit('sidebar print action not found')
t = t.replace(old_side, new_side, 1)

# Current titles — hero.
old_role = '''          <div class="role"><strong class="en">Assistant Hospital Director</strong><strong class="ar">مساعد مدير المستشفى</strong> — <span class="en">Academic Affairs</span><span class="ar">للشؤون الأكاديمية</span></div>'''
new_role = '''          <div class="role"><strong class="en">Assistant Hospital Director</strong><strong class="ar">المساعد لمدير المستشفى</strong> — <span class="en">Academic Affairs &amp; Training</span><span class="ar">للشؤون الأكاديمية والتدريب</span></div>'''
if old_role not in t:
    raise SystemExit('hero assistant role not found')
t = t.replace(old_role, new_role, 1)

old_director = '''          <div class="role"><strong class="en">Director</strong><strong class="ar">مدير</strong> — <span class="en">Medical Education &amp; Training</span><span class="ar">التعليم الطبي والتدريب</span></div>'''
new_director = '''          <div class="role"><strong class="en">Director</strong><strong class="ar">مدير</strong> — <span class="en">Medical Education &amp; Training Department</span><span class="ar">إدارة التعليم الطبي والتدريب</span></div>'''
if old_director not in t:
    raise SystemExit('hero director role not found')
t = t.replace(old_director, new_director, 1)

# Leadership narrative and career titles.
t = t.replace(
    'and currently serving as Assistant Hospital Director for Academic Affairs.',
    'and currently serving as Assistant Hospital Director for Academic Affairs & Training.'
)
t = t.replace(
    'وصولًا إلى دورها الحالي كمساعد مدير المستشفى للشؤون الأكاديمية.',
    'وصولًا إلى دورها الحالي كمساعد لمدير المستشفى للشؤون الأكاديمية والتدريب.'
)
t = t.replace(
    '<span class="en">Assistant Hospital Director for Academic Affairs</span><span class="ar">مساعد مدير المستشفى للشؤون الأكاديمية</span>',
    '<span class="en">Assistant Hospital Director for Academic Affairs &amp; Training</span><span class="ar">المساعد لمدير المستشفى للشؤون الأكاديمية والتدريب</span>',
    1
)
t = t.replace(
    '<span class="en">Director, Medical Education &amp; Training</span><span class="ar">مدير التعليم الطبي والتدريب</span>',
    '<span class="en">Director, Medical Education &amp; Training Department</span><span class="ar">مدير إدارة التعليم الطبي والتدريب</span>',
    1
)

# Current institutional roles.
roles_section = '''
      <div class="current-roles reveal" aria-labelledby="currentRolesTitle">
        <div class="current-roles-heading">
          <div><small><span class="en">Current Institutional Roles</span><span class="ar">الأدوار المؤسسية الحالية</span></small><h3 id="currentRolesTitle"><span class="en">Leadership &amp; Committee Responsibilities</span><span class="ar">المسؤوليات القيادية واللجان الحالية</span></h3></div>
          <p class="en">Current hospital-level leadership, governance, education, development and research responsibilities.</p>
          <p class="ar">المسؤوليات الحالية على مستوى المستشفى في القيادة والحوكمة والتعليم والتطوير والبحث.</p>
        </div>
        <div class="current-roles-grid">
          <div class="current-role-card"><span class="en">Assistant Hospital Director for Academic Affairs &amp; Training</span><span class="ar">المساعد لمدير المستشفى للشؤون الأكاديمية والتدريب</span></div>
          <div class="current-role-card"><span class="en">Director, Medical Education &amp; Training Department</span><span class="ar">مدير إدارة التعليم الطبي والتدريب</span></div>
          <div class="current-role-card"><span class="en">Chair, Hospital Scholarship &amp; External Assignment Committee</span><span class="ar">رئيس لجنة الابتعاث والإيفاد بالمستشفى</span></div>
          <div class="current-role-card"><span class="en">Member, Senior Human Resources Management Committee</span><span class="ar">عضو لجنة إدارة الموارد البشرية العليا</span></div>
          <div class="current-role-card"><span class="en">Member, Senior Advisory Committee Team</span><span class="ar">عضو فريق اللجنة الاستشارية العليا</span></div>
          <div class="current-role-card"><span class="en">Member, Postgraduate Education &amp; Training Committee</span><span class="ar">عضو لجنة التعليم والتدريب للدراسات العليا</span></div>
          <div class="current-role-card"><span class="en">Chair, Hospital Continuing Professional Development Committee</span><span class="ar">رئيس لجنة التطوير المهني المستمر بالمستشفى</span></div>
          <div class="current-role-card"><span class="en">Chair, Weekly Activities &amp; External Conferences Committee</span><span class="ar">رئيس لجنة الفعاليات الأسبوعية والمؤتمرات الخارجية</span></div>
          <div class="current-role-card"><span class="en">Chair, Train-the-Trainer Committee for Physicians &amp; Healthcare Professionals</span><span class="ar">رئيس لجنة تدريب المدربين للأطباء والصحيين</span></div>
          <div class="current-role-card"><span class="en">Member, Hospital Leadership Team &amp; Steering Committee</span><span class="ar">عضو الفريق القيادي واللجنة التوجيهية بالمستشفى</span></div>
          <div class="current-role-card"><span class="en">Member, Research Committee</span><span class="ar">عضو لجنة الأبحاث</span></div>
          <div class="current-role-card"><span class="en">Member, Ethics Committee</span><span class="ar">عضو لجنة الأخلاقيات</span></div>
        </div>
      </div>
'''
marker = '      <div class="impact-list reveal">'
if 'id="currentRolesTitle"' not in t:
    if marker not in t:
        raise SystemExit('leadership insertion marker not found')
    t = t.replace(marker, roles_section + marker, 1)

# Supplied King Fahd Medal documentation image.
old_mark = '      <div class="royal-mark" aria-hidden="true"><div class="royal-star">★</div></div>'
new_mark = '''      <figure class="royal-document">
        <img src="assets/King_Fahd_Medal_Third_Degree_2019.jpg" alt="King Fahd Medal — Third Degree, 2019 documentation">
        <figcaption><span class="en">King Fahd Medal — Third Degree · 2019</span><span class="ar">ميدالية الملك فهد — الدرجة الثالثة · 2019</span></figcaption>
      </figure>'''
if old_mark not in t:
    raise SystemExit('royal visual marker not found')
t = t.replace(old_mark, new_mark, 1)

# Footer roles and emails: keep BOTH addresses; identify Mumaris+.
old_footer_role = '<span class="en">Assistant Hospital Director for Academic Affairs · Director, Medical Education &amp; Training · Consultant, Restorative Dentistry</span><span class="ar">مساعد مدير المستشفى للشؤون الأكاديمية · مدير التعليم الطبي والتدريب · استشاري إصلاح الأسنان</span>'
new_footer_role = '<span class="en">Assistant Hospital Director for Academic Affairs &amp; Training · Director, Medical Education &amp; Training Department · Consultant, Restorative Dentistry</span><span class="ar">المساعد لمدير المستشفى للشؤون الأكاديمية والتدريب · مدير إدارة التعليم الطبي والتدريب · استشاري إصلاح الأسنان</span>'
if old_footer_role not in t:
    raise SystemExit('footer role not found')
t = t.replace(old_footer_role, new_footer_role, 1)

old_contacts = '<a href="mailto:adeelahqattan@gmail.com">adeelahqattan@gmail.com</a><a href="mailto:atqattan@hotmail.com">atqattan@hotmail.com</a>'
new_contacts = '<a href="mailto:atqattan@hotmail.com"><span class="en">Mumaris+: atqattan@hotmail.com</span><span class="ar">ممارس+: atqattan@hotmail.com</span></a><a href="mailto:adeelahqattan@gmail.com"><span class="en">Additional Email: adeelahqattan@gmail.com</span><span class="ar">بريد إضافي: adeelahqattan@gmail.com</span></a>'
if old_contacts not in t:
    raise SystemExit('footer emails not found')
t = t.replace(old_contacts, new_contacts, 1)

# Styling.
css = '''
    .sidebar-downloads{display:grid;gap:10px;margin-top:22px}.resource-download{width:100%;min-height:50px}.royal-document{margin:0;position:relative;border:1px solid rgba(201,169,97,.65);padding:8px;background:#fff;border-radius:18px;box-shadow:0 24px 55px rgba(0,0,0,.2);overflow:hidden}.royal-document img{display:block;width:100%;height:auto;border-radius:11px}.royal-document figcaption{padding:10px 8px 4px;color:var(--teal-950);font-size:.68rem;font-weight:600;text-align:center}.current-roles{margin-top:46px;padding-top:40px;border-top:1px solid var(--line)}.current-roles-heading{display:flex;justify-content:space-between;gap:28px;align-items:end;margin-bottom:22px}.current-roles-heading small{display:block;color:var(--teal-600);font-size:.66rem;font-weight:700;letter-spacing:.15em;text-transform:uppercase}.current-roles-heading h3{margin:5px 0 0;color:var(--teal-950);font:600 2rem/1.05 "Cormorant Garamond",serif}.current-roles-heading p{max-width:430px;margin:0;color:var(--muted);font-size:.82rem}.current-roles-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:11px}.current-role-card{min-height:92px;padding:18px 18px 18px 21px;border:1px solid var(--line);border-radius:15px;background:#fff;color:#36474E;font-size:.8rem;font-weight:500;display:flex;align-items:center;position:relative}.current-role-card:before{content:"";position:absolute;inset:13px auto 13px 0;width:3px;border-radius:3px;background:linear-gradient(var(--teal-600),var(--gold))}html[dir="rtl"] .current-role-card{padding:18px 21px 18px 18px}html[dir="rtl"] .current-role-card:before{left:auto;right:0}.royal-grid{grid-template-columns:minmax(250px,310px) 1fr}
    @media(max-width:980px){.current-roles-grid{grid-template-columns:1fr 1fr}.current-roles-heading{display:block}.current-roles-heading p{margin-top:10px}.royal-grid{grid-template-columns:1fr}.royal-document{max-width:310px;margin:auto}}
    @media(max-width:650px){.current-roles-grid{grid-template-columns:1fr}.current-role-card{min-height:auto}.current-roles{margin-top:34px;padding-top:30px}}
'''
if '.sidebar-downloads{' not in t:
    t = t.replace('    .career{max-width:900px;margin:auto}', css + '    .career{max-width:900px;margin:auto}', 1)

# Bilingual parity and regression checks before writing.
assert 'html[lang="ar"] .en{display:none!important}' in t
assert 'html[lang="ar"] .ar{display:initial}' in t
labels = [
    ('Download CV (PDF)', 'تحميل السيرة الذاتية (PDF)'),
    ('Download Personal Photo', 'تحميل الصورة الشخصية'),
    ('Download Speaker Bio (PDF)', 'تحميل النبذة التعريفية (PDF)'),
]
for en, ar in labels:
    assert t.count(f'<span class="en">{en}</span>') == 1, en
    assert t.count(f'<span class="ar">{ar}</span>') == 1, ar
assert 'Print / Save CV as PDF' not in t
assert 'class="control print-top"' not in t
for value in [
    'المساعد لمدير المستشفى للشؤون الأكاديمية والتدريب',
    'مدير إدارة التعليم الطبي والتدريب',
    'رئيس لجنة الابتعاث والإيفاد بالمستشفى',
    'عضو لجنة إدارة الموارد البشرية العليا',
    'عضو فريق اللجنة الاستشارية العليا',
    'عضو لجنة التعليم والتدريب للدراسات العليا',
    'رئيس لجنة التطوير المهني المستمر بالمستشفى',
    'رئيس لجنة الفعاليات الأسبوعية والمؤتمرات الخارجية',
    'رئيس لجنة تدريب المدربين للأطباء والصحيين',
    'عضو الفريق القيادي واللجنة التوجيهية بالمستشفى',
    'عضو لجنة الأبحاث',
    'عضو لجنة الأخلاقيات',
    'Mumaris+: atqattan@hotmail.com',
    'ممارس+: atqattan@hotmail.com',
    'Additional Email: adeelahqattan@gmail.com',
    'بريد إضافي: adeelahqattan@gmail.com',
]:
    assert value in t, value

p.write_text(t, encoding='utf-8')
print('index.html updated and bilingual parity verified')
