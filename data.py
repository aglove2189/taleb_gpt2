
tweets = open('nntaleb.txt', encoding='utf8').readlines()

tweets = [t.partition('<nntaleb> ')[2] for t in tweets]
tweets = [t for t in tweets if 'http' not in t]

with open('nntaleb_cleaned.txt', 'w', encoding='utf8') as writer:
    writer.writelines(tweets)
