import pymysql
import numpy


class Speculate(object):
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
    def __del__(self):
        self.connect.close()
        self.cursor.close()

    # 中位数计算
    @staticmethod                 #静态方法
    def __medianCalculation(data: dict):
        dataList = []
        if data is not None:
            for var in data:
                dataList.append(var['avg_salary'])
            return numpy.median(dataList)
        return None

    # 岗位名称、职业技能合理性检测
    def __reasonableCheck(self, name, skill: list):

        sql = '''
                select num from handled_data
                where name like %s
                and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)
            '''
        try:
            result = self.cursor.execute(sql, (name, skill[0], skill[1], skill[2], skill[3], skill[4]))
            self.connect.commit()
            if result == 0:
                return False
            else:
                return True
        except Exception as e:
            self.connect.rollback()
            print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)

    @staticmethod
    # 获取查询语句
    def __sqlChoose(lan):

        sql_0 = []
        sql_1 = []
        sql_2 = []
        sql_3 = []
        if lan == 'Java':
            sql_0 = '''
                    select avg_salary from java_data
                    where city = %s and area = %s 
                    and scale = %s and education = %s and experience = %s
                    and name like %s
                    and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                    order by avg_salary    
                '''
            sql_1 = '''
                    select avg_salary from java_data
                    where city = %s 
                    and scale = %s and education = %s and experience = %s
                    and name like %s
                    and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                    order by avg_salary    
                '''
            sql_2 = '''
                    select avg_salary from java_data 
                    where scale = %s and education = %s and experience = %s
                    and name like %s
                    and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                    order by avg_salary    
                '''
            sql_3 = '''
                    select avg_salary from java_data
                    where education = %s and experience = %s
                    and name like %s
                    and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                    order by avg_salary    
                '''
        elif lan == 'Python':
            sql_0 = '''
                        select avg_salary from python_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from python_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from python_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from python_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == 'PHP':
            sql_0 = '''
                        select avg_salary from php_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from php_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from php_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from php_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == 'C/C++':
            sql_0 = '''
                        select avg_salary from c_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from c_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from c_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from c_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == 'C#/.NET':
            sql_0 = '''
                        select avg_salary from c23_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from c23_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from c23_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from c23_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == 'Unity3D/UE':
            sql_0 = '''
                        select avg_salary from u3due_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from u3due_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from u3due_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from u3due_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == 'IOS':
            sql_0 = '''
                        select avg_salary from ios_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from ios_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from ios_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from ios_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == 'Android':
            sql_0 = '''
                        select avg_salary from android_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from android_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from android_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from android_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == 'web前端':
            sql_0 = '''
                        select avg_salary from web_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from web_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from web_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from web_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == '算法':
            sql_0 = '''
                        select avg_salary from algorithm_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from algorithm_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from algorithm_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from algorithm_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == '测试':
            sql_0 = '''
                        select avg_salary from test_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from test_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from test_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from test_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        elif lan == '运维':
            sql_0 = '''
                        select avg_salary from oam_data
                        where city = %s and area = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_1 = '''
                        select avg_salary from oam_data
                        where city = %s 
                        and scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_2 = '''
                        select avg_salary from oam_data 
                        where scale = %s and education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
            sql_3 = '''
                        select avg_salary from oam_data
                        where education = %s and experience = %s
                        and name like %s
                        and(skill like %s or skill like %s or skill like %s or skill like %s or skill like %s)  
                        order by avg_salary    
                    '''
        else:
            return None

        return sql_0, sql_1, sql_2, sql_3

    def salarySpeculate(self, city, area, lan, scale, education, experience, skill: list, name):

        # 名称处理
        name = "%" + name + "%"

        # 特殊处理。。。
        if education == '中技':
            experience = experience + '/中专'

        # 技能数大于5个则删除多余部分
        if len(skill) > 5:
            skill = skill[1:6]

        # 若要求技能数小于5个，则将缺少的部分填充为第一个元素
        while 0 < len(skill) < 5:
            skill.append(skill[0])

        if len(skill) != 0:
            skill[0] = "%" + skill[0] + "%"
            skill[1] = "%" + skill[1] + "%"
            skill[2] = "%" + skill[2] + "%"
            skill[3] = "%" + skill[3] + "%"
            skill[4] = "%" + skill[4] + "%"

        # 获取sql
        sql_0, sql_1, sql_2, sql_3 = self.__sqlChoose(lan=lan)

        Flag = self.__reasonableCheck(name=name, skill=skill)

        if Flag is True:
            try:
                result = self.cursor.execute(sql_0, (city, area, scale, education, experience, name,
                                                     skill[0], skill[1], skill[2], skill[3], skill[4]))
                self.connect.commit()
                data = self.cursor.fetchall()
                if result == 0:
                    result = self.cursor.execute(sql_1, (city, scale, education, experience, name,
                                                         skill[0], skill[1], skill[2], skill[3], skill[4]))
                    self.connect.commit()
                    data = self.cursor.fetchall()
                    if result == 0:
                        result = self.cursor.execute(sql_2, (scale, education, experience, name,
                                                             skill[0], skill[1], skill[2], skill[3], skill[4]))
                        self.connect.commit()
                        data = self.cursor.fetchall()
                        if result == 0:
                            result = self.cursor.execute(sql_3, (education, experience, name,
                                                                 skill[0], skill[1], skill[2], skill[3], skill[4]))
                            self.connect.commit()
                            data = self.cursor.fetchall()
                            if result == 0:
                                return None
                            else:
                                return self.__medianCalculation(data)
                        else:
                            return self.__medianCalculation(data)
                    else:
                        return self.__medianCalculation(data)
                else:
                    return self.__medianCalculation(data)

            except Exception as e:
                self.connect.rollback()
                print(">>>读取数据失败 执行MySQL: {} 时出错：{}", e)
        else:
            return None
