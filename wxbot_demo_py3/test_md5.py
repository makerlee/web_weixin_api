import hashlib

md5file = open("D:\space4Py\web_weixin_api\wxbot_demo_py3\saved\msgimgs\img_6932378532631596267.jpg", 'rb')
md5 = hashlib.md5(md5file.read()).hexdigest()

md5file.close()

print(md5)

