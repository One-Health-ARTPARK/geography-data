from lxml import etree

def _text(el):
    t = el.text or ""
    for c in el.iterchildren():
        t += c.text or ""
    return t.strip(" \n\t")

def parse(filepath):
    context = etree.iterparse(filepath, events=('end',), tag="tr", html=True)
    i = 0
    rows = []
    
    while context:
        event, el = next(context, (None, None))
        if el is None:
            break
        if el.tag=="tr" and el.getparent().get("id")=="__bookmark_2":
            i += 1
            row = [_text(child) for child in el.cssselect("td, th")]
            if row[0]!="":
                rows.append(row)
            if i<4:
                continue
            if i%2!=0:
                continue
            
        while el.getprevious() is not None:
            del el.getparent()[0]
    
    headers = rows[0]
    data = []
    for row in rows[1:]:
        row_dict = {}
        for i in range(len(headers)):
            key, val = headers[i], row[i]
            row_dict[key] = val
        data.append(row_dict)
    return data