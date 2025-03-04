# Global Student Portal: Stability Metrics in Neo4j

Этот проект демонстрирует расчёт метрик стабильности (Fan-in, Fan-out, Instability) для компонентов системы "Global Student Portal" с использованием Neo4j.

## Метрики стабильности

1. **Fan-in:** Количество входящих зависимостей.
2. **Fan-out:** Количество исходящих зависимостей.
3. **Instability (I):** Рассчитывается как `FanOut / (FanIn + FanOut)`.

## Результаты

### Fan-in (входящие зависимости)

| Component          | Fan-in |
|--------------------|--------|
| UserService        | 3      |
| Database           | 2      |
| EmailService       | 1      |

### Fan-out (исходящие зависимости)

| Component          | Fan-out |
|--------------------|---------|
| AuthService        | 1       |
| UserService        | 1       |
| CourseService      | 2       |
| NotificationService| 2       |

### Instability (I)

| Component          | Fan-in | Fan-out | Instability |
|--------------------|--------|---------|-------------|
| AuthService        | 0      | 1       | 1.0         |
| UserService        | 3      | 1       | 0.25        |
| Database           | 2      | 0       | 0.0         |
| CourseService      | 0      | 2       | 1.0         |
| NotificationService| 0      | 2       | 1.0         |
| EmailService       | 1      | 0       | 0.0         |

## Как запустить

1. Установи Docker и Docker Compose.
2. Запусти Neo4j:
   ```bash
   docker-compose up -d