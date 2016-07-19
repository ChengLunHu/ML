from nltk.book import *

####################
# Searching Text
####################
print text4.concordance("democracy")
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

print text1.concordance("monstrous")
text1.dispersion_plot(["monstrous"])
