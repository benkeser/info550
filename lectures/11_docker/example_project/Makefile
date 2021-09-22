report.html: R/report.Rmd figs/barchart.png
	cd R; Rscript -e "rmarkdown::render('report.Rmd', output_file = '../report.html')"

figs/barchart.png: R/make_barchart.R
	Rscript R/make_barchart.R