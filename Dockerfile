FROM lovepocky/dingtalk-chatbot:1.3.0

MAINTAINER zhangdunfeng<halo@hust.edu.cn>

#ENV WEBHOOK='xxxx' \  APPNAME='' \ AT='zdf1' \ COMMAND='xxx' kubernetes inject

COPY . /app

USER root

WORKDIR /app

ENTRYPOINT ["python", "entrypoint.py"]
