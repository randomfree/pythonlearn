import os
import time

# 需要备份的文件
source = ['./backup_ver1.py']

# 备份的路径
target_dir='../pytext/backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S')+'.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup Failed')


