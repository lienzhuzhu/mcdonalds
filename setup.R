# setup.R
# Lien Zhu
# Description: Install packages


print("+++++++++++++++++++")
print("setting up packages")
print("+++++++++++++++++++")

# List of required packages
required_packages <- c(
  "ggplot2"
)

# Function to check if a package is installed and install it if not
install_if_missing <- function(packages) {
  for (pkg in packages) {
    if (!requireNamespace(pkg, quietly = TRUE)) {  # Check if the package is installed
      message(sprintf("Installing missing package: %s", pkg))
      install.packages(pkg)
    } else {
      message(sprintf("Package already installed: %s", pkg))
    }
  }
}

# Install all required packages
install_if_missing(required_packages)