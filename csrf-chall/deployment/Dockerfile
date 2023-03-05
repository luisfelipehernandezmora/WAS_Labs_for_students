FROM ubuntu:20.04
RUN apt update -yqq
RUN apt install curl -yqq
RUN curl -fsSL https://deb.nodesource.com/setup_16.x |  bash -
RUN apt-get install nodejs -yqq
RUN apt install sqlite3 -yqq
RUN apt install unzip -yqq
RUN apt install python3 python3-pip python3-dev -yqq
RUN pip3 install flask requests uuid
# install chrome
ENV TZ=Asia/Kolkata \
    DEBIAN_FRONTEND=noninteractive
WORKDIR /app
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
RUN apt install -y --no-install-recommends libappindicator3-1 libasound2 libatk1.0-0 libatspi2.0-0 libc6 libcairo2 libcap2 libcups2 libdrm2 libevdev2 libexpat1 libfontconfig1 libfreetype6 libgbm1 libglib2.0-0 libgtk-3-0 libpam0g libpango-1.0-0 libpci3 libpcre3 libpixman-1-0 libspeechd2 libstdc++6 libsqlite3-0 libuuid1 libwayland-egl1-mesa libx11-6 libx11-xcb1 libxau6 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxdmcp6 libxext6 libxfixes3 libxi6 libxinerama1 libxrandr2 libxrender1 libxtst6 zlib1g
RUN apt install -y --no-install-recommends libnss3-dev libgdk-pixbuf2.0-dev libgtk-3-dev libxss-dev
COPY ./installers/chromium-latest.sh ./
RUN chmod +x ./chromium-latest.sh 
RUN ./chromium-latest.sh
WORKDIR /app/bot
COPY bot/package.json .
RUN npm install
WORKDIR /app
COPY . .
RUN useradd bot
RUN chown bot ./chall/csrfdb.db
RUN chmod 777 chall
RUN chmod +x ./run.sh
USER bot
CMD "./run.sh"