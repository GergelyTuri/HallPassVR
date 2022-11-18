### Data: three successive days of training for one animal

* there are two matlab files in the `Analysis code` directory. The aim would be translating those to python.  

* The first thing would be to parse the .txt file to get positions and events, then reproduce the heatmap spatial licking plots above, then to calculate some measure of lick tuning and analyze the emergence of lick spatial selectivity over laps and over sessions. 
The `.txt` files are the raw data, the `image.png` files are the output the matlab analysis yields. 

* You can plot both the spatial licking histograms over the whole session (left) and lap-by-lap (right) (se `example histogram.png`)

* One thing that would be good to extend this very basic analysis would be to analyze the increased selectivity of licking during learning. I've done this in different ways in the past, such as a Rayleigh Z-score of circular tuning (i.e. circular tuning vector).