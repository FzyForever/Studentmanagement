from bll import StudentManagerController
from model import StudentModel


class StudentManagerView:
    """
    界面视图类
    """
    def __init__(self):
        self.__manager=StudentManagerController()

    def __input_int(self,msg):
        while True:
            try:
                return int(input(msg))
            except:
                print("你的输入有误")


    def __input_students(self):
        stu = StudentModel()
        stu.name=input("请输入学生姓名:")
        stu.age=self.__input_int("请输入学生年龄:")
        stu.score=self.__input_int("请输入学生成绩:")
        self.__manager.add_student(stu)

    def __output_students(self,list_target):
        """
        显示所有学生列表信息
        :return:
        """
        for stu in list_target:
            print("%d--%s--%d--%d"%(stu.id,stu.name,stu.age,stu.score))

    def __delete_student(self):
        id=self.__input_int("请输入学生编号:")
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")


    def __modify_student(self):
        stu=StudentModel()
        stu.id=self.__input_int("请输入学生编号:")
        stu.name=input("请输入要修改的学生名字:")
        stu.age=self.__input_int("请输入学生年龄:")
        stu.score=self.__input_int("请输入学生成绩:")
        if  self.__manager.update_student(stu):
            print("更新成功")
        else:
            print("更新失败")

    def __output_students_by_score(self):
        """
        按升序将所有学生成绩排序
        :return:
        """
        list_target=self.__manager.order_by_score()
        self.__output_students(list_target)


    def __display_menu(self):
        print("(1) 添加学生")
        print("(2) 显示学生")
        print("(3) 删除学生")
        print("(4) 修改学生")
        print("(5) 按照成绩升序排列")

    def __select_menu(self):
        num = input("请输入选项：")
        if num =="1":
            self.__input_students()
        elif num =="2":
            self.__output_students(self.__manager.list_stu)

        elif num =="3":
            self.__delete_student()

        elif num =="4":
            self.__modify_student()

        elif num =="5":
            self.__output_students_by_score()


    def main(self):
        """
        界面入口方法
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()