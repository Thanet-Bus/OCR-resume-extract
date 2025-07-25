import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('USER')
pwd = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
db = os.getenv('DB_NAME')

try:
    connection = psycopg2.connect(
        user = user, 
        password = pwd, 
        host = host, 
        port = port, 
        database = db)
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(record)
except (Exception, Error) as error:
    print('Error while connecting to PosgreSQL: ', error)

def generate_itewandjob_code(job):
    job = job.upper()
    dt=datetime.now().strftime('%y%m')
    try:
        set = Settingsys.objects.get(runreprot=job)
    except Settingsys.DoesNotExist:
        set = Settingsys.objects.create(runreprot=job, runnumberrt=0)        
    set.runnumberrt=set.runnumberrt+1
    runnumber=str(set.runnumberrt).zfill(3)  
    set.save()
    unid=job+dt+runnumber
    return unid