#encoding=utf-8
import hashlib
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def checkdata(data_str):
	checkData = hashlib.md5(data_str)
	has_data =  checkData.hexdigest()
	return has_data
