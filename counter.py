class Store:
    __item_count = 100

    @classmethod
    def addItem(cls, count):
        cls.__item_count += count

    @classmethod
    def issueItem(cls, count):
        cls.__item_count -= count

    @classmethod
    def getItemCount(cls):
        return cls.__item_count


counter1 = Store()
counter2 = Store()
counter1.addItem(2)
counter1.issueItem(1)
print(Store.getItemCount())


class Store:
    __item_count=100

   # @classmethod
    def addItem(self, count):
        self.__item_count +=count

  #  @classmethod
    def issueItem(self, count):
        self.__item_count -= count

   # @classmethod
    def getItemCount(self):
        return self.__item_count

counter1= Store()
counter2= Store()
counter1.addItem(2)
counter1.issueItem(1)
print(Store.getItemCount(counter2))

