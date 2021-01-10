import requests
from bs4 import BeautifulSoup
import sqlite3


def get_new_post():
    url_home = 'https://www.familug.org/search?max-results=100'
    r = requests.get(url_home)
    tree = BeautifulSoup(markup=r.text, features='html.parser')
    node_home = tree.find_all(name='h3', attrs={'class': 'post-title entry-title', 'itemprop': 'name'})
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    my_id = 1
    for node in node_home:
        node = str(node)
        link = node[node.find('http'): node.find('html') + 4]
        title = node[node.find('html') + 6: node.find('</a>')]
        c.execute('INSERT INTO awesomejob_fami_post VALUES (?, ?, ?)', (my_id, title, link))
        my_id += 1
    conn.commit()
    conn.close()


def get_python_post():
    page = 1
    my_id = 1
    url = 'https://www.familug.org/search/label/Python?max-results=100'
    while True:
        if page == 1:
            url = 'https://www.familug.org/search/label/Python?max-results=100'
        else:
            r = requests.get(url)
            tree = BeautifulSoup(markup=r.text, features='html.parser')
            node = tree.find_all(name='a', attrs={'class': 'blog-pager-older-link', 'id': 'Blog1_blog-pager-older-link'})
            node = str(node)
            url = node[node.find('href') + 6: node.find('title') - 2]
        r = requests.get(url)
        tree = BeautifulSoup(markup=r.text, features='html.parser')
        nodes = tree.find_all(name='h3', attrs={'class': 'post-title entry-title', 'itemprop': 'name'})
        if nodes == []:
            break
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()
        for node in nodes:
            node = str(node)
            link = node[node.find('http'): node.find('html') + 4]
            title = node[node.find('html') + 6: node.find('</a>')]
            c.execute('INSERT INTO awesomejob_python_fami_post VALUES (?, ?, ?)', (my_id, title, link))
            my_id += 1
        conn.commit()
        conn.close()
        page += 1


def get_sys_post():
    page = 1
    my_id = 1
    url = 'https://www.familug.org/search/label/sysadmin?max-results=100'
    while True:
        if page == 1:
            url = 'https://www.familug.org/search/label/sysadmin?max-results=100'
        else:
            r = requests.get(url)
            tree = BeautifulSoup(markup=r.text, features='html.parser')
            node = tree.find_all(name='a', attrs={'class': 'blog-pager-older-link', 'id': 'Blog1_blog-pager-older-link'})
            node = str(node)
            url = node[node.find('href') + 6: node.find('title') - 2]
        r = requests.get(url)
        tree = BeautifulSoup(markup=r.text, features='html.parser')
        nodes = tree.find_all(name='h3', attrs={'class': 'post-title entry-title', 'itemprop': 'name'})
        if nodes == []:
            break
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()
        for node in nodes:
            node = str(node)
            link = node[node.find('http'): node.find('html') + 4]
            title = node[node.find('html') + 6: node.find('</a>')]
            c.execute('INSERT INTO awesomejob_sys_fami_post VALUES (?, ?, ?)', (my_id, title, link))
            my_id += 1
        conn.commit()
        conn.close()
        page += 1


def get_com_post():
    page = 1
    my_id = 1
    url = 'https://www.familug.org/search/label/Command?max-results=100'
    while True:
        if page == 1:
            url = 'https://www.familug.org/search/label/Command?max-results=100'
        else:
            r = requests.get(url)
            tree = BeautifulSoup(markup=r.text, features='html.parser')
            node = tree.find_all(name='a', attrs={'class': 'blog-pager-older-link', 'id': 'Blog1_blog-pager-older-link'})
            node = str(node)
            url = node[node.find('href') + 6: node.find('title') - 2]
        r = requests.get(url)
        tree = BeautifulSoup(markup=r.text, features='html.parser')
        nodes = tree.find_all(name='h3', attrs={'class': 'post-title entry-title', 'itemprop': 'name'})
        if nodes == []:
            break
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()
        for node in nodes:
            node = str(node)
            link = node[node.find('http'): node.find('html') + 4]
            title = node[node.find('html') + 6: node.find('</a>')]
            c.execute('INSERT INTO awesomejob_com_fami_post VALUES (?, ?, ?)', (my_id, title, link))
            my_id += 1
        conn.commit()
        conn.close()
        page += 1


def main():
    get_new_post()
    get_com_post()
    get_sys_post()
    get_python_post()


if __name__ == "__main__":
    main()
