# Рост апельсинового дерева
{
  require(stats); require(graphics)
  coplot(circumference ~ age | Tree, data = Orange, show.given = FALSE)
  fm1 <- nls(circumference ~ SSlogis(age, Asym, xmid, scal),
             data = Orange, subset = Tree == 3)
  plot(circumference ~ age, data = Orange, subset = Tree == 3,
       xlab = "Tree age (days since 1968/12/31)",
       ylab = "Tree circumference (mm)", las = 1,
       main = "Orange tree data and fitted model (Tree 3 only)")
  age <- seq(0, 1600, length.out = 101)
  lines(age, predict(fm1, list(age = age)))
}

# Получение уранения регрессии
{
  lm.tree <- lm(formula = age ~ circumference, data = Orange)
  lm.tree$coefficients  
  print("Уравнение модели:")
  paste("age = ", lm.tree$coefficients[1], "+", lm.tree$coefficients[2], "*circumference")
}

# Регрессионный анализ набора данных Orange  
{
  b <- lm.tree$coefficients[1]
  a <- lm.tree$coefficients[2]
  xmin <- min(Orange$circumference)
  xmax <- max(Orange$circumference)
  x <- seq(from = xmin, to = xmax, length.out = 100)
  y <- b + a*x
  plot(
    Orange$circumference, 
    Orange$age, 
    main = "Регрессия", 
    xlab = "длинна окружности (мм)", 
    ylab = "возраст (дни с 1968/12/31)"
    )
  grid()
  lines(x, y, col="red")  
}

summary(lm.tree)
