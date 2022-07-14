import pymongo

nosql_conn = pymongo.MongoClient('mongodb://127.0.0.1:27017/')  # 1. Kết nối DB
mydb = nosql_conn['Nhanvien']                                   # 2. Khởi tạo hoặc gọi một Database
mycol = mydb["nhanvien"]                                        # 3. Khởi tạo hoặc gọi một Collection
print(mycol)

#Insert
# mydict = { "id_nhanvien": "2", "ten_nhanvien": "Huy", "cccd": "4228", "email": "huyle123@gmail.com","phone": "55411" }
# x = mycol.insert_one(mydict)

#Update
# myquery = { "id_nhanvien": "2" }
# newvalues = { "$set": { "phone": "55555" } }
# mycol.update_one(myquery, newvalues)


#Delete
# myquery = { "id_nhanvien": "2" }
# mycol.delete_one(myquery)

#print
for x in mycol.find():
  print(x)