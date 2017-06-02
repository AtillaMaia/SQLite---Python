from database import Database

if __name__ == "__main__":
	
	db = Database()
	db.connect()
	db.disconnect()
	db.create_table()
	db.connect()
	db.insert_customer('Marcos', 'python', '11111111111', 'mcastrosouza@live.com')
	db.insert_customer('Thomas', 'javascript', '22222222222', 'thomas@gmail.com')
	db.search_customer('11111111111')
	db.remove_customer('22222222222')
	db.search_email('thomas@gmail.com')
	db.search_customer('11111111111')
