# read data
data <- read.csv("data.txt", header = TRUE)

# make and save histogram
png("fig1.png")
hist(data$X)
dev.off()