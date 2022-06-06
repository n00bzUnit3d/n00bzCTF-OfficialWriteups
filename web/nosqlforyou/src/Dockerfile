FROM mhart/alpine-node:14
RUN mkdir -p /challenge
WORKDIR /challenge
COPY package.json /challenge
RUN npm install
COPY challenge /challenge
EXPOSE 42067
CMD ["node", "challenge.js"]
