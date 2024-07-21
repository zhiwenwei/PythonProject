import time,sys

indent = 0 # 缩进多少空格
indentIncreasing = True # 缩进是否增加

try:
    while True:
        print('    ' * indent, end='')
        print('********')
        time.sleep(0.1)  # 暂定0.1秒

        if indentIncreasing:
            # 增加空格的数量
            indent = indent + 1
            if indent == 20:
                # 切换方向
                indentIncreasing = False
        else:
            # 减少空格的数量
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
