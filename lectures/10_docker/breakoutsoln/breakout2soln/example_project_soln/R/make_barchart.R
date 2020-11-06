#! /usr/bin/Rscript

# get environment variable to determine which figure to make
which_fig <- Sys.getenv("which_fig")
# here, I added a new comment
data(mtcars)

library(wesanderson)
colors <- wes_palettes$Zissou1[1:3]

if(which_fig == "gears_vs_cylinders"){
	tab <- table(mtcars$cyl, mtcars$gear)
	x_names <- paste0("Type ", 1:3)
	main <- "Distribution of Gears vs Cylinders"
	xlab <- "Gear Types"
}else if(which_fig == "gears_vs_carb"){
	tab <- table(mtcars$cyl, mtcars$carb)
	x_names <- paste0("Carb ", sort(unique(mtcars$carb)))
	main <- "Distribution of Gears vs. Carb"
	xlab <- "Carb Types"
}

png("figs/barchart.png")
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
