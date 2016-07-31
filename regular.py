import re 
p=re.compile('diel_[0-9]')
keyword=["diel_[0-9]","via_[0-9]","net_[0-9]"]
p=re.compile(keyword[0])
m=p.match('via_3dfkds')
m.group()
