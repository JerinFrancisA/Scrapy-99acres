# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class QuotesPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('house.db')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""drop table if exists homes""")
        self.cur.execute("""create table homes(
                            price text,
                            title text,    
                            area text,
                            society text,
                            description text,
                            features text,
                            link text
                            )""")

    def insert_tb(self, item):
        self.cur.execute("""insert into homes values(?,?,?,?,?,?,?)""", (
            item["price"],
            item["title"],
            item["area"],
            item["society"],
            item["description"],
            item["features"],
            item["link"]))
        self.conn.commit()

    def process_item(self, item, spider):
        self.insert_tb(item)
        return item
