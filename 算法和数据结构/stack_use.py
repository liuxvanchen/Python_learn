def is_stack(s):
    opening = "({["
    closeing = ")}]"
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for ss in s:
        if ss in opening:
            stack.append(ss)
        elif ss in closeing:
            if not stack or mapping[ss] != stack.pop():
                return False
    return not stack


print(is_stack("[(]"))
