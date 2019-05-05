import tweepy
from time import sleep
from random import shuffle
import random
import time

Addresses={}

Accounts={}
accounts_list=[]
for key in Accounts:
    accounts_list.append(key)            

#myBot = api.get_user(screen_name='@CryptoKyle00')

def dm_reader():
    file=open('dm_count.txt','r+')
    old_count=[]
    new_count=[]
    for count in file:
        old_count.append(str(count))
    j=0
    errors=False
    for key in Accounts:
        try:
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
            dm_list= api.direct_messages()
            if len(dm_list) != 0:
                if len(dm_list[0].text) == int(old_count[j]):
                    print(Accounts[key][4]+': '+'No New Messages')
                    new_count.append(str(len(dm_list[0].text)))
                else:
                    print(Accounts[key][4]+': '+'NEW MESSAGE(S)')
                    new_count.append(str(len(dm_list[0].text)))
            else:
                print(Accounts[key][4]+': '+'0 Total Messages') 
                new_count.append(str(0))
            j+=1
        except tweepy.TweepError as e:
            print(Accounts[key][4]+':',e.reason)
            errors=True
            break
    if errors == False:
        file.truncate()
        file=open('dm_count.txt','w')
        for count in new_count:
            file.write(str(count)+'\n')
        file.close()
    
def get_email_addresses():
    for key in Accounts:
        print(key+': '+Accounts[key][4]+'\n')


def run_individual_bots(bot_lst):
    RTs_per_acc=50
    total_counter=0
    acc_counter=0
    query=0
    sleep_time=1
    search_queries=[#'Retweet Giveaway Tomorrow', 
                    #'Retweet Giveaway',
                    'Retweet to Win',
                    #'Retweet Game Giveaway',
                    #'Gift Card Giveaway',
                    #'Retweet to Win Amazon'
                    ]
    shuffle(search_queries)
    for username in bot_lst:
        over_limit=False
        consumer_key = Accounts[username][0]
        consumer_secret = Accounts[username][1]
        access_token = Accounts[username][2]
        access_token_secret = Accounts[username][3]
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        auth.secure = True
        api = tweepy.API(auth)
        if query < len(search_queries) - 1:
            query+=1
        else:
            query=0
        acc_counter=0
        ran_time = random.randint(3,9)
        for tweet in tweepy.Cursor(api.search, q=search_queries[query]).items(450):
            time.sleep(ran_time)
            if over_limit==True:
                break
            else:
                if not tweet.retweeted:
                    try:
                        print("Found tweet by: @" + tweet.user.screen_name + " on "+Accounts[username][4])
                        if (tweet.retweeted == False) or (tweet.favorited == False):
                            tweet.retweet()
                            tweet.favorite()
                            #if 'FOLLOW' in tweet.full_text or 'Follow' in tweet.full_text or 'follow' in tweet.full_text or '#Follow' in tweet.full_text or '#FOLLOW' in tweet.full_text or '#follow' in tweet.full_text:
                                #print (tweet.full_text)
                            if hasattr(tweet, 'retweeted_status'):
                                tweet.retweeted_status.author.follow()
                                print ('Followed: @'+tweet.retweeted_status.author.screen_name)
                                  
                            else:
                               tweet.user.follow()
                               print ('Followed: @'+tweet.author.screen_name)
                        acc_counter += 1
                        total_counter+=1
                        print('Contests Entered on: '+username+': '+str(acc_counter), '\n', 'Total Contests Entered: '+str(total_counter))
                        if acc_counter >= RTs_per_acc:
                            break
                    except tweepy.TweepError as e:
                        print(e.reason)
                        if "User is over daily status update limit" in e.reason:
                            over_limit=True
                        sleep(sleep_time)
                        continue
                    except StopIteration:
                        break

