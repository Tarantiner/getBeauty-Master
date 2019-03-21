

### 项目介绍
- 利用scrapy_redis爬虫框架，爬取fun一下网站的美女图片，将图片存储到本地mongodb并下载图片到img路径下


### 开发环境
- python 3.6.4

### 配置开发环境
- python库：
    命令行下运行 pip install -r requirements.txt

- exe程序：

    数据库软件：mongodb

    数据库可视化软件： robo3t(for mongodb)


- PS:

    确保scrapy, pip已在系统环境变量目录下

### 部署
- 启动mongodb服务端


### 启动项目
- ！！！本项目需要手动生成代理列表，务必在启动前运行getBeauty/service/protester文件
- 在项目目录下，在命令行输入：scrapy crawl get_beauty启动    

