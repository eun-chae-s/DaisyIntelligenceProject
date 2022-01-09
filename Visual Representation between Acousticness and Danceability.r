library(ggplot2)

# Reading .csv file

file <- read.csv('./tiktok_newdataset.csv')
file

# New DataFrame with 'popularity', 'danceability' and 'acousticness'

data = file[(names(file) %in% c("popularity", "danceability", "acousticness"))]
data

# Scatter Plot 

ggplot(data, aes(x = popularity, y = Values)) +
geom_point(aes(y = danceability, color = 'danceability'), alpha=0.2) +
scale_x_continuous(breaks=c(0, 30, 60, 90)) + 
geom_point(aes(y = acousticness, color = 'acousticness'), alpha = 0.2) +
ggtitle('Popularity rate in Acousticness and Danceability')

# Ramdoming new DataFrame with samples of 1000

sampling <- data[sample(nrow(data), 1000), ]
sampling

# Scatter Plot

ggplot(sampling, aes(x = popularity, y = Values)) +
geom_point(aes(y = danceability, color = 'danceability'), alpha=0.4) +
scale_x_continuous(breaks=c(0, 30, 60, 90)) + 
geom_point(aes(y = acousticness, color = 'acousticness'), alpha = 0.4) +
ggtitle('Popularity rate in Acousticness and Danceability from samples of 1000')
