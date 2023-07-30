import threading
import time
import numpy

class Singleton(object):
    '''
    1 单例模式: 单例模式是指：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
    单例模式的优点
    1、由于单例模式要求在全局内只有一个实例，因而可以节省比较多的内存空间；
    2、全局只有一个接入点，可以更好地进行数据同步控制，避免多重占用；3、单例可长驻内存，减少系统开销。

    单例模式的应用举例
    1、生成全局惟一的序列号；
    2、访问全局复用的惟一资源，如磁盘、总线等；
    3、单个对象占用的资源过多，如数据库等；
    4、系统全局统一管理，如Windows下的Task Manager；
    5、网站计数器。

    四、单例模式的缺点
    1、单例模式的扩展是比较困难的；
    2、赋于了单例以太多的职责，某种程度上违反单一职责原则（六大原则后面会讲到）;
    3、单例模式是并发协作软件模块中需要最先完成的，因而其不利于测试；4、单例模式在某种情况下会导致“资源瓶颈”。
    '''

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class Bus(Singleton):
    lock = threading.RLock()

    def send_data(self, data):
        self.lock.acquire()
        time.sleep(3)
        print("发送单例数据", data)
        self.lock.release()


class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.send_data(self.name)


class Burger:
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPricce(self, price):
        self.price = price

    def getName(self):
        return self.name


class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class spicyChickenBurer(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0
        

class Beverage():
    name = ""
    price = 0.0
    type = "Beverage"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 0.4


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

class drinkDecortor():
    def getName(self):
        pass

    def etPrice(self):
        pass


class iceDecorator(drinkDecortor):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " + ice"

    def getPrice(self):
        return self.beverage.getPrice() + 0.3


class suggerDecorator(drinkDecortor):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " + suger"

    def getPrice(self):
        return self.beverage.getPrice() + 0.5


if __name__ == "__main__":
    # # 单例模式
    # for i in range(3):
    #     print(f"开始解析数据：{i}")
    #     my_entity = VisitEntity()
    #     my_entity.setName("Entity_" + str(i))
    #     my_entity.start()

    # 装饰器模式
    # 常见场景，日志，公共权限校验、参数校验等 多层装饰器的调试和维护有比较大的困难。
    coke_cola = coke()
    ice_coke = iceDecorator(coke_cola)
    print(ice_coke.getPrice())
    print(ice_coke.getName())

    # 组合模式 优点：
    # 1、节点增加和减少是非常自由和方便的，这也是树形结构的一大特点；2、所有节点，不管是分支节点还是叶子结点，不管是调用一个结点，还是调用一个结点群，都是非常方便的。
