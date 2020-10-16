#! /usr/local/bin/Rscript

data_merge <- read.table("clean_data/clean_data.txt", header = TRUE)

# plot of biom1 vs. biom 2
png("figs/fig2.png")
plot(y = data_merge$biom1, x = data_merge$biom2,
     xlab = "Biomarker2", ylab = "Biomarker 1")
dev.off()