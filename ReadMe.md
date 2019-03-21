

### 项目介绍
- 利用scrapy_redis爬虫框架，分布式爬取fun一下网站的美女图片，将图片地址存储到本地mongodb和远程mongodb，并下载图片到imgs路径下


### 开发环境
- python 3.6.4

### 配置开发环境
- python库：
    命令行下运行 pip install -r requirements.txt
- exe程序：

    版本管理软件: git

    数据库软件：mongodb, redis

    数据库可视化软件： robo3t(for mongodb)， RedisDesktopManager(for redis)

- settings配置：

    添加redis服务器地址>>>REDIS_URL = 'redis://name:password@ip:port'
- PS:

    确保scrapy, pip已在系统环境变量目录下

### 部署
- master主机启动redis服务和mongodb服务

- slave主机启动mongodb服务


### 启动项目
- ！！！本项目需要手动生成代理列表，务必在启动前运行oldHouse/service/protester文件
- 分别在各台主机项目目录下，在命令行输入：scrapy crawl get_beauty启动

