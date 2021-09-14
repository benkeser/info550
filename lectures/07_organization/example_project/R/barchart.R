here::i_am("R/barchart.R")
data(mtcars)

library(wesanderson)
colors <- wes_palettes$Zissou1[1:3]

tab <- table(mtcars$cyl, mtcars$gear)
x_names <- paste0("Type ", 1:3)
main <- "Distribution of Gears vs Cylinders"
xlab <- "Gear Types"

png(here::here("figs", "barchart.png"))
	barplot(tab, 
	        main = main, 
	        names.arg = x_names, 
	        xlab = xlab, 
	        ylab = "Frequency", 
	        col = colors)
	legend(x = "topright", 
	       legend = rownames(tab), 
	       fill = colors)
dev.off()