# Лабараторная работата 5
# Выполнил студент гр. АСУ4-22-1м
# Попов Кирилл Михайлович
# Задание 2
# Проведение вычислений:
{
  names <- c("Кирилл", "Михаил", "Иван", "Фёдор","Игорь", "Алексей", "Александр", "Григорий", "Виктор", "Олег",
             "Артур", "Евгений", "Максим", "Фёдор", "Генадий", "Сергей", "Даниил", "Константин", "Николай", "Никита")
  familys <- c("Попов", "Пушкин", "Сидоров", "Иванов","Жуков", "Герасимов", "Фролов", "Лермонтов", "Красильников", "Чуприянов",
               "Мояковский", "Онегин", "Пушной", "Менделеев", "Распутин", "Галкин", "Докучаев", "Прянишников", "Кондратьев", "Троцкий")
  names <- sample(names, 20, replace=TRUE) # с тёсками по имени
  familys <- sample(familys, 20, replace=FALSE) # Без родственников и однофамильцев
  full_names = paste(familys, names)
  
  BY <- ceiling(sample(runif((1960:1985),1960, 1985), 20, replace=FALSE))
  BY_18 <- BY + 18

  EY_1 <- ceiling(sample(runif((BY_18[1]:2006),BY_18[1], 2006), 1))
  EY_2 <- ceiling(sample(runif((BY_18[2]:2006),BY_18[2], 2006), 1))
  EY_3 <- ceiling(sample(runif((BY_18[3]:2006),BY_18[3], 2006), 1))
  EY_4 <- ceiling(sample(runif((BY_18[4]:2006),BY_18[4], 2006), 1))
  EY_5 <- ceiling(sample(runif((BY_18[5]:2006),BY_18[5], 2006), 1))
  EY_6 <- ceiling(sample(runif((BY_18[6]:2006),BY_18[6], 2006), 1))
  EY_7 <- ceiling(sample(runif((BY_18[7]:2006),BY_18[7], 2006), 1))
  EY_8 <- ceiling(sample(runif((BY_18[8]:2006),BY_18[8], 2006), 1))
  EY_9 <- ceiling(sample(runif((BY_18[9]:2006),BY_18[9], 2006), 1))
  EY_10 <- ceiling(sample(runif((BY_18[10]:2006),BY_18[10], 2006), 1))
  EY_11 <- ceiling(sample(runif((BY_18[11]:2006),BY_18[11], 2006), 1))
  EY_12 <- ceiling(sample(runif((BY_18[12]:2006),BY_18[12], 2006), 1))
  EY_13 <- ceiling(sample(runif((BY_18[13]:2006),BY_18[13], 2006), 1))
  EY_14 <- ceiling(sample(runif((BY_18[14]:2006),BY_18[14], 2006), 1))
  EY_15 <- ceiling(sample(runif((BY_18[15]:2006),BY_18[15], 2006), 1))
  EY_16 <- ceiling(sample(runif((BY_18[16]:2006),BY_18[16], 2006), 1))
  EY_17 <- ceiling(sample(runif((BY_18[17]:2006),BY_18[17], 2006), 1))
  EY_18 <- ceiling(sample(runif((BY_18[18]:2006),BY_18[18], 2006), 1))
  EY_19 <- ceiling(sample(runif((BY_18[19]:2006),BY_18[19], 2006), 1))
  EY_20 <- ceiling(sample(runif((BY_18[20]:2006),BY_18[20], 2006), 1))
  
  EY <- c(EY_1, EY_2, EY_3, EY_4, EY_5, EY_6, EY_7, EY_8, EY_9, EY_10, 
         EY_11, EY_12, EY_13, EY_14, EY_15, EY_16, EY_17, EY_18, EY_19, EY_20)
  
  for(i in BY){
    if(i > 1975){
      slry <- ceiling((log(2007-EY)+1)*8000)
    }
    else{
      slry <- ceiling((log2(2007-EY)+1)*8000)
    } 
  }
}

# Получение фрейма
{
  print(c("Фрейм данных:"))
  Nrow = c((1:20))
  Name = c(full_names)
  BirthYear = c(BY)
  EmployYear = c(EY)
  Salary = c(slry)
  tax = ceiling(slry*0.13)
  f = data.frame(Nrow, Name, BirthYear, EmployYear, Salary, tax)
  print(f)

  n <- 0
  for(i in slry){
    if (i > 15000){
      n = n +1
    }
  }
  print(paste("Колличество людей, чъя з/п > 15000: ",n))
}
