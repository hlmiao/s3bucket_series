## 1. 创建Lambda Function，runtime选择Python3.7
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-001.png)
## 2. 创建Role或者选择已有Role
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-002.png)
## 3. 打开新的页面，在IAM中选择Role，确认这个Role可以读写s3存储桶
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-003.png)
## 4. 回到之前创建Lambda Function页面，点击新建，Lambda Function代码见同目录gzip_compress.py
## 5. 创建了两个桶，-bk为备份用
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-004.png)
## 6. 选择桶tizhong-compression，在属性中找到Event notifications，编辑并名字
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-007.png)
## 7. 编辑触发的事件类型
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-008.png)
## 8. 选择目标为Lambda Function，并选择刚才创建好的Lambda Function
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-009.png)
## 9. 初始化文件上传大小
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-005.png)
## 10. 压缩后文件大小
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-006.png)
## 11. 监控任务面板，CloudWatch
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-011.png)
## 12. 需要根据处理文件大小调整Lambda Function RAM大小
![image](https://github.com/hlmiao/s3bucket_series/blob/master/gzip_compress/pic/tz-012.png)





