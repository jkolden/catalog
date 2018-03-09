#!/usr/bin/env python
# python code for the logs problem.

import datetime
import psycopg2
DBNAME = "news"


def sql_helper(query):
    """helper function to run sql queries"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        query = c.execute(query)
        results = c.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    db.close
    return results


def top_articles():
    """print the most downloaded articles"""
    query = ("""SELECT count(l.*) count, a.title
                FROM log l, articles a
                WHERE '/article/' || a.slug = l.path
                GROUP BY path, title
                ORDER BY count desc limit 3""")
    articles = sql_helper(query)
    print("The three most popular articles are:")
    for views, title in articles:
        print('"{}" - {:,d} views'.format(title, views))


def popular_authors():
    """print the most popular authors"""
    query = ("""SELECT auth.name, count(l.*) count
                FROM log l
                JOIN articles a on '/article/' || a.slug = l.path
                LEFT JOIN authors auth ON a.author=auth.id
                GROUP BY auth.name
                ORDER BY count desc""")
    authors = sql_helper(query)
    print("The most downloaded authors are:")
    for author, views in authors:
        print('{} - {:,d} views'.format(author, views))


def fails():
    """find days when download errors exceeded 1 percent of the /
    total downloads for that day"""
    query = ("""SELECT d, (fail * 1.0 / total) * 100 pct
                FROM (SELECT cast(time as date) d,
                count(*) AS total, SUM(CASE status WHEN '404 NOT FOUND'
                THEN 1 ELSE 0 END) AS fail
                FROM log group by d) as foo
                where ((fail * 1.0 / total) * 1.0) * 100 > 1""")
    fails = sql_helper(query)
    print("Days when more than 1% of downloads led to errors:")
    for date, pct in fails:
        print('{:%B %d, %Y} - {:.2f}% errors'.format(date, pct))


if __name__ == "__main__":
    top_articles()
    print("-------------------")
    popular_authors()
    print("-------------------")
    fails()
