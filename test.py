
import mysql.connector

db = mysql.connector.connect(
    host = 'PRCSGI1884L',
    user = 'root',
    passwd = 'admin',
    database = 'workflow_engine'
)

#print('database is : ',db)
mycursor = db.cursor()


mycursor.execute("select value as description_german , instructions from workflow_engine.error_descriptions where id in(select error_description_id from workflow_engine.error_code_descriptions where error_code_id in (select  id from workflow_engine.error_codes where id in (select error_code_id from workflow_engine.tasks where id = 1))) and language_code = 'de-DE'")
data = mycursor.fetchall()
for x in data:
    errordesc = x[0];
    errorIns = x[1];
    print(errordesc)
    print(errorIns)

taskId = 1
mycursor.execute('select error_time from workflow_engine.tasks where id = %s',(taskId,))

data = mycursor.fetchone()
for x in data:
    errorTime = x;
    print(errorTime)