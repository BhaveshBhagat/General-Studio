import sqlite3
from flask import Flask 
from flask import redirect, url_for, request,render_template,send_file
from werkzeug.utils import secure_filename
import os

#defining base upload folder
UPLOAD_FOLDER = 'C:/Users/Bhagat/Documents/Python/Practices/uploaded/'

#initialize...
app = Flask(__name__ , template_folder='.')

#path variable for send files
sender_path = ''

#function to check db connection
def connect_db(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('Connection is Up..')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

#function to create table if not exists...
def create_table():
    try:
        conn = sqlite3.connect('Sqlite_python.db')
        print("Connected to SQLite...")
        createTable = '''CREATE TABLE IF NOT EXISTS DataUpload
                                    (ID integer PRIMARY KEY AUTOINCREMENT,
                                    PROJECT_NAME TEXT NOT NULL,
                                    ORGANIZATION_NAME TEXT NOT NULL,
                                    SONG_METADATA TEXT NOT NULL,
                                    SONG_FILE TEXT NOT NULL,
                                    VIDEO_METADATA TEXT NOT NULL,
                                    VIDEO_FILE TEXT NOT NULL,
                                    IMAGE_METADATA TEXT NOT NULL,
                                    IMAGE_FILE TEXT NOT NULL);'''
        conn.execute(createTable)
        conn.commit()
        print("Table Created Successfully...")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


#function to insert records in table for each uploads
def insertRow(pname,orgname,smeta,sfile,vmeta,vfile,imeta,ifile):
    try:
        conn = sqlite3.connect('Sqlite_python.db')
        cursor = conn.cursor()
        print("Connected to SQLite...")
        sqlite_insert = '''INSERT INTO DataUpload(PROJECT_NAME,ORGANIZATION_NAME,SONG_METADATA,SONG_FILE,VIDEO_METADATA,VIDEO_FILE,IMAGE_METADATA,IMAGE_FILE)
                          VALUES(?,?,?,?,?,?,?,?)'''
        data_tuple = (pname,orgname,smeta,sfile,vmeta,vfile,imeta,ifile)
        cursor.execute(sqlite_insert , data_tuple )

        conn.commit()
        print('Successfully Inserted')
        cursor.close()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print('Connection Closed..')



#function to fetch the uploaded records from table...
def fetchRecords(pname , orgname):
    data = list()
    temp = list()
    try:
        conn = sqlite3.connect('Sqlite_python.db')
        cursor = conn.cursor()
        print("Connected to SQLite...")
        sqlite_insert = '''SELECT * FROM DataUpload where PROJECT_NAME = ? and  ORGANIZATION_NAME=? '''
        data_tuple = (pname,orgname)
        cursor.execute(sqlite_insert , data_tuple )
        records=cursor.fetchall()
        print('fetched all..')

        for row in records:
            temp = list()
            print(row)
            print(row[3].split('/')[-1])
            temp.append(row[3].split('/')[-1])
            print('Clear')
            temp.append(row[4].split('/')[-1])
            temp.append(row[5].split('/')[-1])
            temp.append(row[6].split('/')[-1])
            temp.append(row[7].split('/')[-1])
            temp.append(row[8].split('/')[-1])
            data.append(temp)    
        print(data)
        conn.commit()
        print('Successfully Fetched...')
        cursor.close()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print('Connection Closed..')

    return data        



#routing to home page... 
@app.route('/')
def home():
    return render_template('web_app.html')


#routing request to uploaded file
@app.route('/uploaded', methods = ['POST','GET'])
def upload():
    if request.method == 'POST':
        user = request.form['PName']
        org = request.form['OName']
        songMeta = request.files.getlist('song_metadata')
        songFile = request.files.getlist('song_file')
        videoMeta = request.files.getlist('video_Metadata')
        videoFile = request.files.getlist('video_file')
        imageMeta = request.files.getlist('image_Metadata')
        imageFile = request.files.getlist('image_file')
        print(user)
        print(org)
        if os.path.isdir(UPLOAD_FOLDER+org):
            path = UPLOAD_FOLDER+org
            print(path)

            if os.path.isdir(path+'/'+user):
                path = path+'/'+user
                print(path)
            else:
                path = os.path.join(path,user)
                print('...')
                os.mkdir(path)
                print(path)
        else:
            path = os.path.join(UPLOAD_FOLDER,org)
            os.mkdir(path)
            print(path)
            path = os.path.join(path,user)
            os.mkdir(path)
            print(path)

            
        app.config['UPLOAD_FOLDER'] = path
        
        for i in songMeta:    
                i.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(i.filename)))
                print(path)
                f1 = path+'/'+secure_filename(i.filename)
                print(f1)

        for j in songFile:   
                j.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(j.filename)))
                f2 = path+'/'+secure_filename(j.filename)
                print(f2)
                   
        for i in videoMeta: 
                   print(i)
                   i.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(i.filename)))
                   f3 = path+'/'+secure_filename(i.filename)
                   print(f3)

        for i in videoFile:  
                   print(i)
                   i.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(i.filename)))
                   f4 = path+'/'+secure_filename(i.filename)
                   print(f4)

        for i in imageMeta:  
                   print(i)
                   i.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(i.filename)))
                   f5 = path+'/'+secure_filename(i.filename)
                   print(f5)

        for i in imageFile:  
                   print(i)
                   i.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(i.filename)))
                   f6 = path+'/'+secure_filename(i.filename)
                   print(f6)

        insertRow(user,org,f1,f2,f3,f4,f5,f6)       
        value = 'Successfully Uploaded'   
        return render_template('web_app.html', data = value)


# routing request to view page
@app.route('/view')
def viewHome():
    return render_template('view.html')


#routing request to fetch all records and display   
@app.route('/viewed', methods = ['POST','GET'])
def display_details():
    global sender_path
    if request.method == 'POST':
        user = request.form['PName']
        org = request.form['OName']
        Data = fetchRecords(user,org)
        print(Data)
        sender_path = UPLOAD_FOLDER+org+'/'+user+'/'
        print(sender_path)
        return render_template('view.html', data=Data)

#routing request to download or return file... 
@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = sender_path+filename
    print(file_path)
    return send_file(file_path, as_attachment=True, attachment_filename='')



if __name__ == '__main__':
    #checking for connectivity
    connect_db(r'Sqlite_python.db')

    #creating table if not exists
    create_table()

    #running the API..
    app.run()
    
    
