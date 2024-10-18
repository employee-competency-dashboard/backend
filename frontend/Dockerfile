# FROM node:21-alpine AS base

# # Install dependencies only when needed
# FROM base AS deps
# # Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
# RUN apk add --no-cache libc6-compat
# WORKDIR /app

# # Install dependencies based on the preferred package manager
# COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./
# RUN \
#   if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
#   elif [ -f package-lock.json ]; then npm ci; \
#   elif [ -f pnpm-lock.yaml ]; then corepack enable pnpm && pnpm i --frozen-lockfile; \
#   else echo "Lockfile not found." && exit 1; \
#   fi


# # Rebuild the source code only when needed
# FROM base AS builder
# WORKDIR /app
# COPY --from=deps /app/node_modules ./node_modules
# COPY . .

# # Next.js collects completely anonymous telemetry data about general usage.
# # Learn more here: https://nextjs.org/telemetry
# # Uncomment the following line in case you want to disable telemetry during the build.
# # ENV NEXT_TELEMETRY_DISABLED=1

# # Production image, copy all the files and run next
# FROM base AS runner
# WORKDIR /app

# ENV NODE_ENV=production
# # Uncomment the following line in case you want to disable telemetry during runtime.
# # ENV NEXT_TELEMETRY_DISABLED=1

# RUN addgroup --system --gid 1001 nodejs
# RUN adduser --system --uid 1001 nextjs

# COPY --from=builder /app/public ./public

# # Set the correct permission for prerender cache
# RUN mkdir .next
# RUN chown nextjs:nodejs .next

# # Automatically leverage output traces to reduce image size
# # https://nextjs.org/docs/advanced-features/output-file-tracing
# COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

# USER nextjs

# EXPOSE 3000

# ENV PORT=3000

# # server.js is created by next build from the standalone output
# # https://nextjs.org/docs/pages/api-reference/next-config-js/output
# ENV HOSTNAME="0.0.0.0"
# CMD ["node", "server.js"]

# # Устанавливаем базовый образ
# FROM node:21-alpine AS base

# FROM base AS builder

# # Устанавливаем рабочую директорию
# WORKDIR /app

# # Устанавливаем зависимости только при необходимости
# COPY package.json package-lock.json ./
# RUN npm ci

# # Копируем исходный код и выполняем команды
# COPY . .

# # Отключаем телеметрию Next.js
# ENV NEXT_TELEMETRY_DISABLED=1
# ENV NODE_ENV=production

# # Сборка приложения
# RUN npm run build

# # Производственный этап
# FROM base AS runner

# # Устанавливаем рабочую директорию
# WORKDIR /app

# # Отключаем телеметрию Next.js
# ENV NEXT_TELEMETRY_DISABLED=1

# ENV HOST=http://127.0.0.1
# ENV NEXT_PUBLIC_API_HOST=http://127.0.0.1
# ENV PORT=3000
# ENV HOSTNAME="0.0.0.0"

# RUN addgroup --system --gid 1001 nodejs
# RUN adduser --system --uid 1001 nextjs


# RUN mkdir .next
# RUN chown nextjs:nodejs .next

# # Копируем необходимые файлы из предыдущего шага
# COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static
# COPY --from=builder --chown=nextjs:nodejs /app/public ./public

# USER nextjs

# # Открываем порт
# EXPOSE 3000

# ENV PORT=3000

# # Запускаем приложение
# # CMD ["node", "server.js"]

# # Устанавливаем pm2 глобально
# RUN npm install -g pm2

# # Команда для запуска приложения с помощью pm2
# CMD ["pm2-runtime", "start", "npm", "--name", "frontend", "--", "start"]

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