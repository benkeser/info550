#! /usr/local/bin/Rscript

data_merge <- read.table("clean_data/clean_data.txt", header = TRUE)

# plot of biom1 by age and biom2 by age
png("figs/fig1.png")
layout(t(1:2))
plot(y = data_merge$biom1, x = data_merge$age,
     xlab = "Age", ylab = "Biomarker 1",
     col = data_merge$sexf + 1, pch = 19)
legend(title = "Sex", col = c(1, 2), 
       legend = c("Male", "Female"),
       pch = 19,
       x = "topleft")
plot(y = data_merge$biom2, x = data_merge$age,
     xlab = "Age", ylab = "Biomarker 2",
     col = data_merge$sexf + 1, pch = 19)
dev.off()