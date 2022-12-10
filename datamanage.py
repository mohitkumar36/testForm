from dbconfig import dbconfig

def checkEntry(name, address, age, batch):
	db = dbconfig()
	cursor = db.cursor()
	query = f"SELECT * FROM yoga.entries WHERE name = '{name}' AND address = '{address}' AND age = '{age}' AND batch = '{batch}'"
	cursor.execute(query)
	results = cursor.fetchall()

	if len(results)!=0:
		return True
	return False

def giveRegno():
    db = dbconfig()
    cursor = db.cursor()
    query = f"SELECT * FROM yoga.entries"
    cursor.execute(query)
    results = cursor.fetchall()
    return len(results)

def addEntry(name, address, age, batch):
	resNo = giveRegno()
	#print(resNo)
	resNo += 1
	if resNo != 1 and checkEntry(name, address, age, batch):
		return False
	#print("*************" * 5)
	# Add to db
	db = dbconfig()
	cursor = db.cursor()
	
	query = "INSERT INTO yoga.entries (reg_no, name, address, age, batch) values (%s, %s, %s, %s, %s)"
	val = (resNo, name, address, age, batch)
	cursor.execute(query, val)

	query = "INSERT INTO yoga.payment (reg_no, JAN, FEB, MAR, APRIL, MAY, JUN, JUL, AUG, SEPT, OCT, NOV, DECEM) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (resNo, "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0")
	cursor.execute(query, val)

	db.commit()

	return resNo

def doPayment(regNo, month):
	db = dbconfig()
	cursor = db.cursor()
	query = f"SELECT * FROM yoga.payment WHERE REG_NO = '{regNo}'"
	cursor.execute(query)
	results = cursor.fetchall()
	if len(results)==0:
		return False

	print(regNo, month)
	query = (f"UPDATE yoga.payment \nSET {month}='1' \nWHERE REG_NO ='{regNo}';")
	cursor.execute(query)
	db.commit()
	return True

def changeBatch(regNo, batch):
	db = dbconfig()
	cursor = db.cursor()
	query = f"SELECT * FROM yoga.payment WHERE REG_NO = '{regNo}'"
	cursor.execute(query)
	results = cursor.fetchall()
	if len(results)==0:
		return False

	print(regNo, batch)
	query = (f"UPDATE yoga.entries \nSET BATCH='{batch}' \nWHERE REG_NO ='{regNo}';")
	cursor.execute(query)
	db.commit()
	return True