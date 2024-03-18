class AddressManagement:  # 创建一个类
    def __init__(self):
        self.address = ""
        self.phone = ""
        self.name = ""

    def write_address(self, address):
        self.address = self.address + address
        with open('/文艺部/新建 文本文档.txt', 'a', encoding='utf-8') as fp:
            fp.write(self.address + '\n')
            fp.flush()

    def write_name(self, name):
        self.name = self.name + name
        with open('/文艺部/新建 文本文档.txt', 'a', encoding='utf-8') as fp:
            fp.write(self.name + '\n')
            fp.flush()

    def write_phone(self, phone):
        self.phone = self.phone + phone
        with open('/文艺部/新建 文本文档.txt', 'a', encoding='utf-8') as fp:
            fp.write(self.phone + '\n')
            fp.flush()


# 创建一个AddressManagement对象，并且赋值给address_manager
address_manager = AddressManagement()

# 使用write_address方法写入一个地址
address_manager.write_address("北京市朝阳区三里屯路1号")

# 使用write_name方法写入一个姓名
address_manager.write_name("张三")

# 使用write_phone方法写入一个电话号码
address_manager.write_phone("13800138000")

# 再次写入一个地址、姓名和电话号码
address_manager.write_address("上海市浦东新区世纪大道100号")
address_manager.write_name("李四")
address_manager.write_phone("13900139000")
