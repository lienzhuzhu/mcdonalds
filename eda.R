source("./setup.R")

mcds <- read.csv("./data/mcds_clean.csv", header=TRUE)

mcds$other_fat <- mcds$total_fat_g - (mcds$saturated_fat_g + mcds$trans_fat_g)
mcds$weight_watchers_points <- NULL

print(sapply(mcds, class))