FROM mhart/alpine-node:14
RUN mkdir -p /challenge
WORKDIR /challenge

#ENV for running host and port
#HOST={domain or ip}:port
ENV HOST="143.110.151.14:42069" 

#For chromium
ENV CHROME_BIN="/usr/bin/chromium-browser"\
    PUPPETEER_SKIP_CHROMIUM_DOWNLOAD="true"
RUN apk add chromium

#Cronjob to remove all files from public dir every 30 mins
RUN touch crontab.tmp \
    && echo '0,30 * * * * /usr/bin/find /challenge/app/public -name "*.html" -type f -exec rm -f {} \;' > crontab.tmp \
    && crontab crontab.tmp \
    && rm -rf crontab.tmp
CMD ["/usr/sbin/crond", "-f", "-d", "0"]

COPY package.json /challenge
RUN npm install
COPY challenge /challenge
EXPOSE 42069
WORKDIR /challenge/app
CMD ["node", "app.js"]
