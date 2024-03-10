import argparse
import os
import shutil
import time


def backup_directory(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(dest_dir, f"backup_{timestamp}")
    shutil.copytree(src_dir, backup_dir)
    print(f"备份完成： {src_dir}->{backup_dir}")


def main():
    parser = argparse.ArgumentParser(description="一个简单的命令行工具来自动化一些常见任务")
    parser.add_argument("src_dir", type=str, help="要备份的源目录")
    parser.add_argument("dest_dir", type=str, help="备份文件的目标目录")
    parser.add_argument("--verbose", "-v", action="store_true", help="显示详细输出")

    args = parser.parse_args()

    if args.verbose:
        print(f"开始备份 {args.src_dir} 到 {args.dest_dir}")

    backup_directory(args.src_dir, args.dest_dir)


if __name__ == "__main__":
    main()
