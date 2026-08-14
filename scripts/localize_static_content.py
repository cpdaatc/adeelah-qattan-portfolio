from pathlib import Path
p=Path('index.html')
t=p.read_text(encoding='utf-8')

def rep(old,new,required=False):
    global t
    if required and old not in t:
        raise SystemExit(f'missing required target: {old[:90]}')
    t=t.replace(old,new)

# Identity / hero.
rep('<a class="brand" href="#home">A. Qattan <i>— Portfolio</i></a>', '<a class="brand" href="#home"><span class="en">A. Qattan <i>— Portfolio</i></span><span class="ar">د. عديلة قطان <i>— المحفظة المهنية</i></span></a>', True)
rep('<h1>Dr. Adeelah Talat <em>Qattan</em></h1>', '<h1><span class="en">Dr. Adeelah Talat <em>Qattan</em></span><span class="ar">د. عديلة طلعت <em>قطان</em></span></h1>', True)
rep('<div class="portrait-note"><small>ROYAL HONOUR · 2019</small><b>King Fahd Medal<br>Third Degree</b></div>', '<div class="portrait-note"><small><span class="en">ROYAL HONOUR · 2019</span><span class="ar">تكريم ملكي · 2019</span></small><b><span class="en">King Fahd Medal<br>Third Degree</span><span class="ar">ميدالية الملك فهد<br>الدرجة الثالثة</span></b></div>', True)
rep('<div class="overline">ROYAL HONOUR · 2019</div>', '<div class="overline"><span class="en">ROYAL HONOUR · 2019</span><span class="ar">تكريم ملكي · 2019</span></div>', True)
rep('<h2>King Fahd Medal <span>Third Degree</span></h2>', '<h2><span class="en">King Fahd Medal <span>Third Degree</span></span><span class="ar">ميدالية الملك فهد <span>الدرجة الثالثة</span></span></h2>', True)

# Section labels.
for en,ar in [
    ('01 / Leadership','01 / القيادة'),('02 / Career','02 / المسيرة المهنية'),('03 / Governance','03 / الحوكمة'),
    ('04 / Quality &amp; Research','04 / الجودة والبحث'),('05 / Credentials','05 / المؤهلات'),
    ('06 / Recognition','06 / التكريم والتقدير'),('07 / Activities','07 / الأنشطة المهنية'),('08 / References','08 / المراجع المهنية')]:
    rep(f'<small>{en}</small>', f'<small><span class="en">{en}</span><span class="ar">{ar}</span></small>', True)

# Impact labels.
for en,ar in [('Accreditation','الاعتماد'),('Digital','التحول الرقمي'),('Education','التعليم والتدريب'),('Clinical Pathways','المسارات السريرية'),('Strategy','الاستراتيجية')]:
    rep(f'<div class="impact-row"><b>{en}</b>', f'<div class="impact-row"><b><span class="en">{en}</span><span class="ar">{ar}</span></b>', True)

# Current date labels with Present.
for year in ['2023','2017','1992']:
    rep(f'<time>{year} — Present</time>', f'<time><span class="en">{year} — Present</span><span class="ar">{year} — حتى الآن</span></time>')

# Quality project meta and conference ordinal labels.
rep('<span>Level 2</span>', '<span><span class="en">Level 2</span><span class="ar">المستوى الثاني</span></span>')
for old,en,ar in [('2023 · 2nd','2023 · 2nd','2023 · الثاني'),('2024 · 3rd','2024 · 3rd','2024 · الثالث'),('2025 · 4th','2025 · 4th','2025 · الرابع'),('2026 · 5th','2026 · 5th','2026 · الخامس')]:
    rep(f'<div class="year">{old}</div>', f'<div class="year"><span class="en">{en}</span><span class="ar">{ar}</span></div>')

# Credentials that were static English.
rep('<h3>SCFHS Saudi Board in Restorative Dentistry</h3><p>Certified Consultant — Saudi Commission for Health Specialties</p>', '<h3><span class="en">SCFHS Saudi Board in Restorative Dentistry</span><span class="ar">البورد السعودي في إصلاح الأسنان — الهيئة السعودية للتخصصات الصحية</span></h3><p><span class="en">Certified Consultant — Saudi Commission for Health Specialties</span><span class="ar">استشاري معتمد — الهيئة السعودية للتخصصات الصحية</span></p>')
rep('<h3>Saudi Specialty Certificate</h3><p>SSC-(DENT) RESTO · Saudi Commission for Health Specialties</p>', '<h3><span class="en">Saudi Specialty Certificate</span><span class="ar">شهادة الاختصاص السعودية</span></h3><p><span class="en">SSC-(DENT) RESTO · Saudi Commission for Health Specialties</span><span class="ar">إصلاح الأسنان · الهيئة السعودية للتخصصات الصحية</span></p>')
rep('<p>National Committee of Bioethics</p>', '<p><span class="en">National Committee of Bioethics</span><span class="ar">اللجنة الوطنية للأخلاقيات الحيوية</span></p>')

