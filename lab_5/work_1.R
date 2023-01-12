# Лабараторная работата 5
# Выполнил студент гр. АСУ4-22-1м
# Попов Кирилл Михайлович
# Задание 1. Вариант 9
# Задание вектора длинной 1000 из логнормального распределения
{
  x <- 1000
  rl_norm <- rlnorm(x, meanlog=1,sdlog=1)
  print(rl_norm)
}

# Вычисление с помощью встроенных функций
{
  cat("Мат. ожидание 1: ", mean(rl_norm), "\n")
  cat("стандартное отклонение 1: ", sd(rl_norm), "\n")
  cat("Медиана вектора 1: ", median(rl_norm), "\n")
}

# Вычиление без встроенных функций
{
  s <- 0 # сумма элементов
  m <- 0 # среднее арифметическое (мат.ожидание) значение вектора
  q <-0 # стандартное отклонение
  md <- 0 # медиана вектора
  
  # Математическое ожидание
  for (v in rl_norm){
    s <- s+v
  }
  m <- s/x
  cat("Мат. ожидание 2 : ", m, "\n")
  
  # стандартное отклонение
  sum <- 0
  for (z in rl_norm){
    s1 <- (z-m)^2
    sum = sum + s1
  }
  q <- sqrt(sum/x)
  cat("стандартное отклонение 2 : ", q, "\n")

  # Медиана вектора
  ord <- order(rl_norm)
  ord <- rl_norm[ord]
  if(x%%2 == 0){
    md1 <- ord[x/2]
    md2 <- ord[x/2 + 1]
    md = (md1 + md2)/2
    #md = md/2
  }else{
    md <- ord[x/2 +0.5]
  }

  cat("медиана вектора 2 : ", md, "\n")
}

# Исследование изменений значений мат. ожидания логнормального распределения
{
  calc_mean <- function(x)
  {
    rlnorm = rlnorm(x,meanlog=1,sdlog=1)
    mean_rnorm <- mean(rlnorm)
    cat("Мат. ожидание: ", mean_rnorm, "\n")
    return(mean_rnorm)
  }
  
  c <- calc_mean(1000)
  c <- c(c, calc_mean(2000))
  c <- c(c, calc_mean(4000))
  c <- c(c, calc_mean(8000))
  c <- c(c, calc_mean(16000))
  c <- c(c, calc_mean(32000))
  c <- c(c, calc_mean(64000))
  plot(c)
  lines(c)  
}









