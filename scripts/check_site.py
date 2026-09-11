from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=[];self.links=[];self.h1=0;self.title=0;self.errors=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.title+=1
  for k,v in attrs:
   if k in ('href','src') and v:self.links.append(v)
   if k.startswith('on') or k=='style':self.errors.append('Inline handler/style')
  if tag=='script' and not a.get('src'):self.errors.append('Inline script')
pages={p.name:Page(p.read_text(encoding='utf-8')) for p in ROOT.glob('*.html')}
errors=[]
for name,p in pages.items():
 if p.h1!=1 or p.title!=1:errors.append(name+': expected one H1/title')
 if len(p.ids)!=len(set(p.ids)):errors.append(name+': duplicate IDs')
 errors += [name+': '+e for e in p.errors]
 for link in p.links:
  u=urlsplit(link)
  if u.scheme in ('https','http','mailto','tel'):continue
  if u.scheme:errors.append(name+': unexpected URL scheme');continue
  target=unquote(u.path) or name
  f=(ROOT/target).resolve()
  if not f.is_relative_to(ROOT) or not f.is_file():errors.append(name+': missing/invalid '+target)
  if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(name+': missing fragment '+link)
 if 'C:/Users/' in (ROOT/name).read_text(encoding='utf-8'):errors.append(name+': local path leak')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(pages)} pages; local assets, anchors and structural checks.')
