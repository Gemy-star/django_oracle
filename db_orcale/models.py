from django.db import models
import os
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('172.16.1.50', '1521', service_name='ORCL')


def get_resYear():
    resYear = None

    try:
        # create a connection to the Oracle Database
        with cx_Oracle.connect(user=r'res', password='res', dsn=dsn_tns) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # call the function
                return_value = cursor.var(cx_Oracle.DB_TYPE_CURSOR)
                resYear = cursor.callfunc('FU_RES_YEAR',
                                          return_value,
                                          )
                res = resYear.fetchall()
    except cx_Oracle.Error as error:
        print(error)

    return res
