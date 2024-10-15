# # build env
# FROM node:21.6.2-alpine
# WORKDIR /app

# COPY package*.json ./

# RUN npm install

# COPY . ./
# RUN npm run build

FROM node:21.6.2
WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY package.json package.json
COPY package-lock.json package-lock.json

# Устанавливаем зависимости
RUN npm ci

# Копируем все файлы проекта
COPY . .

# Собираем проект
RUN npm run build
# Устанавливаем глобально http-server для раздачи статических файлов
RUN npm install --global http-server

# Команда для запуска http-server, раздающего статические файлы из /app/dist
CMD ["npx", "-y", "http-server", "-p", "8000", "/app/build"]
