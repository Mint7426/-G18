import psutil


def get_disk_paths():
    disk_partitions = psutil.disk_partitions()
    disk_paths = []
    for partition in disk_partitions:
        if 'cdrom' not in partition.opts and partition.fstype != '':
            disk_paths.append(partition.mountpoint)
    return disk_paths


# 获取本地磁盘路径列表
disk_paths = get_disk_paths()

# 打印本地磁盘路径
for path in disk_paths:
    print(path)
