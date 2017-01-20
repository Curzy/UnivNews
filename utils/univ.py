def univ_info2dict(univ_name, title, prefix_url, link):
    link = link if 'http' in link else prefix_url + link
    data = {
        'univ': univ_name,
        'title': title,
        'link': link
    }
    return data
