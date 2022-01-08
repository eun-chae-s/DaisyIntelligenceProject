library(ggplot2)
file <- read.csv('./tiktok_dataset.csv')
file

data = file[(names(file) %in% c("popularity", "danceability", "acousticness"))]
data

ggplot(data, aes(x = popularity, y = Values)) +
geom_point(aes(y = danceability, color = 'danceability'), alpha=0.2) +
scale_x_continuous(breaks=c(0, 30, 60, 90)) + 
geom_point(aes(y = acousticness, color = 'acousticness'), alpha = 0.2) +
ggtitle('Popularity rate in acousticness and danceability')

sampling <- data[sample(nrow(data), 1000), ]
sampling

ggplot(sampling, aes(x = popularity, y = Values)) +
geom_point(aes(y = danceability, color = 'danceability'), alpha=0.4) +
scale_x_continuous(breaks=c(0, 30, 60, 90)) + 
geom_point(aes(y = acousticness, color = 'acousticness'), alpha = 0.4) +
ggtitle('Popularity rate in acousticness and danceability from samples of 1000')
