# dingtalk-chatbot
## 描述
这是一个基于dingtalk-chatbot镜像进行二次开发的Docker镜像，有时候可能你需要使用它来返回一些在Linux上运行命令的结果，如日常文件备份的通知，警告

## 环境变量
WEBHOOK: 钉钉机器人的webhook

APPNAME: 应用信息标题 (看你想输入什么)

COMMAND: 执行的命令 如：（cat /proc/cpuinfo）

AT: @钉钉群组里的某个人（填写电话号码，使用逗号分隔） 

## 示例
docker run -v /root/dingtalk:/root/log --rm -d --env WEBHOOK=https://oapi.dingtalk.com/robot/send?access_token=xxx --env APPNAME=xxx --env COMMAND=xxx --env AT=xxx,xxx arrowhalo/dingtalk-chatbot:1.0.0 


