import pymysql      #将整个模块导入
from collections import Counter   #从某个模块导入某个函数
import json


# 数据库对象
class MySql(object):
    # 建立数据库链接
    def __init__(self):
        self.connect = pymysql.connect(host="127.0.0.1",
                                       port=3306,
                                       user="root",
                                       password="123456",
                                       database="spiderdatabase",
                                       charset="utf8")
        self.cursor = self.connect.cursor(cursor=pymysql.cursors.DictCursor)

    # 关闭链接
    def __del_(self):
        self.connect.close()
        self.cursor.close()

    # 手动关闭数据库链接
    def close(self):
        self.connect.close()
        self.cursor.close()

    '''============================================数据处理======================================================='''

    # 原始数据存储
    def saveData(self, job_name, job_place, job_company, job_scale, job_salary, job_education, job_experience,
                 job_label, job_skill, job_welfare,type):

        sql = '''
                insert into row_data(name,place,company,scale,salary,education,experience,label,skill,welfare,type)
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            '''
        try:
            self.cursor.execute(sql, (job_name, job_place, job_company, job_scale, job_salary, job_education,
                                      job_experience, job_label, job_skill, job_welfare,type))
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            print(">>>插入数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 原始数据存储
    def saveHandledData(self, name, city, area, detail, company, scale, salary_min, salary_max, salary_avg, education,
                        experience, label, skill, welfare):

        sql = '''
                insert into handled_data (name, city, area, detail, company, scale, min_salary, max_salary,
                                          avg_salary, education, experience, label, skill, welfare)
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            '''
        try:
            self.cursor.execute(sql, (name, city, area, detail, company, scale, salary_min, salary_max, salary_avg,
                                      education, experience, label, skill, welfare))
            self.connect.commit()
            print("【数据处理模块】===>SUCCESS！插入数据成功 执行MySQL打印 ")
            print((name, city, area, detail, company, scale, salary_min, salary_max, salary_avg,
                                      education, experience, label, skill, welfare))
        except Exception as e:
            self.connect.rollback()
            print(">>>插入数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readRowData(self):
        sql = '''
                select * from row_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取处理后表单
    def readHandledData(self):
        sql = '''
                select * from handled_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readAlgorithmData(self):
        sql = '''
                select * from algorithm_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readAndroidData(self):
        sql = '''
                select * from android_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readCData(self):
        sql = '''
                select * from c_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readC23Data(self):
        sql = '''
                select * from c23_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readIosData(self):
        sql = '''
                select * from ios_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readJavaData(self):
        sql = '''
                select * from java_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readOamData(self):
        sql = '''
                select * from oam_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readPhpData(self):
        sql = '''
                select * from php_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readPythonData(self):
        sql = '''
                select * from python_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readTestData(self):
        sql = '''
                select * from test_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readU3dueData(self):
        sql = '''
                select * from u3due_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 读取原始表单
    def readWebData(self):
        sql = '''
                select * from web_data
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            # 获取所有字段
            fields = self.cursor.fetchall()
            return fields
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 去除薪资为的实习岗位，便于计算

    '''================================================首页======================================================'''

    # 获取表数据量
    def getLastNum(self):
        sql = '''
                select num from handled_data
                where num = (select MAX(num) from handled_data)
            '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def getMaxSalary(self):
        sql = '''
                select max_salary from handled_data
                where max_salary = (select MAX(max_salary) from handled_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def getMinSalary(self):
        sql = '''
                select min_salary from handled_data
                where min_salary = (select MIN(min_salary) from handled_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 计算全部数据的平均薪资
    def getAllAvgSalary(self):
        sql = '''
                select avg_salary from handled_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询所有学历的薪资平均情况
    def getSalaryForEducation(self):
        sql_0 = '''
                select  edu from educationforsalary
        '''
        sql_1 = '''
                select AVG(min) from educationforsalary
                where edu = %s
        '''
        sql_2 = '''
                select AVG(max) from educationforsalary
                where edu = %s
        '''
        sql_3 = '''
                select AVG(avg) from educationforsalary
                where edu = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['edu'])
            edu = dict(Counter(education_list))
            for key in list(edu.keys()):
                if edu[key] < 26:
                    del edu[key]
                    continue
            edu_list = list(edu)
            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询总体学历
    def getEducation(self):
        sql = '''
                select education from handled_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            for key in list(edu.keys()):
                if edu[key] < 26:
                    del edu[key]
                    continue
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询总体经验与薪资关系
    def getSalaryForExperience(self):
        sql_0 = '''
                        select experience from experienceforsalary
                '''
        sql_1 = '''
                        select AVG(min_salary) from experienceforsalary
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from experienceforsalary
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from experienceforsalary
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 188:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询总体经验
    def getExperience(self):
        sql = '''
                select experience from handled_data
                       
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 188:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询总体城市情况情况
    def getCity(self):
        sql = '''
                select city from handled_data 
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            city = []
            for var in result:
                city.append(var['city'])
            return list(set(city))
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询所有岗位名称
    def getJobName(self):
        sql = '''
                select name from handled_data 
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            name = []
            for var in result:
                name.append(var['name'])
            return name
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 城市平均待遇
    def getSalaryForCity(self):

        city = self.getCity()
        sql = '''
                select AVG(salary) from salaryforcity
                where city = %s
          '''
        try:
            salary = []
            for var in city:
                self.cursor.execute(sql, var)
                self.connect.commit()
                result = self.cursor.fetchall()
                salary.append(result)

            salary_list = []
            for var in salary:
                for i in var:
                    salary_list.append(round(int(i['AVG(salary)'])))

            return json.dumps({'name': city, 'value': salary_list}, ensure_ascii=False)



        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 福利查询
    def getWelfare(self):
        sql = '''
                select welfare from handled_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            welfare = []
            for var in result:
                welfare.append(var['welfare'])
            return welfare

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    '''================================================Java======================================================'''

    # 取得Java的岗位数量
    def javaGetNum(self):
        sql = '''
                select num from java_data
                 where num = (select MAX(num) from java_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得Java岗位的总体平均薪资
    def javaGetAvgSalary(self):
        sql = '''
                   select avg_salary from java_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def javaGetMaxSalary(self):
        sql = '''
                select max_salary from java_data
                where max_salary = (select MAX(max_salary) from java_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def javaGetMinSalary(self):
        sql = '''
                select min_salary from java_data
                where min_salary = (select MIN(min_salary) from java_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def javaGetEdu(self):
        sql = '''
                       select education from java_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询java经验要求
    def javaGetExp(self):
        sql = '''
                   select experience from java_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # java薪资与学历的关系
    def javaGetEduForSalary(self):
        sql_0 = '''
                select distinct education from java_data
        '''
        sql_1 = '''
                select AVG(min_salary) from java_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from java_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from java_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # java经验与薪资
    def javaGetExpForSalary(self):
        sql_0 = '''
                        select experience from java_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from java_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from java_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from java_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def javaGetSkill(self):
        sql = '''
                select skill from java_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def javaRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        javaSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        javaMin = float(self.javaGetMinSalary())
        javaMax = float(self.javaGetMaxSalary())
        javaAvg = float(self.javaGetAvgSalary())
        javaNum = float(self.javaGetNum())
        # 添加最低薪资分数
        javaSocre.append(javaMin / Min)
        # 添加最高薪资分数
        javaSocre.append(javaMax / Max)
        # 添加平均薪资分数
        javaSocre.append(javaAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from java_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from java_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            javaSocre.append(1 - (Exp / javaNum))
            # 添加学历分数
            javaSocre.append(Edu / javaNum)
            # 添加数量分
            javaSocre.append((javaNum / Num) * 100)
            return json.dumps({'name': 'Java', 'value': javaSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================python============================================='''

    def pythonGetNum(self):
        sql = '''
                select num from python_data
                 where num = (select MAX(num) from python_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得python岗位的总体平均薪资
    def pythonGetAvgSalary(self):
        sql = '''
                   select avg_salary from python_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def pythonGetMaxSalary(self):
        sql = '''
                select max_salary from python_data
                where max_salary = (select MAX(max_salary) from python_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def pythonGetMinSalary(self):
        sql = '''
                select min_salary from python_data
                where min_salary = (select MIN(min_salary) from python_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def pythonGetEdu(self):
        sql = '''
                       select education from python_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询java经验要求
    def pythonGetExp(self):
        sql = '''
                   select experience from python_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # java薪资与学历的关系
    def pythonGetEduForSalary(self):
        sql_0 = '''
                select distinct education from python_data
        '''
        sql_1 = '''
                select AVG(min_salary) from python_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from python_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from python_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # java经验与薪资
    def pythonGetExpForSalary(self):
        sql_0 = '''
                        select experience from python_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from python_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from python_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from python_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def pythonGetSkill(self):
        sql = '''
                select skill from python_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def pythonRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        pythonSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        pythonMin = float(self.pythonGetMinSalary())
        pythonMax = float(self.pythonGetMaxSalary())
        pythonAvg = float(self.pythonGetAvgSalary())
        pythonNum = float(self.pythonGetNum())
        # 添加最低薪资分数
        pythonSocre.append(pythonMin / Min)
        # 添加最高薪资分数
        pythonSocre.append(pythonMax / Max)
        # 添加平均薪资分数
        pythonSocre.append(pythonAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from python_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from python_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            pythonSocre.append(1 - (Exp / pythonNum))
            # 添加学历分数
            pythonSocre.append(Edu / pythonNum)
            # 添加数量分
            pythonSocre.append((pythonNum / Num) * 100)
            return json.dumps({'name': 'Python', 'value': pythonSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================C============================================='''

    def cGetNum(self):
        sql = '''
                select num from c_data
                 where num = (select MAX(num) from c_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得c岗位的总体平均薪资
    def cGetAvgSalary(self):
        sql = '''
                   select avg_salary from c_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def cGetMaxSalary(self):
        sql = '''
                select max_salary from c_data
                where max_salary = (select MAX(max_salary) from c_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def cGetMinSalary(self):
        sql = '''
                select min_salary from c_data
                where min_salary = (select MIN(min_salary) from c_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def cGetEdu(self):
        sql = '''
                       select education from c_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询java经验要求
    def cGetExp(self):
        sql = '''
                   select experience from c_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 11:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # java薪资与学历的关系
    def cGetEduForSalary(self):
        sql_0 = '''
                select distinct education from c_data
        '''
        sql_1 = '''
                select AVG(min_salary) from c_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from c_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from c_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # java经验与薪资
    def cGetExpForSalary(self):
        sql_0 = '''
                        select experience from c_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from c_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from c_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from c_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 11:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def cGetSkill(self):
        sql = '''
                select skill from c_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def cRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        cSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        cMin = float(self.cGetMinSalary())
        cMax = float(self.cGetMaxSalary())
        cAvg = float(self.cGetAvgSalary())
        cNum = float(self.cGetNum())
        # 添加最低薪资分数
        cSocre.append(cMin / Min)
        # 添加最高薪资分数
        cSocre.append(cMax / Max)
        # 添加平均薪资分数
        cSocre.append(cAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from c_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from c_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            cSocre.append(1 - (Exp / cNum))
            # 添加学历分数
            cSocre.append(Edu / cNum)
            # 添加数量分
            cSocre.append((cNum / Num) * 100)
            return json.dumps({'name': 'c', 'value': cSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================c23============================================='''

    def c23GetNum(self):
        sql = '''
                select num from c23_data
                 where num = (select MAX(num) from c23_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得c23岗位的总体平均薪资
    def c23GetAvgSalary(self):
        sql = '''
                   select avg_salary from c23_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def c23GetMaxSalary(self):
        sql = '''
                select max_salary from c23_data
                where max_salary = (select MAX(max_salary) from c23_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def c23GetMinSalary(self):
        sql = '''
                select min_salary from c23_data
                where min_salary = (select MIN(min_salary) from c23_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def c23GetEdu(self):
        sql = '''
                       select education from c23_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询java经验要求
    def c23GetExp(self):
        sql = '''
                   select experience from c23_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # java薪资与学历的关系
    def c23GetEduForSalary(self):
        sql_0 = '''
                select distinct education from c23_data
        '''
        sql_1 = '''
                select AVG(min_salary) from c23_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from c23_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from c23_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # java经验与薪资
    def c23GetExpForSalary(self):
        sql_0 = '''
                        select experience from c23_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from c23_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from c23_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from c23_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def c23GetSkill(self):
        sql = '''
                select skill from c23_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def c23Radar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        c23Socre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        c23Min = float(self.c23GetMinSalary())
        c23Max = float(self.c23GetMaxSalary())
        c23Avg = float(self.c23GetAvgSalary())
        c23Num = float(self.c23GetNum())
        # 添加最低薪资分数
        c23Socre.append(c23Min / Min)
        # 添加最高薪资分数
        c23Socre.append(c23Max / Max)
        # 添加平均薪资分数
        c23Socre.append(c23Avg / Avg)

        sql_1 = '''
                    select COUNT(num) from c23_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from c23_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            c23Socre.append(1 - (Exp / c23Num))
            # 添加学历分数
            c23Socre.append(Edu / c23Num)
            # 添加数量分
            c23Socre.append((c23Num / Num) * 100)
            return json.dumps({'name': 'c23', 'value': c23Socre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================u3dUe============================================='''

    def u3dUeGetNum(self):
        sql = '''
                select num from u3dUe_data
                 where num = (select MAX(num) from u3dUe_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得u3dUe岗位的总体平均薪资
    def u3dUeGetAvgSalary(self):
        sql = '''
                   select avg_salary from u3dUe_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def u3dUeGetMaxSalary(self):
        sql = '''
                select max_salary from u3dUe_data
                where max_salary = (select MAX(max_salary) from u3dUe_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def u3dUeGetMinSalary(self):
        sql = '''
                select min_salary from u3dUe_data
                where min_salary = (select MIN(min_salary) from u3dUe_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def u3dUeGetEdu(self):
        sql = '''
                       select education from u3dUe_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询java经验要求
    def u3dUeGetExp(self):
        sql = '''
                   select experience from u3dUe_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # java薪资与学历的关系
    def u3dUeGetEduForSalary(self):
        sql_0 = '''
                select distinct education from u3dUe_data
        '''
        sql_1 = '''
                select AVG(min_salary) from u3dUe_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from u3dUe_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from u3dUe_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # java经验与薪资
    def u3dUeGetExpForSalary(self):
        sql_0 = '''
                        select experience from u3dUe_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from u3dUe_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from u3dUe_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from u3dUe_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def u3dUeGetSkill(self):
        sql = '''
                select skill from u3dUe_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def u3dUeRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        u3dUeSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        u3dUeMin = float(self.u3dUeGetMinSalary())
        u3dUeMax = float(self.u3dUeGetMaxSalary())
        u3dUeAvg = float(self.u3dUeGetAvgSalary())
        u3dUeNum = float(self.u3dUeGetNum())
        # 添加最低薪资分数
        u3dUeSocre.append(u3dUeMin / Min)
        # 添加最高薪资分数
        u3dUeSocre.append(u3dUeMax / Max)
        # 添加平均薪资分数
        u3dUeSocre.append(u3dUeAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from u3dUe_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from u3dUe_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            u3dUeSocre.append(1 - (Exp / u3dUeNum))
            # 添加学历分数
            u3dUeSocre.append(Edu / u3dUeNum)
            # 添加数量分
            u3dUeSocre.append((u3dUeNum / Num) * 100)
            return json.dumps({'name': 'u3dUe', 'value': u3dUeSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================php============================================='''

    def phpGetNum(self):
        sql = '''
                select num from php_data
                 where num = (select MAX(num) from php_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得php岗位的总体平均薪资
    def phpGetAvgSalary(self):
        sql = '''
                   select avg_salary from php_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def phpGetMaxSalary(self):
        sql = '''
                select max_salary from php_data
                where max_salary = (select MAX(max_salary) from php_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def phpGetMinSalary(self):
        sql = '''
                select min_salary from php_data
                where min_salary = (select MIN(min_salary) from php_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def phpGetEdu(self):
        sql = '''
                       select education from php_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询经验要求
    def phpGetExp(self):
        sql = '''
                   select experience from php_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 薪资与学历的关系
    def phpGetEduForSalary(self):
        sql_0 = '''
                select distinct education from php_data
        '''
        sql_1 = '''
                select AVG(min_salary) from php_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from php_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from php_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 经验与薪资
    def phpGetExpForSalary(self):
        sql_0 = '''
                        select experience from php_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from php_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from php_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from php_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def phpGetSkill(self):
        sql = '''
                select skill from php_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def phpRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        phpSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        phpMin = float(self.phpGetMinSalary())
        phpMax = float(self.phpGetMaxSalary())
        phpAvg = float(self.phpGetAvgSalary())
        phpNum = float(self.phpGetNum())
        # 添加最低薪资分数
        phpSocre.append(phpMin / Min)
        # 添加最高薪资分数
        phpSocre.append(phpMax / Max)
        # 添加平均薪资分数
        phpSocre.append(phpAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from php_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from php_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            phpSocre.append(1 - (Exp / phpNum))
            # 添加学历分数
            phpSocre.append(Edu / phpNum)
            # 添加数量分
            phpSocre.append((phpNum / Num) * 100)
            return json.dumps({'name': 'php', 'value': phpSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================web============================================='''

    def webGetNum(self):
        sql = '''
                select num from web_data
                 where num = (select MAX(num) from web_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得web岗位的总体平均薪资
    def webGetAvgSalary(self):
        sql = '''
                   select avg_salary from web_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def webGetMaxSalary(self):
        sql = '''
                select max_salary from web_data
                where max_salary = (select MAX(max_salary) from web_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def webGetMinSalary(self):
        sql = '''
                select min_salary from web_data
                where min_salary = (select MIN(min_salary) from web_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def webGetEdu(self):
        sql = '''
                       select education from web_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询经验要求
    def webGetExp(self):
        sql = '''
                   select experience from web_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 薪资与学历的关系
    def webGetEduForSalary(self):
        sql_0 = '''
                select distinct education from web_data
        '''
        sql_1 = '''
                select AVG(min_salary) from web_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from web_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from web_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 经验与薪资
    def webGetExpForSalary(self):
        sql_0 = '''
                        select experience from web_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from web_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from web_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from web_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def webGetSkill(self):
        sql = '''
                select skill from web_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def webRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        webSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        webMin = float(self.webGetMinSalary())
        webMax = float(self.webGetMaxSalary())
        webAvg = float(self.webGetAvgSalary())
        webNum = float(self.webGetNum())
        # 添加最低薪资分数
        webSocre.append(webMin / Min)
        # 添加最高薪资分数
        webSocre.append(webMax / Max)
        # 添加平均薪资分数
        webSocre.append(webAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from web_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from web_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            webSocre.append(1 - (Exp / webNum))
            # 添加学历分数
            webSocre.append(Edu / webNum)
            # 添加数量分
            webSocre.append((webNum / Num) * 100)
            return json.dumps({'name': 'web', 'value': webSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================Android============================================='''

    def AndroidGetNum(self):
        sql = '''
                select num from Android_data
                 where num = (select MAX(num) from Android_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得Android岗位的总体平均薪资
    def AndroidGetAvgSalary(self):
        sql = '''
                   select avg_salary from Android_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def AndroidGetMaxSalary(self):
        sql = '''
                select max_salary from Android_data
                where max_salary = (select MAX(max_salary) from Android_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def AndroidGetMinSalary(self):
        sql = '''
                select min_salary from Android_data
                where min_salary = (select MIN(min_salary) from Android_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def AndroidGetEdu(self):
        sql = '''
                       select education from Android_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询经验要求
    def AndroidGetExp(self):
        sql = '''
                   select experience from Android_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 薪资与学历的关系
    def AndroidGetEduForSalary(self):
        sql_0 = '''
                select distinct education from Android_data
        '''
        sql_1 = '''
                select AVG(min_salary) from Android_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from Android_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from Android_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 经验与薪资
    def AndroidGetExpForSalary(self):
        sql_0 = '''
                        select experience from Android_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from Android_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from Android_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from Android_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def AndroidGetSkill(self):
        sql = '''
                select skill from Android_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def AndroidRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        AndroidSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        AndroidMin = float(self.AndroidGetMinSalary())
        AndroidMax = float(self.AndroidGetMaxSalary())
        AndroidAvg = float(self.AndroidGetAvgSalary())
        AndroidNum = float(self.AndroidGetNum())
        # 添加最低薪资分数
        AndroidSocre.append(AndroidMin / Min)
        # 添加最高薪资分数
        AndroidSocre.append(AndroidMax / Max)
        # 添加平均薪资分数
        AndroidSocre.append(AndroidAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from Android_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from Android_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            AndroidSocre.append(1 - (Exp / AndroidNum))
            # 添加学历分数
            AndroidSocre.append(Edu / AndroidNum)
            # 添加数量分
            AndroidSocre.append((AndroidNum / Num) * 100)
            return json.dumps({'name': 'Android', 'value': AndroidSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================ios============================================='''

    def iosGetNum(self):
        sql = '''
                select num from ios_data
                 where num = (select MAX(num) from ios_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得ios岗位的总体平均薪资
    def iosGetAvgSalary(self):
        sql = '''
                   select avg_salary from ios_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def iosGetMaxSalary(self):
        sql = '''
                select max_salary from ios_data
                where max_salary = (select MAX(max_salary) from ios_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def iosGetMinSalary(self):
        sql = '''
                select min_salary from ios_data
                where min_salary = (select MIN(min_salary) from ios_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def iosGetEdu(self):
        sql = '''
                       select education from ios_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询经验要求
    def iosGetExp(self):
        sql = '''
                   select experience from ios_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 薪资与学历的关系
    def iosGetEduForSalary(self):
        sql_0 = '''
                select distinct education from ios_data
        '''
        sql_1 = '''
                select AVG(min_salary) from ios_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from ios_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from ios_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 经验与薪资
    def iosGetExpForSalary(self):
        sql_0 = '''
                        select experience from ios_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from ios_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from ios_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from ios_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def iosGetSkill(self):
        sql = '''
                select skill from ios_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def iosRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        iosSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        iosMin = float(self.iosGetMinSalary())
        iosMax = float(self.iosGetMaxSalary())
        iosAvg = float(self.iosGetAvgSalary())
        iosNum = float(self.iosGetNum())
        # 添加最低薪资分数
        iosSocre.append(iosMin / Min)
        # 添加最高薪资分数
        iosSocre.append(iosMax / Max)
        # 添加平均薪资分数
        iosSocre.append(iosAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from ios_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from ios_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            iosSocre.append(1 - (Exp / iosNum))
            # 添加学历分数
            iosSocre.append(Edu / iosNum)
            # 添加数量分
            iosSocre.append((iosNum / Num) * 100)
            return json.dumps({'name': 'ios', 'value': iosSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================algorithm============================================='''

    def algorithmGetNum(self):
        sql = '''
                select num from algorithm_data
                 where num = (select MAX(num) from algorithm_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得algorithm岗位的总体平均薪资
    def algorithmGetAvgSalary(self):
        sql = '''
                   select avg_salary from algorithm_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def algorithmGetMaxSalary(self):
        sql = '''
                select max_salary from algorithm_data
                where max_salary = (select MAX(max_salary) from algorithm_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def algorithmGetMinSalary(self):
        sql = '''
                select min_salary from algorithm_data
                where min_salary = (select MIN(min_salary) from algorithm_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def algorithmGetEdu(self):
        sql = '''
                       select education from algorithm_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询经验要求
    def algorithmGetExp(self):
        sql = '''
                   select experience from algorithm_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 薪资与学历的关系
    def algorithmGetEduForSalary(self):
        sql_0 = '''
                select distinct education from algorithm_data
        '''
        sql_1 = '''
                select AVG(min_salary) from algorithm_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from algorithm_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from algorithm_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 经验与薪资
    def algorithmGetExpForSalary(self):
        sql_0 = '''
                        select experience from algorithm_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from algorithm_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from algorithm_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from algorithm_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def algorithmGetSkill(self):
        sql = '''
                select skill from algorithm_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def algorithmRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        algorithmSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        algorithmMin = float(self.algorithmGetMinSalary())
        algorithmMax = float(self.algorithmGetMaxSalary())
        algorithmAvg = float(self.algorithmGetAvgSalary())
        algorithmNum = float(self.algorithmGetNum())
        # 添加最低薪资分数
        algorithmSocre.append(algorithmMin / Min)
        # 添加最高薪资分数
        algorithmSocre.append(algorithmMax / Max)
        # 添加平均薪资分数
        algorithmSocre.append(algorithmAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from algorithm_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from algorithm_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            algorithmSocre.append(1 - (Exp / algorithmNum))
            # 添加学历分数
            algorithmSocre.append(Edu / algorithmNum)
            # 添加数量分
            algorithmSocre.append((algorithmNum / Num) * 100)
            return json.dumps({'name': 'algorithm', 'value': algorithmSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================test============================================='''

    def testGetNum(self):
        sql = '''
                select num from test_data
                 where num = (select MAX(num) from test_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得test岗位的总体平均薪资
    def testGetAvgSalary(self):
        sql = '''
                   select avg_salary from test_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def testGetMaxSalary(self):
        sql = '''
                select max_salary from test_data
                where max_salary = (select MAX(max_salary) from test_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def testGetMinSalary(self):
        sql = '''
                select min_salary from test_data
                where min_salary = (select MIN(min_salary) from test_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def testGetEdu(self):
        sql = '''
                       select education from test_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询经验要求
    def testGetExp(self):
        sql = '''
                   select experience from test_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 50:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 薪资与学历的关系
    def testGetEduForSalary(self):
        sql_0 = '''
                select distinct education from test_data
        '''
        sql_1 = '''
                select AVG(min_salary) from test_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from test_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from test_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 经验与薪资
    def testGetExpForSalary(self):
        sql_0 = '''
                        select experience from test_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from test_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from test_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from test_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 50:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def testGetSkill(self):
        sql = '''
                select skill from test_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def testRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        testSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        testMin = float(self.testGetMinSalary())
        testMax = float(self.testGetMaxSalary())
        testAvg = float(self.testGetAvgSalary())
        testNum = float(self.testGetNum())
        # 添加最低薪资分数
        testSocre.append(testMin / Min)
        # 添加最高薪资分数
        testSocre.append(testMax / Max)
        # 添加平均薪资分数
        testSocre.append(testAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from test_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from test_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            testSocre.append(1 - (Exp / testNum))
            # 添加学历分数
            testSocre.append(Edu / testNum)
            # 添加数量分
            testSocre.append((testNum / Num) * 100)
            return json.dumps({'name': 'test', 'value': testSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    '''============================================oam============================================='''

    def oamGetNum(self):
        sql = '''
                select num from oam_data
                 where num = (select MAX(num) from oam_data)
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            last_num = result['num']
            return last_num
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得oam岗位的总体平均薪资
    def oamGetAvgSalary(self):
        sql = '''
                   select avg_salary from oam_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            salary_list = []
            for var in result:
                salary_list.append(var['avg_salary'])
            avg = 0
            for var in salary_list:
                avg = avg + var
            return format(avg / len(salary_list), '.2f')
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最高薪资
    def oamGetMaxSalary(self):
        sql = '''
                select max_salary from oam_data
                where max_salary = (select MAX(max_salary) from oam_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Max = result['max_salary']
            return Max
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询最低薪资
    def oamGetMinSalary(self):
        sql = '''
                select min_salary from oam_data
                where min_salary = (select MIN(min_salary) from oam_data)
            '''

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchone()
            Min = result['min_salary']
            return Min
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 取得java学历情况
    def oamGetEdu(self):
        sql = '''
                       select education from oam_data
               '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            education_list = []
            for var in result:
                education_list.append(var['education'])
            edu = dict(Counter(education_list))
            edu_name = []
            edu_value = []

            for var in edu:
                edu_name.append(var)
                edu_value.append(edu[var])

            return json.dumps({'name': edu_name, 'value': edu_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 查询经验要求
    def oamGetExp(self):
        sql = '''
                   select experience from oam_data
           '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 10:
                    del exp[key]
                    continue
            exp_name = []
            exp_value = []
            for var in exp:
                exp_name.append(var)
                exp_value.append(exp[var])

            return json.dumps({'name': exp_name, 'value': exp_value}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    # 薪资与学历的关系
    def oamGetEduForSalary(self):
        sql_0 = '''
                select distinct education from oam_data
        '''
        sql_1 = '''
                select AVG(min_salary) from oam_data
                where education = %s
        '''
        sql_2 = '''
                select AVG(max_salary) from oam_data
                where education = %s
        '''
        sql_3 = '''
                select AVG(avg_salary) from oam_data
                where education = %s
        '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            edu = self.cursor.fetchall()
            edu_list = []
            for var in edu:
                edu_list.append(var['education'])

            # 最小值处理
            min_salary = []
            for var in edu_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in edu_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in edu_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(edu)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': edu_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 经验与薪资
    def oamGetExpForSalary(self):
        sql_0 = '''
                        select experience from oam_data
                '''
        sql_1 = '''
                        select AVG(min_salary) from oam_data
                        where experience = %s
                '''
        sql_2 = '''
                        select AVG(max_salary) from oam_data
                        where experience = %s
                '''
        sql_3 = '''
                        select AVG(avg_salary) from oam_data
                        where experience = %s
                '''
        try:
            self.cursor.execute(sql_0)
            self.connect.commit()
            result = self.cursor.fetchall()
            experience_list = []
            for var in result:
                experience_list.append(var['experience'])
            exp = dict(Counter(experience_list))
            for key in list(exp.keys()):
                if exp[key] < 50:
                    del exp[key]
                    continue
            exp_list = list(exp)

            # 最小值处理
            min_salary = []
            for var in exp_list:
                self.cursor.execute(sql_1, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                min_salary.append(data)

            min_list = []
            for i in min_salary:
                for j in i:
                    min_list.append(round(float(j['AVG(min_salary)']), 2))

            # 最大值
            max_salary = []
            for var in exp_list:
                self.cursor.execute(sql_2, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                max_salary.append(data)

            max_list = []
            for i in max_salary:
                for j in i:
                    max_list.append(round(float(j['AVG(max_salary)']), 2))

            # 平均值
            avg_salary = []
            for var in exp_list:
                self.cursor.execute(sql_3, var)
                self.connect.commit()
                data = self.cursor.fetchall()
                avg_salary.append(data)

            avg_list = []
            for i in avg_salary:
                for j in i:
                    avg_list.append(round(float(j['AVG(avg_salary)']), 2))

            # 整合
            salary_list = []
            for i in range(len(exp_list)):
                data = [min_list[i], avg_list[i], max_list[i]]
                salary_list.append(data)

            return json.dumps({'name': exp_list, 'value': salary_list}, ensure_ascii=False)

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 ：{}".format(e))

    # 查询技术要求
    def oamGetSkill(self):
        sql = '''
                select skill from oam_data
        '''
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            result = self.cursor.fetchall()
            skill = []
            for var in result:
                skill.append(var['skill'])
            return skill

        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}".format(sql, e))

    def oamRadar(self):
        # 分数： 最低薪资分（10分） 最高薪资分  平均薪资分  经验分  学历分  数量分
        oamSocre = []
        Min = float(self.getMinSalary())
        Max = float(self.getMaxSalary())
        Avg = float(self.getAllAvgSalary())
        Num = float(self.getLastNum())
        oamMin = float(self.oamGetMinSalary())
        oamMax = float(self.oamGetMaxSalary())
        oamAvg = float(self.oamGetAvgSalary())
        oamNum = float(self.oamGetNum())
        # 添加最低薪资分数
        oamSocre.append(oamMin / Min)
        # 添加最高薪资分数
        oamSocre.append(oamMax / Max)
        # 添加平均薪资分数
        oamSocre.append(oamAvg / Avg)

        sql_1 = '''
                    select COUNT(num) from oam_data
                    where experience = '1-3年' or  experience ='经验不限' or  experience ='在校/应届'
            '''
        sql_2 = '''
                    select COUNT(num) from oam_data
                    where education = '博士' or  education = '硕士' or education = '本科'
            '''
        try:
            self.cursor.execute(sql_1)
            self.connect.commit()
            result = self.cursor.fetchone()
            Exp = result['COUNT(num)']
            self.cursor.execute(sql_2)
            self.connect.commit()
            result = self.cursor.fetchone()
            Edu = result['COUNT(num)']
            # 添加经验分数
            oamSocre.append(1 - (Exp / oamNum))
            # 添加学历分数
            oamSocre.append(Edu / oamNum)
            # 添加数量分
            oamSocre.append((oamNum / Num) * 100)
            return json.dumps({'name': 'oam', 'value': oamSocre}, ensure_ascii=False)
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)
