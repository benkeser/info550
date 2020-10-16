#! /usr/local/bin/Rscript

data_clin <- read.table("raw_data/clinical.txt", header = TRUE)
data_biom <- read.table("raw_data/biomarkers.txt", header = TRUE)
data_merge <- merge(data_clin, data_biom)

write.table(data_merge, "clean_data/clean_data.txt")