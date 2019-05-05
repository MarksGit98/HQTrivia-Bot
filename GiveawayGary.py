import tweepy
from time import sleep

Accounts={'CryptoKyle00':['P7lkPR7goQ1acnUnZYuaPTkry',
                          'wJCqidJZ7zTMA0grAfqDMyEkeYjVgD8nbOLvdEbzMKaafLMcX4',
                          	'956278884256899073-JD1LJTyDW9B2AxJIIalOVuHvGdIJoZj',
                              'gviwOa4DtVOsnuh1G76ZtYSFCTxqk8popr3cqWHpgCo1A',
                              'TwitterBot231@gmail.com'],
        'CryptoKyle007':['jGv4qm5KIrbzBJpEgGo6CuhR9',
                         'AzXkYfxDeUt1aRLXfClJCMLXtZO3qF3ZLUSYn8w9ldUjAItCGC',
                         '956290349076484096-rC3qa9UjnGVRqxuuTI5Yal0KFRuI78x',
                         'U6Y32wFkXlu9iK0ZruW7Bemq2ZINsKZGWzkQv55FRZ6Bt',
                         'memesupplier007@gmail.com'],
        'AgasiZarbail':['C0ccBwcU2A1Q8u9swhH5niHaq',
                        'ngjvlC4CEZrCGLqOFmqHH75q6GPQ7CC4eWmhrtOuB1K5B1Ebdy',
                        '960017545716797441-6c41HPpyOY2KCn52PVp0JAYmeeovd2j',
                        '0V4lRsoApmcKgDl0cp1eSy7LtRLONWTsydu7zTOF1flGF',
                        'thatguysammm@aol.com'],
        'YoloShlomo':['CoW9BFeJvOEhIosS0HYRPIUxC',
                      'CK8ZkjKWJ4v3p64ybaShoTGMP2hHaK472fbvKA9vfPzL5ZzwCz',
                      '961714268637888512-ePluEF0nxOQnkwT04oJuF4FYUZjidMr',
                      'eI62LGxzonpkGiUgOJA3C4k5RV0vyBkT8fx8TNmXHJ9E1',
                      'TwitterBot232@gmail.com'],
        'SamRichards1122':['HY1oJLotgeehPEYCoQ5fcEXUR',
                           'PWQMHUxQvuZfDyK8QFr4ldxEue8qcjO1wlYLboyr6VnMaSl8Bm',
                           '961737629866844162-nzJ5M9W3CPg9jjFEgDCfQJG0ly8oOL5',
                           'PSNA44RnfWQzl6S9SsZW69AMQdZJEhtvHZXNd4kab4p5x',
                           'Twitterbot233@gmail.com']}
        

myBot = api.get_user(screen_name='@CryptoKyle00')

def main():
    acc_counter = 0
    total_counter = 0
    for key in Accounts:
        consumer_key = Accounts[key][0]
        consumer_secret = Accounts[key][1]
        access_token = Accounts[key][2]
        access_token_secret = Accounts[key][3]
        #followed_users_list= open('followed_users.text','r+')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        auth.secure = True
        api = tweepy.API(auth)
        # myList=api.get_list(owner=myBot)
        for tweet in tweepy.Cursor(api.search, q='Retweet to Win').items(5000):
            try:
                print("Found tweet by: @" + tweet.user.screen_name)
                if (tweet.retweeted == False) or (tweet.favorited == False):
                    tweet.retweet()
                    tweet.favorite()
                    if hasattr(tweet, 'retweeted_status'):
                        tweet.retweeted_status.author.follow()
                        #followed_users_list.write((tweet.retweeted_status.author.screen_name) + '\n')
                    else:
                       tweet.user.follow()
                       #followed_users_list.write((tweet.user.screen_name) + '\n')
                    sn=tweet.user.screen_name
                  
                    acc_counter += 1
                    total_counter+=1
                    print('Contests Entered on: '+key+': '+acc_counter, '\n', 'Total Contests Entered: '+total_counter)
                if acc_counter == 250:
                    acc_counter=0
                    break
            except tweepy.TweepError as e:
                print(e.reason)
                sleep(1)
                continue
            except StopIteration:
                break
        #followed_users_list.close()
        
def dm_reader():
    file=open('dm_count.txt','r+')
    old_count=[]
    for line in file:
        old_count.append(int(line))
    new_count=[]
    j=0
    for key in Accounts:
        consumer_key = Accounts[key][0]
        consumer_secret = Accounts[key][1]
        access_token = Accounts[key][2]
        access_token_secret = Accounts[key][3]
        #followed_users_list= open('followed_users.text','r+')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        auth.secure = True
        api = tweepy.API(auth)
        api.direct_messages().full_text = True
        counter=0
        for dm in api.direct_messages():
            counter+=1
        new_count.append(counter)
        
        print(key+' has '+str(counter-old_count[j])+' new messages.')
        j+=1
    i=0
    for line in file:
        file.write(new_count[i])
dm_reader()

