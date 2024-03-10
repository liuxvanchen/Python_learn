import psutil
import os


def list_processes():
    print("当前运行的进程:")
    for proc in psutil.process_iter(['pid', 'name', 'status', 'create_time']):
        print(
            f"PID: {proc.info['pid']}, 名称: {proc.info['name']}, 状态: {proc.info['status']}, 创建时间: {proc.info['create_time']}")


def kill_process(pid):
    try:
        os.kill(pid, os.signal.SIGTERM)  # 发送SIGTERM信号来请求进程优雅地终止
        print(f"进程 {pid} 已被终止")
    except ProcessLookupError:
        print(f"找不到进程 {pid}")
    except PermissionError:
        print(f"没有权限终止进程 {pid}")
    except Exception as e:
        print(f"终止进程 {pid} 时出错: {e}")


while True:
    print("\n请选择操作:")
    print("1. 列出所有进程")
    print("2. 终止一个进程 (请输入PID)")
    print("3. 退出")
    choice = input("请输入选项 (1/2/3): ")

    if choice == '1':
        list_processes()
    elif choice == '2':
        pid = input("请输入要终止的进程的PID: ")
        kill_process(int(pid))
    elif choice == '3':
        break
    else:
        print("无效的选项，请重新输入")