# Recognition entries.
recs=[
('2nd Medical Education Conference','مؤتمر التعليم الطبي الثاني'),
('Appreciation recognition · MODHS','شهادة تقدير · الخدمات الصحية بوزارة الدفاع'),
('Utilisation of Dental Clinic','استخدام عيادات الأسنان'),
('Recognition of Excellence &amp; Success of the Flow Initiative','التقدير للتميز ونجاح مبادرة Flow'),
('King Fahd Medal — Third Degree','ميدالية الملك فهد — الدرجة الثالثة'),
('CBAHI Hospital Accreditation Recognition','تقدير اعتماد المستشفى من سباهي (CBAHI)'),
('Recognition for support in achieving accreditation','تقدير للمساهمة في تحقيق الاعتماد'),
('Joint Commission International Accreditation','اعتماد اللجنة الدولية المشتركة (JCI)'),
('Institutional appreciation recognition','تقدير مؤسسي للمساهمة في الاعتماد'),
('Saudi Heritage Preservation Society','الجمعية السعودية للمحافظة على التراث'),
('Contribution to the UNESCO Intangible Heritage listing of the Oboe file','المساهمة في ملف التراث الثقافي غير المادي لدى اليونسكو'),
('Qualifying National Health Cadres','تأهيل الكوادر الصحية الوطنية'),
('Recognition associated with SCFHS','تقدير مرتبط بالهيئة السعودية للتخصصات الصحية')]
for en,ar in recs:
    rep(f'<h3>{en}</h3>', f'<h3><span class="en">{en}</span><span class="ar">{ar}</span></h3>')
    rep(f'<p>{en}</p>', f'<p><span class="en">{en}</span><span class="ar">{ar}</span></p>')
# A few texts appear as paragraph values distinct from titles.
rep('<p>Appreciation recognition · MODHS</p>', '<p><span class="en">Appreciation recognition · MODHS</span><span class="ar">شهادة تقدير · الخدمات الصحية بوزارة الدفاع</span></p>')
rep('<p>KFAFH / MODHS</p>', '<p><span class="en">KFAFH / MODHS</span><span class="ar">مستشفى الملك فهد للقوات المسلحة / الخدمات الصحية بوزارة الدفاع</span></p>')
rep('<p>Recognition for support in achieving accreditation</p>', '<p><span class="en">Recognition for support in achieving accreditation</span><span class="ar">تقدير للمساهمة في تحقيق الاعتماد</span></p>')
rep('<p>Institutional appreciation recognition</p>', '<p><span class="en">Institutional appreciation recognition</span><span class="ar">تقدير مؤسسي للمساهمة في الاعتماد</span></p>')
rep('<p>Contribution to the UNESCO Intangible Heritage listing of the Oboe file</p>', '<p><span class="en">Contribution to the UNESCO Intangible Heritage listing of the Oboe file</span><span class="ar">المساهمة في ملف التراث الثقافي غير المادي لدى اليونسكو</span></p>')
rep('<p>Recognition associated with SCFHS</p>', '<p><span class="en">Recognition associated with SCFHS</span><span class="ar">تقدير مرتبط بالهيئة السعودية للتخصصات الصحية</span></p>')

