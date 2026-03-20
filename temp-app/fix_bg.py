with open('portfolio.html', 'r', encoding='utf-8') as f: text = f.read()
for t in ['D4ciMv4.jpg', '958DvKQ.jpg', 'JrvsgXo.jpg', 'lxfKiWw.jpg']:
    text = text.replace(f"url('https://i.imgur.com/{t}') center/cover", f"url('https://i.imgur.com/{t}') top/cover")
    # Also just in case they meant the whole image to show, we could use contain. But top/cover is standard. 
    # If they complain again, I will change to center/contain.
with open('portfolio.html', 'w', encoding='utf-8') as f: f.write(text)
print("Done fixing background positions.")
