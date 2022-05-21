# web crawler

def get_next_target(s):
	start_link = s.find('a href=')
	if start_link == -1:
		return None, 0
	else:
		start_quote = s.find('"', start_link)
		end_quote = s.find('"', start_quote + 1)
		url = s[start_quote+1:end_quote]
		return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			union(tocrawl, get_all_links(get_page(page))
			crawled.append(page)
	return crawled
	
print get_all_links('this is a website')	