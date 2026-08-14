from pathlib import Path
p=Path('index.html')
t=p.read_text(encoding='utf-8')
old='''      <figure class="royal-document">
        <img src="assets/King_Fahd_Medal_Third_Degree_2019.jpg?v=20260814-2" alt="King Fahd Medal — Third Degree, 2019 documentation">
        <figcaption><span class="en">King Fahd Medal — Third Degree · 2019</span><span class="ar">ميدالية الملك فهد — الدرجة الثالثة · 2019</span></figcaption>
      </figure>'''
new='''      <figure class="royal-document">
        <a class="royal-image-link" href="assets/King_Fahd_Medal_Third_Degree_2019.jpg?v=20260814-2" target="_blank" rel="noopener" aria-label="Open King Fahd Medal image full size">
          <img src="assets/King_Fahd_Medal_Third_Degree_2019.jpg?v=20260814-2" alt="King Fahd Medal — Third Degree, 2019 documentation" loading="eager" decoding="sync">
        </a>
        <figcaption>
          <strong><span class="en">King Fahd Medal — Third Degree · 2019</span><span class="ar">ميدالية الملك فهد — الدرجة الثالثة · 2019</span></strong>
          <small><span class="en">Tap or click the image to view it full size</span><span class="ar">اضغط على الصورة لعرضها بالحجم الكامل والتكبير</span></small>
        </figcaption>
      </figure>'''
if old not in t:
    raise SystemExit('royal document markup not found')
t=t.replace(old,new,1)
oldcss='.royal-document{margin:0;position:relative;border:1px solid rgba(201,169,97,.65);padding:8px;background:#fff;border-radius:18px;box-shadow:0 24px 55px rgba(0,0,0,.2);overflow:hidden}.royal-document img{display:block;width:100%;height:auto;border-radius:11px}.royal-document figcaption{padding:10px 8px 4px;color:var(--teal-950);font-size:.68rem;font-weight:600;text-align:center}'
newcss='.royal-document{margin:0;position:relative;border:1px solid rgba(201,169,97,.72);padding:10px;background:#fff;border-radius:18px;box-shadow:0 28px 70px rgba(0,0,0,.24);overflow:hidden;width:100%;max-width:480px}.royal-image-link{display:block;overflow:hidden;border-radius:11px;background:#fff;cursor:zoom-in}.royal-document img{display:block;width:100%;height:auto;border-radius:11px;filter:contrast(1.05) saturate(1.02);transform:translateZ(0)}.royal-document figcaption{padding:12px 8px 5px;color:var(--teal-950);text-align:center;line-height:1.45}.royal-document figcaption strong{display:block;font-size:.72rem}.royal-document figcaption small{display:block;margin-top:4px;font-size:.61rem;color:#6b777c;font-weight:500}'
if oldcss not in t:
    raise SystemExit('royal document CSS not found')
t=t.replace(oldcss,newcss,1)
t=t.replace('.royal-grid{grid-template-columns:minmax(250px,310px) 1fr}', '.royal-grid{grid-template-columns:minmax(380px,480px) 1fr}',1)
t=t.replace('.royal-document{max-width:310px;margin:auto}', '.royal-document{max-width:480px;margin:auto}',1)
assert 'royal-image-link' in t
assert 'اضغط على الصورة لعرضها بالحجم الكامل والتكبير' in t
p.write_text(t,encoding='utf-8')
