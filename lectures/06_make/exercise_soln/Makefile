biom_report.html: figs/fig1.png figs/fig2.png R/biom_report.Rmd raw_data/biomarkers.txt raw_data/clinical.txt
	cd R && Rscript -e "rmarkdown::render('biom_report.Rmd', output_file = '../biom_report.html')"

figs/fig1.png: R/make_fig1.R clean_data/clean_data.txt
	chmod +x R/make_fig1.R && R/make_fig1.R

figs/fig2.png: R/make_fig2.R clean_data/clean_data.txt
	chmod +x R/make_fig2.R && R/make_fig2.R

# add documentations
clean_data/clean_data.txt: R/clean_data.R raw_data/biomarkers.txt raw_data/clinical.txt
	chmod +x R/clean_data.R && R/clean_data.R