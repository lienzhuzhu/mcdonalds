source("./setup.R")

mcds <- read.csv("./data/mcds_clean.csv", header=TRUE)
cat(sprintf("Protein and Calories:\t%f\n", cor(mcds$protein, mcds$calories)))
cat(sprintf("Calories and Total Fat:\t%f\n", cor(mcds$calories, mcds$total_fat_g)))


mcds$other_fat <- mcds$total_fat_g - (mcds$saturated_fat_g + mcds$trans_fat_g)
mcds$weight_watchers_points <- NULL


print(head(mcds[, c(1:2, (ncol(mcds) - 1):ncol(mcds))]))

View(mcds)