s = "я люблю динамическую типизацию!"
print(len(s.encode('cp1251')),"байт")
print(len(s.encode('utf8')),"байт")
print(len(s.encode('utf16')),"байт")
print(len(s.encode('utf32')),"байт")