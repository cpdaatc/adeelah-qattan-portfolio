import puppeteer from 'puppeteer-core';

const browser = await puppeteer.launch({headless:true, executablePath:process.env.CHROME, args:['--no-sandbox','--disable-dev-shm-usage']});
const page = await browser.newPage();
await page.setViewport({width:390,height:844,deviceScaleFactor:1});
const base='http://127.0.0.1:8000/';
const fail=(m)=>{throw new Error(m)};

await page.goto(base,{waitUntil:'networkidle0'});
await page.evaluate(()=>Promise.all([...document.images].map(i=>i.complete?true:new Promise(r=>{i.onload=i.onerror=r}))));
let hero=await page.$eval('.portrait-frame img',i=>({src:i.getAttribute('src'),nw:i.naturalWidth,nh:i.naturalHeight,w:i.getBoundingClientRect().width,h:i.getBoundingClientRect().height}));
if(hero.nw<400||hero.nh<400) fail('Hero portrait intrinsic size too small: '+JSON.stringify(hero));
if(hero.w<180||hero.h<180) fail('Hero portrait rendered too small');
await page.screenshot({path:'qa-artifacts/01-en-hero.png',fullPage:false});

await page.click('#menuBtn');
await page.waitForFunction(()=>document.body.classList.contains('menu-open'));
const enMenu=await page.$$eval('.sidebar-downloads .resource-download',els=>els.map(e=>({txt:e.innerText.trim(),h:e.getBoundingClientRect().height,fs:parseFloat(getComputedStyle(e).fontSize),bg:getComputedStyle(e).backgroundColor,color:getComputedStyle(e).color,href:e.getAttribute('href')})));
if(enMenu.length!==4) fail('Expected 4 mobile actions, got '+enMenu.length);
for(const a of enMenu){if(a.h>52||a.h<38) fail('Button height out of range '+JSON.stringify(a)); if(a.fs>16) fail('Button font too large '+JSON.stringify(a));}
if(!enMenu.some(x=>x.txt.includes('Download Personal Photo'))) fail('Photo action missing');
if(enMenu.some(x=>x.txt.includes('Print'))) fail('Unexpected print action');
await page.screenshot({path:'qa-artifacts/02-en-menu.png',fullPage:false});

await page.click('#menuBtn');
await page.click('#langToggle');
await page.waitForFunction(()=>document.documentElement.lang==='ar'&&document.documentElement.dir==='rtl');
const langState=await page.evaluate(()=>({lang:document.documentElement.lang,dir:document.documentElement.dir,en:[...document.querySelectorAll('.en')].filter(e=>getComputedStyle(e).display!=='none').length,ar:[...document.querySelectorAll('.ar')].filter(e=>getComputedStyle(e).display!=='none').length}));
if(langState.en!==0||langState.ar<5) fail('Language isolation failed '+JSON.stringify(langState));
await page.click('#menuBtn');
await page.waitForFunction(()=>document.body.classList.contains('menu-open'));
const arMenu=await page.$$eval('.sidebar-downloads .resource-download',els=>els.map(e=>({txt:e.innerText.trim(),h:e.getBoundingClientRect().height,fs:parseFloat(getComputedStyle(e).fontSize)})));
if(arMenu.length!==4) fail('AR expected 4 actions');
if(!arMenu.some(x=>x.txt.includes('تحميل الصورة الشخصية'))) fail('Arabic photo label missing');
for(const a of arMenu){if(a.h>52||a.h<38||a.fs>16) fail('AR button sizing failed '+JSON.stringify(a));}
await page.screenshot({path:'qa-artifacts/03-ar-menu.png',fullPage:false});

await page.click('#menuBtn');
await page.goto(base+'#royal',{waitUntil:'networkidle0'});
await page.evaluate(()=>document.querySelector('#royal').scrollIntoView({block:'start'}));
await new Promise(r=>setTimeout(r,400));
const cert=await page.$eval('.royal-document img',i=>{const r=i.getBoundingClientRect();return {src:i.getAttribute('src'),nw:i.naturalWidth,nh:i.naturalHeight,w:r.width,h:r.height,fit:getComputedStyle(i).objectFit,link:!!i.closest('a')}});
if(cert.nw<200||cert.nh<=cert.nw) fail('Certificate intrinsic dimensions invalid '+JSON.stringify(cert));
if(cert.fit!=='contain') fail('Certificate object-fit not contain');
if(cert.link) fail('Certificate must be display-only');
const ri=cert.nw/cert.nh, rr=cert.w/cert.h; if(Math.abs(ri-rr)>.03) fail('Certificate rendered aspect ratio cropped '+JSON.stringify(cert));
if(cert.w>330) fail('Certificate too wide on mobile');
await page.screenshot({path:'qa-artifacts/04-ar-royal.png',fullPage:false});

await page.goto(base,{waitUntil:'networkidle0'});
const metas=await page.evaluate(()=>({og:document.querySelector('meta[property="og:image"]')?.content,tw:document.querySelector('meta[name="twitter:image"]')?.content}));
if(!metas.og?.includes('share-preview.jpg')||!metas.tw?.includes('share-preview.jpg')) fail('Share preview metadata incorrect '+JSON.stringify(metas));
const resources=await page.$$eval('.sidebar-downloads a.resource-download',els=>els.map(e=>e.getAttribute('href')));
for(const href of resources.filter(Boolean).filter(x=>!x.startsWith('#'))){const res=await fetch(new URL(href,base));if(!res.ok) fail('Download resource failed '+href+' '+res.status);const b=await res.arrayBuffer();if(b.byteLength<5000) fail('Download resource suspiciously small '+href+' '+b.byteLength);}
const required=['atqattan@hotmail.com','adeelahqattan@gmail.com','2nd Medical Education Conference','Healthcare Artificial Intelligence','3rd Medical Education Conference','Innovation in Medical Education','4th Medical Education Conference','AI and Medical Education: Partnership for Resilient Healthcare','5th Medical Education Leadership Summit','From Innovation to Measurable Impact and Sustainable System','From AI to Responsible Intelligence','Conference Committee Chair','رئيسة لجنة المؤتمر'];
const html=await page.content(); for(const token of required){if(!html.includes(token)) fail('Missing HTML content '+token)}

const share=await browser.newPage(); await share.setViewport({width:1200,height:630,deviceScaleFactor:1});
await share.goto(base+'assets/share-preview.jpg?v=20260815-canonical',{waitUntil:'networkidle0'}); await share.screenshot({path:'qa-artifacts/05-share-preview.png',fullPage:false});
console.log('PASS MOBILE RENDER QA',JSON.stringify({hero,enMenu,arMenu,cert,metas}));
await browser.close();
