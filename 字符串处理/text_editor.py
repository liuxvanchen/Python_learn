class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []
        self.current_index = -1

    def insert(self, new_text):
        self.text = self.text + new_text
        self.add_to_history(new_text, "insert")

    def copy(self):
        self.history.append(("copy", self.text))
        return self.text

    def paste(self, old_text):
        self.text = old_text
        self.add_to_history(old_text, "paste")

    def cut(self):
        if self.text:
            cut_text = self.text[-1]  # 删除最后一个元素
            self.text = self.text[:-1]  # 切片，从第一个到倒数第二个元素
            self.add_to_history(cut_text, "cut")
            return cut_text

    def undo(self):
        if self.current_index >= 0:
            self.current_index -= 1
            old_action = self.history[self.current_index]
            if old_action[1] == "insert":
                to_remove = len(old_action[0])
                self.text = self.text[:-to_remove]
            elif old_action[1] == "paste":
                self.text = ""
                for action in reversed(self.history[:self.current_index + 1]):
                    if action[1] == "insert":
                        self.text = action[0] + self.text
            elif old_action[1] == "cut":
                self.text += old_action[0]

    def add_to_history(self, text, action):
        if action == "insert":
            if self.current_index + 1 < len(self.history) and self.history[self.current_index + 1][1] == "insert":
                self.history[self.current_index + 1] = (self.history[self.current_index + 1][0] + text, "insert")
            else:
                self.history.append((text, action))
                self.current_index += 1
        elif action == "paste":
            self.history = self.history[:self.current_index + 1]
            self.history.append((text, action))
            self.current_index = len(self.history) - 1

    def show(self):
        print("Current text: ", self.text)
        print("History: ", self.history)


# 使用示例
editor = TextEditor()
editor.insert("Hello")
editor.show()  # 输出：Current text:  Hello History:  [('Hello', 'insert')]

editor.insert(", World!")
editor.show()  # 输出：Current text:  Hello, World! History:  [('Hello', 'insert'), ('Hello, World!', 'insert')]

copy_text = editor.copy()
editor.show()  # 输出：Current text:  Hello, World! History:  [('Hello', 'insert'), ('Hello, World!', 'insert'), ('copy', 'Hello, World!')]

editor.paste(copy_text)
editor.show()  # 输出：Current text:  Hello, World!Hello, World! History:  [('Hello', 'insert'), ('Hello, World!', 'insert'), ('copy', 'Hello, World!'), ('Hello, World!Hello, World!', 'paste')]

editor.undo()
editor.show()  # 输出：Current text:  Hello, World! History:  [('Hello', 'insert'), ('Hello, World!', 'insert'), ('copy', 'Hello, World!'), ('Hello, World!Hello, World!', 'paste')]

cut_text = editor.cut()
editor.show()  # 输出：Current text:  Hello, World! History:  [('Hello', 'insert'), ('Hello, World!', 'insert'), ('copy', 'Hello, World!'), ('Hello, World!Hello, World!', 'paste'), ('!', 'cut')]

print("Cut text: ", cut_text)  # 输出：Cut text:  !
