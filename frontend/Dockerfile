# # build env
# FROM node:21.6.2-alpine
# WORKDIR /app

# COPY package*.json ./

# RUN npm install

# COPY . ./
# RUN npm run build

# FROM node:21.6.2
# WORKDIR /app

# # Копируем package.json и package-lock.json для установки зависимостей
# COPY package.json package.json
# COPY package-lock.json package-lock.json

# # Устанавливаем зависимости
# RUN npm ci

# # Копируем все файлы проекта
# COPY . .

# # Собираем проект
# RUN npm run build
# # Устанавливаем глобально http-server для раздачи статических файлов
# RUN npm install --global http-server

# # Команда для запуска http-server, раздающего статические файлы из /app/.next/static
# CMD ["npx", "-y", "http-server", "-p", "8000", "/app/.next/static"]

# FROM node:21.6.2
# WORKDIR /app

# # Копируем package.json и package-lock.json для установки зависимостей
# COPY package*.json ./

# # Устанавливаем зависимости
# RUN npm ci

# # Копируем все файлы проекта
# COPY . .

# # Собираем проект
# RUN npm run build

# # Устанавливаем глобально http-server для раздачи статических файлов (если необходимо)
# RUN npm install --global http-server

# # Команда для запуска http-server, раздающего статические файлы из /app/.next/static
# # CMD ["npx", "-y", "http-server", "-p", "8000", "/app/.next/static"]

# # Если вы хотите использовать Next.js сервер, раскомментируйте следующую строку:
# CMD ["npm", "start"]

FROM node:21.6.2
WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY package*.json ./

# Устанавливаем зависимости
RUN npm ci

# Копируем все файлы проекта
COPY . .

# Собираем проект
RUN npm run build

# Устанавливаем pm2 глобально
RUN npm install -g pm2

# Команда для запуска приложения с помощью pm2
CMD ["pm2-runtime", "start", "npm", "--name", "frontend", "--", "start"]
