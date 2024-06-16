class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left  = None      #единица      
        self.__right  = None    #нуль
    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, left):
        self.__left = left 
     
    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, right):
        self.__right = right 
 
class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        counter = root                    #инициализация бегунка корнем дерева
             
        #в цикле - прохождение по переданному списку. В списке значений: каждое значение имеет позицию соответствующую индексу 
        #одного из объектов. То есть нулевая позиция соответствует объекту с индексом ноль
        #т.е. для трех головных объектов список [1, 1, 0] - означает:
        # Объект с индексом ноль = 1 (выбрать значение истины. Истина это левая ветка - self.__left)
        # Объект с индексом один = 1 (выбрать значение истины. Истина это левая ветка - self.__left)
        # Объект с индексом два = 0 (выбрать значение лжи. Ложь это правая ветка - self.__right)
        # Ветка - это переменная со значением другого объекта (у которого также могут быть две переменные для других объектов)
        #
        #Алгоритм прохождения по ветвям (по объектам)
        #
        #0 Берется объект (головной) и записывается в бегунок
        #1 По индексу объекта определяется значение в списке. Для объекта с индексом 0, нужно взять x[0]
        # это записывается в meaning - это значение для выбранного объекта 
        #2.1 Если meaning истина, то надо брать counter.left (ветка истины - левая ветка бегунка). 
        # Здесь же проверяется есть ли в объекте ветка истины или объект это конец дерева (добраться до конца дерева = получить ответ)
        
        #2.2 Если meaning ложь, то надо брать counter.right (ветка лжи - правая ветка бегунка).
        # и проверка есть ли в объекте ветка лжи
        
        #3 При выполнении одного из условий, происходит присвоение бегунку следующего объекта, который находился в нужной ветке предыдущего 
        # алгоритм повторяется до того момента, когда для значения (истина/ложь) бегунка (объекта бегунка) не будет для соответствующей переменной нового объекта 
        # значит конец достигнут и рассматриваемый объект и есть ответ
        for i in x:                       
            meaning = x[counter.indx]     #
            if meaning and counter.left is not None:
                counter = counter.left
            elif meaning == 0 and counter.right is not None:
                counter = counter.right
        return counter.value
            
            
    
    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if obj.indx != 0:                            #проверка, что не корень
            if left is True: 
                node.left = obj                      #Запись объекта как истины для его родителя
            else:
                node.right = obj                     #Запись объекта как лжи для его родителя
        return obj                                   #Возврат, чтобы использовать объект как родителя для других 
    
 
 
 
root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "X"), v_11)
DecisionTree.add_obj(TreeObj(-1, "Y"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "A"), v_12)
DecisionTree.add_obj(TreeObj(-1, "B"), v_12, False)
 
x = [0, 1, 1]
res = DecisionTree.predict(root, x) 
print(res)
