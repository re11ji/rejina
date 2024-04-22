import mysq1.connector
mydb=mysq1.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_database"
)
mycursor=mydb.cursor()

mycursor.execute("create table Emp(id int(10)primary key auto_increment,name varchar(120),address varchar(115),mail varchar(10),department varchar(100))")
print("table created successfully.")


sq1="insert into Emp(id,name,address,mail,phone,Department)values(%s,%s,%s,%s,%s,%s)"
val=[

    
     ('',"Mr.Lohar","Sonada","lohar1567@gmail.com","3698521473","finance"),
     ('',"Mr.rai","darjeeling","rai4561@gmail.com","7418529631","sales"),
     ('',"Mr.subba","kolkata","subba8521@gmail.com","8521479631","purchase"),
     ('',"Mr.Saroj","Siliguri","saroj3333@gmail.com","5676899076", "customercare")
     ('',"Mrs.Das","Mumbai","das4554@gmail.com","1234567890","sales")
     ('',"Mrs.paul","Delhi","paul4444@gmail.com","9087564312","accounts")
     ('',"Mrs.kapoor","Pune","kapoor1234@gmail.com","8909086754","Dealer")
    ]

mycursor.executemany(sq1,val)
mydb.commit()
print(mycursor.rowcount,"row\s added successfully.")
mycursor.execute("select*from Emp")
result = mycursor.fetcha11()
for t in result:
    print (t)

    sq1="update Emp set name=%s where name=%s"
    val=("Mr.Das","Mrs.Paul")
    mycursor.execute(sq1,val)
    print (mycursor.rowcount,"row\s affected.")