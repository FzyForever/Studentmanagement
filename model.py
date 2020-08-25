class StudentModel:
    """
     学生数据模型类
    """
    def __init__(self,id=0,name="",age=0,score=0):
        """

        :param id: 学生编号
        :param name:学生姓名
        :param age:学生年龄
        :param score:学生得分
        """
        self.id=id
        self.name=name
        self.age=age
        self.score=score
    @property
    def id(self):
        return  self.__id

    @id.setter
    def id(self,value):
        self.__id=value

    @property
    def name(self):
        return  self.__name

    @name.setter
    def name(self,value):
        self.__name=value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age=value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        self.__score=value