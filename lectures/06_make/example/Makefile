# rule for making report  
report.html: data.txt report.Rmd
	Rscript -e "rmarkdown::render('report.Rmd', quiet = TRUE)"

# rule for cleaning data
data.txt: cleandata.R raw_data.txt
	chmod +x cleandata.R & \
	Rscript cleandata.R
