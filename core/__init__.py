import pymysql

# Django 6.0 要求 mysqlclient >= 2.2.1，PyMySQL 自报版本为 1.4.6，
# 这里伪装成满足要求的版本号以通过检查
pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.install_as_MySQLdb()