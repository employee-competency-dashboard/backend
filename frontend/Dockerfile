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

# # Устанавливаем pm2 глобально
# RUN npm install -g pm2

# # Команда для запуска приложения с помощью pm2
# CMD ["pm2-runtime", "start", "npm", "--name", "frontend", "--", "start"]

# Устанавливаем базовый образ
FROM node:21-alpine AS base

FROM base AS builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости только при необходимости
COPY package.json package-lock.json ./
RUN npm ci

# Копируем исходный код и выполняем команды
COPY . .

# Отключаем телеметрию Next.js
ENV NEXT_TELEMETRY_DISABLED=1
ENV NODE_ENV=production

# Сборка приложения
RUN npm run build

# Производственный этап
FROM base AS runner

# Устанавливаем рабочую директорию
WORKDIR /app

# Отключаем телеметрию Next.js
ENV NEXT_TELEMETRY_DISABLED=1

ENV NODE_ENV=production
ENV AUTH_SECRET="NfYkdDFYYreY="
ENV HOST=http://127.0.0.1
ENV NEXT_PUBLIC_API_HOST=http://127.0.0.1
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs


RUN mkdir .next
RUN chown nextjs:nodejs .next

# Копируем необходимые файлы из предыдущего шага
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static
COPY --from=builder --chown=nextjs:nodejs /app/public ./public

USER nextjs

# Открываем порт
EXPOSE 3000

ENV PORT=3000

# Запускаем приложение
CMD node server.js

