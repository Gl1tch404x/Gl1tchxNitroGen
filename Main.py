import secrets
import string

PURPLE = "\033[95m"
RESET = "\033[0m"

ASCII_ART = r"""
  ________.__  ____  __         .__           ___________           .__          
 /  _____/|  |/_   |/  |_  ____ |  |__ ___  __\__    ___/___   ____ |  |   ______
/   \  ___|  | |   \   __\/ ___\|  |  \\  \/  / |    | /  _ \ /  _ \|  |  /  ___/
\    \_\  \  |_|   ||  | \  \___|   Y  \>    <  |    |(  <_> |  <_> )  |__\___ \ 
 \______  /____/___||__|  \___  >___|  /__/\_ \ |____| \____/ \____/|____/____  >
        \/                    \/     \/      \/                               \/ 
"""

def generate_test_gift_link(length=16):
    alphabet = string.ascii_letters + string.digits + "-_"
    body = ''.join(secrets.choice(alphabet) for _ in range(length))
    return f"https://discord.gift/{body}"

def main():
    print(PURPLE + ASCII_ART + RESET)
    
    try:
        amount = int(input(PURPLE + "How many Nitro codes would you like to generate? " + RESET))
    except ValueError:
        print(PURPLE + "Please enter a valid number." + RESET)
        return

    print(PURPLE + "\nGenerating Nitro gift links...\n" + RESET)

    links = []
    for i in range(amount):
        link = generate_test_gift_link()
        links.append(link)
        print(PURPLE + f"{i + 1}. {link}" + RESET)

    print(PURPLE + f"\nSuccessfully Created {amount} Nitro Links!" + RESET)

    save = input(PURPLE + "\nWould you like to save the links to a file? (y/n): " + RESET).strip().lower()
    if save == 'y':
        with open("Nitro_Links.txt", "w") as f:
            for link in links:
                f.write(link + "\n")
        print(PURPLE + "Links saved to Nitro_Links.txt!" + RESET)

if __name__ == "__main__":
    main()