# Activity cards: bilingual content in both toggle states.
acts={
'NCBE — National Committee of Bioethics, SCFHS':'NCBE — اللجنة الوطنية للأخلاقيات الحيوية، الهيئة السعودية للتخصصات الصحية',
'Train the Trainer — Healthcare Leadership Academy':'تدريب المدربين — أكاديمية القيادة الصحية',
'Emotional Intelligence for Healthcare Leaders':'الذكاء العاطفي لقادة الرعاية الصحية',
'Train the Trainer — Royal College of Surgeons in Ireland':'تدريب المدربين — الكلية الملكية للجراحين في أيرلندا',
'Train the Trainer for Healthcare Practitioners':'تدريب المدربين للممارسين الصحيين',
'Building High-Performing Healthcare Teams':'بناء فرق رعاية صحية عالية الأداء',
'Sharp Thinking for Successful Action':'التفكير الحاد من أجل عمل ناجح',
'Posterior Composite Restoration &amp; Dental Bleaching — Speaker, KFAFH':'ترميمات الكمبوزيت الخلفية وتبييض الأسنان — متحدثة، مستشفى الملك فهد للقوات المسلحة',
'Dental Composite — Speaker, 9th Makkah International Dental Conference':'الكمبوزيت السني — متحدثة، مؤتمر مكة الدولي التاسع لطب الأسنان',
'Direct Resin Composite Restoration &amp; Porcelain Laminate Veneers — Workshops':'ترميمات الراتنج المركب المباشرة وقشور البورسلان — ورش عمل',
'Restorative Dentistry Symposium — Chair, KFAFH':'ندوة إصلاح الأسنان — رئيسة الندوة، مستشفى الملك فهد للقوات المسلحة'}
for en,ar in acts.items():
    rep(f'<span>{en}</span>', f'<span><span class="en">{en}</span><span class="ar">{ar}</span></span>')

# Professional references: bilingual names/descriptions.
refs={
'Maj. Gen. Dr. Ibrahim Al Nasser':'اللواء الطبيب د. إبراهيم الناصر',
'Maj. Gen. Dr. Fayez Bokhari':'اللواء الطبيب د. فايز بخاري',
'Prof. Abdul-Ghani Mira':'أ.د. عبدالغني ميرا',
'Dr. Mansour Qassem Asiri':'د. منصور قاسم عسيري',
'Hospital Director · Head &amp; Consultant, Radio Diagnostic Department · KFAFH':'مدير المستشفى · رئيس واستشاري قسم الأشعة التشخيصية · مستشفى الملك فهد للقوات المسلحة',
'Assistant Hospital Director for Technical &amp; Medical Affairs · Director of Medical Administration · KFAFH':'مساعد مدير المستشفى للشؤون الفنية والطبية · مدير الإدارة الطبية · مستشفى الملك فهد للقوات المسلحة',
'Dean, College of Dentistry · Professor of Restoration &amp; Cosmetic Dentistry · King Abdulaziz University':'عميد كلية طب الأسنان · أستاذ إصلاح وتجميل الأسنان · جامعة الملك عبدالعزيز',
'Chairman, Scientific Council for Dental Restoration — SCFHS · Vice Dean for Postgraduate Studies':'رئيس المجلس العلمي لإصلاح الأسنان — الهيئة السعودية للتخصصات الصحية · وكيل الكلية للدراسات العليا'}
for en,ar in refs.items():
    rep(f'<h3>{en}</h3>', f'<h3><span class="en">{en}</span><span class="ar">{ar}</span></h3>')
    rep(f'<p>{en}</p>', f'<p><span class="en">{en}</span><span class="ar">{ar}</span></p>')

# Footer identity and institution.
rep('<div class="footer-name">Dr. Adeelah Talat <em>Qattan</em></div>', '<div class="footer-name"><span class="en">Dr. Adeelah Talat <em>Qattan</em></span><span class="ar">د. عديلة طلعت <em>قطان</em></span></div>', True)
rep('<span>King Fahd Armed Forces Hospital · Jeddah, KSA</span><span><span class="en">Professional Portfolio</span><span class="ar">المحفظة المهنية</span></span>', '<span><span class="en">King Fahd Armed Forces Hospital · Jeddah, KSA</span><span class="ar">مستشفى الملك فهد للقوات المسلحة · جدة، المملكة العربية السعودية</span></span><span><span class="en">Professional Portfolio</span><span class="ar">المحفظة المهنية</span></span>', True)

# Verify key user-facing static labels have language pairs.
for pair in [
('ROYAL HONOUR · 2019','تكريم ملكي · 2019'),('01 / Leadership','01 / القيادة'),('02 / Career','02 / المسيرة المهنية'),
('Accreditation','الاعتماد'),('Digital','التحول الرقمي'),('Education','التعليم والتدريب'),
('Download CV (PDF)','تحميل السيرة الذاتية (PDF)'),('Download Personal Photo','تحميل الصورة الشخصية'),
('Download Speaker Bio (PDF)','تحميل النبذة التعريفية (PDF)')]:
    en,ar=pair
    assert en in t and ar in t, pair
assert 'html[lang="ar"] .en{display:none!important}' in t
assert 'html[lang="ar"] .ar{display:initial}' in t

p.write_text(t,encoding='utf-8')
print('static bilingual parity applied')
