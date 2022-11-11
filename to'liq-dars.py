# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 08:26:18 2022

@author: User
"""

# download postgresql
# pip install psycopg2

import psycopg2
import psycopg2.extras


hostname='localhost'
database='baza'
username='postgres'
pwd='parolingiz'
port_id=5432

conn=None

# Hatolik bo'lganda exceptga tushadi
try:
    with psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    ) as conn:

        # cursor_factory=psycopg2.extras.DictCursor SHU KOD BULMASA HAM BOLADI, BU MALUMOTNI DICT QILIB BER
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            # cur.execute('DROP TABLE IF EXISTS forexample')

            # BUYRUQ YOZIB OLINADI
            # ikkinci marta kodni yurgizganda table yaratilmaydi
            create_table = """
                CREATE TABLE IF NOT EXISTS forexample(
                    id SERIAL PRIMARY KEY,
                    name varchar(40) NOT NULL,
                    namee varchar(40) NULL
                )
            """
            # PSQL GA BUYRUQ YUBORIL
            cur.execute(create_table)

            # BAZAGA MALUMOT YOZISH
            # insert_value = [('vali','valiyev'),('ali','aliyev')]
            # insert_code = "INSERT INTO forexample (name,namee) VALUES(%s, %s)"
            # for n in insert_value:
            #     cur.execute(insert_code, n)

            # MALUMOT OZGAR
            update_code = "UPDATE forexample SET name='ali'"
            cur.execute(update_code)

            update_code2="UPDATE forexample SET name='vali' WHERE id=1"
            cur.execute(update_code2)

            update_code3 = "UPDATE forexample SET name='gali' WHERE id=%s"
            update_word = ('3')
            cur.execute(update_code3, update_word)

            # MALUMOT OCHiRiSH
            delete_code="DELETE FROM forexample WHERE id=%s"
            delete_id=('5')
            cur.execute(delete_code, delete_id)

            # MALUMOT OQISH
            cur.execute('SELECT * FROM forexample')
            # print(cur.fetchall())
            for n in cur.fetchall():
                print(f"{n['id']} - {n['name']}")

except Exception as error: # Bu degani hatolikni chiqar degani
    print(error)

finally:
    if conn is not None:
        conn.close()