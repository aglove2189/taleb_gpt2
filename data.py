
user = 'TalebWisdom'

tweets = open('{}.txt'.format(user), encoding='utf8').readlines()

tweets = [t.partition('<{}> '.format(user))[2] for t in tweets]
tweets = [t for t in tweets if 'http' not in t and 'pic.twitter' not in t]

rm_strings = ['"', '@nntaleb', 'Nassim', 'Nicholas', 'Taleb', ' - ']
for rm_string in rm_strings:
    tweets = [t.replace(rm_string, '') for t in tweets]

tweets = [' '.join(t.split()) for t in tweets]
tweets = [t + '\n' for t in tweets]

with open('{}_cleaned.txt'.format(user), 'w', encoding='utf8') as writer:
    writer.writelines(tweets)