def write_bot(bot_lst):
    total_counter=0
    acc_counter=0
    for username in bot_lst:
        consumer_key = Accounts[username][0]
        consumer_secret = Accounts[username][1]
        access_token = Accounts[username][2]
        access_token_secret = Accounts[username][3]
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        auth.secure = True
        api = tweepy.API(auth)
        for tweet in tweepy.Cursor(api.search, q='Crypto Giveaway').items(1000):
            try:
                print("Found tweet by: @" + tweet.user.screen_name)
                if (tweet.retweeted == False) or (tweet.favorited == False):
                    tweet.retweet()
                    tweet.favorite()
                    if hasattr(tweet, 'retweeted_status'):
                        tweet.retweeted_status.author.follow()
                        if ('Bitcoin' in tweet.text or 'BTC' in tweet.text) and 'Address' in tweet.text:
                             message='BTC Address: '+str(Addresses['BTC'])
                             api.update_status("@"+tweet.retweeted_status.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif ('Ethereum' in tweet.text or 'ETH') and 'Address' in tweet.text:
                             message='ETH Address: '+str(Addresses['ETH'])
                             api.update_status("@"+tweet.retweeted_status.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif ('Litecoin' in tweet.text or 'LTC') and 'Address' in tweet.text:
                             message='LTC Address: '+str(Addresses['LTC'])
                             api.update_status("@"+tweet.retweeted_status.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif ('Cardano' in tweet.text or 'ADA') and 'Address' in tweet.text:
                             message='ADA Address: '+str(Addresses['ADA'])
                             api.update_status("@"+tweet.retweeted_status.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif ('FunFair' in tweet.text or 'FUN') and 'Address' in tweet.text:
                             message='FUN Address: '+str(Addresses['FUN'])
                             api.update_status("@"+tweet.retweeted_status.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif 'NEO' in tweet.text and 'Address' in tweet.text:
                             message='NEO Address: '+str(Addresses['NEO'])
                             api.update_status("@"+tweet.retweeted_status.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                    else:
                        tweet.user.follow()
                        if ('Bitcoin' in tweet.text or 'BTC' in tweet.text) and 'Address' in tweet.text:
                             message='BTC Address: '+str(Addresses['BTC'])
                             api.update_status("@"+tweet.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif ('Ethereum' in tweet.text or 'ETH') and 'Address' in tweet.text:
                             message='ETH Address: '+str(Addresses['ETH'])
                             api.update_status("@"+tweet.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif ('Litecoin' in tweet.text or 'LTC') and 'Address' in tweet.text:
                             message='LTC Address: '+str(Addresses['LTC'])
                             api.update_status("@"+tweet.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif ('Cardano' in tweet.text or 'ADA') and 'Address' in tweet.text:
                             message='ADA Address: '+str(Addresses['ADA'])
                             api.update_status("@"+tweet.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif ('FunFair' in tweet.text or 'FUN') and 'Address' in tweet.text:
                             message='FUN Address: '+str(Addresses['FUN'])
                             api.update_status("@"+tweet.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                        elif 'NEO' in tweet.text and 'Address' in tweet.text:
                             message='NEO Address: '+str(Addresses['NEO'])
                             api.update_status("@"+tweet.author.screen_name+' '+message,in_reply_to_status_id=tweet.id)
                    acc_counter += 1
                    total_counter+=1
                    print('Contests Entered on: '+username+': '+str(acc_counter), '\n', 'Total Contests Entered: '+str(total_counter))
                    if acc_counter == 250:
                        acc_counter=0
                        break
            except tweepy.TweepError as e:
                print(e.reason)
                sleep(1)
                continue
            except StopIteration:
                break
            
def following_clear(usernames):
     for username in usernames:
         consumer_key = Accounts[username][0]
         consumer_secret = Accounts[username][1]
         access_token = Accounts[username][2]
         access_token_secret = Accounts[username][3]
         #followed_users_list= open('followed_users.text','r+')
         auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
         auth.set_access_token(access_token, access_token_secret)
         auth.secure = True
         api = tweepy.API(auth)
         api.direct_messages().full_text = True
         counter=0
         for following_id in reversed(api.friends_ids()):
             #user=api.get_user(following_id)
             api.destroy_friendship(following_id)
             counter+=1
             user=api.get_user(following_id)
             print("Unfollowed: @"+str(user.screen_name))
             print("Users Unfollowed: "+str(counter),"on", username)
             if counter >= 500:
                  break

def num_following():
    following_list=[]
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
          for following_id in api.friends_ids():
              counter+=1
          following_list.append(counter)
    i=0
    for key in Accounts:
        print (key+':', str(following_list[i]), 'following')
        i+=1

def giveaways_from_users(lst):
    total_counter=0
    for key in Accounts:
        over_limit=False
        acc_counter=0
        consumer_key = Accounts[key][0]
        consumer_secret = Accounts[key][1]
        access_token = Accounts[key][2]
        access_token_secret = Accounts[key][3]
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        auth.secure = True
        api = tweepy.API(auth)
        for page in lst:
            if over_limit==True:
                break
            else:
                user=api.get_user(screen_name = page)
                user.follow()
            for tweet in tweepy.Cursor(api.user_timeline, user.id).items(20):
                if not tweet.retweeted:
                    if over_limit==True:
                        break
                    else:
                        try:
                            if "Giveaway" in tweet.text or "giveaway" in tweet.text or "GIVEAWAY" in tweet.text or "RT" in tweet.text or "Retweet" in tweet.text or "Enter" in tweet.text or "ENTER" in tweet.text or "Win" in tweet.text or "WIN" in tweet.text or "FREE" in tweet.text or "Free" in tweet.text or "free" in tweet.text or "CONTEST" in tweet.text or "Contest" in tweet.text or "contest" in tweet.text or "RAFFLE" in tweet.text or "Raffle" in tweet.text or "raffle" in tweet.text:
                                tweet.retweet()
                                tweet.favorite()
                                acc_counter+=1
                                total_counter+=1
                                print('Contests Entered on: '+key+': '+str(acc_counter), '\n','On Page: '+page+'\n', 'Total Contests Entered: '+str(total_counter))
                        except tweepy.TweepError as e:
                            print(e.reason)
                            if "User is over daily status update limit" in e.reason:
                                over_limit=True
                            sleep(1)
                            continue
                        except StopIteration:
                            break

#main()
 
#get_email_addresses()
 
#num_following()          
following_clear([
                  ])

#write_bot([])

#giveaways_from_users()      

#dm_reader()

run_individual_bots([])


#sdm_reader()
