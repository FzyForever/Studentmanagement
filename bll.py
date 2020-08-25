class StudentManagerController:
    """
    学生逻辑控制类
    """

    def __init__(self):
        self.__list_stu=[]

    @property
    def list_stu(self):
        return self.__list_stu

    def add_student(self,stu):
        """

        :param stu: 需要添加的学生对象
        :return:
        """
        stu.id=self.__generate_id()
        self.__list_stu.append(stu)

    def remove_student(self,id):
        """
            删除学生
          :param num:需要删除的学生编号
          :return:
        """
        # for stu in self.list_stu:
        #     if stu.id==id:
        #         del self.list_stu[id-1]
        for stu in self.list_stu:
            if stu.id==id:
                self.list_stu.remove(stu)
                return True #表示删除成功
            return False #表示删除失败

    def update_student(self,stu):
        for item in self.__list_stu:
            if stu.id==item.id:
                item.name=stu.name
                item.age=stu.age
                item.score=stu.score
                return True
        return False


    def __generate_id(self):
        """
       生成新的编号，比上次添加对象+1
        """
        # if len(self.__list_stu) > 0:
        #     id = self.__list_stu[-1].id+1
        # else:
        #     id=1
        # return id
        return self.__list_stu[-1].id+1 if len(self.__list_stu)>0 else 1

    def order_by_score(self):
        new_list=self.list_stu[:]
        for r in range(len(new_list) - 1):
            for c in range(r + 1, len(new_list)):
                if new_list[r].score > new_list[c].score:
                    new_list[r], new_list[c] = new_list[c], new_list[r]
        return new_list

