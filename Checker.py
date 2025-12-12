import aiohttp
import asyncio

ASCII_ART = r"""
  ________.__  ____  __         .__           ___________           .__          
 /  _____/|  |/_   |/  |_  ____ | 1   ___  ____\__    ___/___   ____ |  |   ______
/   \  ___|  | |   \   __\/ ___\|  |  \\  \/  / |    | /  _ \ /  _ \|  |  /  ___/
\    \_\  \  |_|   ||  | \  \___|   Y  \>    <  |    |(  <_> |  <_> )  |__\___ \ 
 \______  /____/___||__|  \___  >___|  /__/\_ \ |____| \____/ \____/|____/____  >
        \/                    \/     \/      \/                               \/ 
"""

PURPLE = "\033[95m"
GREEN  = "\033[92m"
RED    = "\033[91m"
RESET  = "\033[0m"

async def check_gift_code(session, code):
    url = f"https://discord.com/api/v9/entitlements/gift-codes/""{code}?with_application=false&with_subscription_plan=true"
    try:
        async with session.get(url) as response:
            return response.status == 200
    except:
        return False

async def main_async():
    print(PURPLE + ASCII_ART + RESET)
    file_path = input(PURPLE + "Upload txt file containing Nitro codes (e.g., codes.txt): " + RESET)

    try:
        with open(file_path, "r") as f:
            codes = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(RED + "File not found. Please make sure the file exists." + RESET)
        return

    print(PURPLE + f"\nChecking {len(codes)} Nitro codes...\n" + RESET)

    valid_list = []

    async with aiohttp.ClientSession() as session:
        for i, code in enumerate(codes, start=1):
            is_valid = await check_gift_code(session, code)

            if is_valid:
                print(f"{GREEN}{i}. {code} -> VALID ✅{RESET}")
                valid_list.append(code)
            else:
                print(f"{RED}{i}. {code} -> INVALID ❌{RESET}")

    print(PURPLE + f"\nFinished checking {len(codes)} codes." + RESET)
    print(PURPLE + f"Valid: {len(valid_list)}, Invalid: {len(codes) - len(valid_list)}" + RESET)

    save = input(PURPLE + "\nWould you like to save ONLY valid codes to Valid_Links.txt? (y/n): " + RESET).strip().lower()

    if save == "y":
        with open("Valid_Links.txt", "w") as f:
            for code in valid_list:
                f.write(code + "\n")

        print(GREEN + "Valid codes saved to Valid_Links.txt!" + RESET)
    else:
        print(RED + "Not saving valid codes." + RESET)

if __name__ == "__main__":
    asyncio.run(main_async())
