from tools import manager

def io(name, *args):
    msg = "Incorrect number of arguments.Please check and try again."
    tool = manager.ToolManager(args[0])
    match name:
        case "ls":
            if conf(1, *args):
                return tool.ls()
            return msg
        case "lsr":
            if conf(1, *args):
                return tool.lsr()
            return msg
        case "read":
            if conf(1, *args):
                return tool.read()
            return msg
        case "read_docx":
            if conf(1, *args):
                return tool.read_docx()
            return msg
        case "write_docx":
            if conf(2, *args):
                return tool.write_docx(args[1])
            return msg
        case "create_f":
            if conf(1, *args):
                return tool.create_f()
            return msg
        case "create_d":
            if conf(1, *args):
                return tool.create_d()
            return msg
        case "delete":
            if conf(1, *args):
                return tool.delete()
            return msg
        case "info":
            if conf(1, *args):
                return tool.info()
            return msg
        case "rename":
            if conf(2, *args):
                return tool.rename(args[1])
            return msg
        case "write_a":
            if conf(2, *args):
                return tool.write_a(args[1])
            return msg
        case "write_w":
            if conf(2, *args):
                return tool.write_w(args[1])
            return msg
        case "search":
            if conf(2, *args):
                return tool.search(args[1])
            elif conf(3, *args):
                return tool.search(args[1], args[2])
            return msg
        case "readl":
            if conf(2, *args):
                return tool.readl(args[1])
            elif conf(3, *args):
                return tool.readl(args[1], args[2])
            return msg
        
    tool = manager.ToolManager(args[0], args[1])
    match name:
        case "move":
            if conf(2, *args):
                return tool.move()
            return msg
        case "copy":
            if conf(2, *args):
                return tool.copy()
            return msg
        
    return "No such tool.Please check and try again."

def conf(num, *args):
    if num != len(args):
        return False
    return True