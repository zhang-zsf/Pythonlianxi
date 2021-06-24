print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore'))
len('jhfdsjkfkskk')#1111111111111111111111111111111