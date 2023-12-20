import hashlib

with open("123.jpg","rb") as f:
	image=f.read()
result= hashlib.sha3_256(image)
print("hash for naruto icon:",result.hexdigest())