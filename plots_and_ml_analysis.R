twitter_data <- read.csv("intermediate_data.txt", encoding="UTF-*", stringsAsFactors = FALSE, header = FALSE)
twitter_data[,5] <- NULL
colnames(twitter_data) <- c("Month", "Day", "Year", "Count")

library(ggplot2)

qplot(twitter_data$Month, twitter_data$Count)