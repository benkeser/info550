#! /usr/bin/env Rscript

# read data
raw_data <- read.csv("raw_data.txt", header = TRUE)

# remove NAs
data <- raw_data[!is.na(raw_data), , drop = FALSE]

# save data
write.table(data, "data.txt", quote = FALSE, row.names = FALSE)