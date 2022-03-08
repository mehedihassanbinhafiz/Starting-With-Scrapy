# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter


# after crawled We need to store data,  The data is stored by pipelines.

class QuotetutorialPipeline:
    def __init__(self):
        self.create_conn()
        self.create_table()

    def create_conn(self):
        self.conn = sqlite3.connect('quote.sqlite3')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""drop table if exists quotes""")  # drop the table if it is exist.
        self.cur.execute("""create table quotes(
                title text,
                author text,
                tag text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        print('pipeline: ', item['title'][0])
        return item

    def store_db(self, item):
        self.cur.execute("""insert into quotes values (?,?,?) """,
                         (item['title'][0], item['author'][0], item['tags'][0]))
        self.conn.commit()


class BinaryPipeline:
    def __init__(self):
        pass
