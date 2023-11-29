import instaloader # For working with Instagram
import sys # For working with script (exit if required)
import csv # For writing data
import json # For receiving data 
from colorama import Fore, init # For colors in terminal window

init(convert=True) # For colorama library

# Init instaloader
loader = instaloader.Instaloader()

def main():
    # Get all information via json file
    info = json.load(open('info.json'))

    # Try to login
    try:
        print(Fore.CYAN + 'Logging..')
        loader.login(info['username'], info['password'])
    # If username or password incorrect. Catch error, send user-friendly explanation and exit
    except instaloader.exceptions.ConnectionException:
        print(Fore.RED + f"[*]Error message: Login Error! Please, try again.")
        sys.exit()

    # User request  
    query = str(input(Fore.WHITE + "Type your query: "))

    # Function that start parse proccess with user query and max count variable from info.json
    parse_instagram_search(query, info['max_count'])

""" Function that start parse proccess. Query argument represent user search request. 
    Max_count argument represents the number of accounts to find (10 by default). 
    You are also able to change max_count in info.json file.
"""
def parse_instagram_search(query, max_count = 10):   
    # Try to get all profiles with current query
    try:
        # Start search via TopSearchResults class and get_profiles() method
        search_results = instaloader.TopSearchResults(loader.context, query).get_profiles()
        
        # Start counting from 0
        count = 0
        # Create or open data.csv file for further data writing. Encoding = utf-8, It's important!
        with open('data.csv', 'w', encoding='utf-8') as file:
            # Initialise writer from csv library with delimitiers and lineterminators
            writer = csv.writer(file, delimiter=',', lineterminator='\n')

            # Write headers
            writer.writerow(['username', 'full_name', 'biography', 'followers', 'followees', 'posts', 'business_category', 'contact_url'])

            # Start check each result from search_results
            for result in search_results:
                # Check if result is not None
                if isinstance(result, instaloader.Profile):
                    
                    # Get parsed information (username, full_name, bio, followers, followees, number of posts, business category)
                    username = result.username.strip()
                    full_name = result.full_name.strip()
                    bio = result.biography
                    followers = result.followers
                    followees = result.followees
                    posts = result.get_posts().count
                    bs_name = result.business_category_name

                    # Check if external url is exists
                    if result.external_url:
                        contact_url = result.external_url.strip()
                    # Else, just set None
                    else:
                        contact_url = 'None'
                    
                    # Apply information to csv file
                    writer.writerow([username, full_name, bio.replace('\n', ''), followers, followees, posts, bs_name, contact_url])
                    
                    # + 1 account in csv file
                    count += 1
                    # Display progress
                    print(Fore.GREEN + f"Progress: {count}/{max_count}", end='\r')

                    # Check if count is equals or greater than max_count value
                    if count >= max_count:
                        # If true, break loop and send finish message
                        print(Fore.CYAN + "[+] Finished!")
                        break
            # If loop can't go ahead and find new accounts to parse, just say about that
            else:
                print(Fore.RED + "[=] Maximum reached!")
                input()
        
        """ Some issues can happen with parse. So we catch this error and send message.
            Actually I get only from 1 to 2 types of errors
            401 or 400 error code. In other words: client error. 
            Instagram not allow to send requests more than 200 times. So keep in mind about that!
        """

    except instaloader.exceptions.InstaloaderException as e:
        print(Fore.RED + f"[*]Error message: {e}")


if __name__ == "__main__":
    main()