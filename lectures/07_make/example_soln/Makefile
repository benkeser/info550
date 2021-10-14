# rule for making report  
report.html: data.txt report.Rmd fig1.png
	Rscript -e "rmarkdown::render('report.Rmd', quiet = TRUE)"

# rule for cleaning data
data.txt: cleandata.R raw_data.txt
	Rscript cleandata.R

# rule for making the figure
fig1.png: make_fig1.R data.txt
	Rscript make_fig1.R