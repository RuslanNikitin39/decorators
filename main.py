import app_scrapping as a_s

if __name__ == '__main__':

    base_url = 'https://habr.com'
    url = base_url + '/ru/all/'
    a_s.get_links(url, base_url)