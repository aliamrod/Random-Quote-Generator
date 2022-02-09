#point of execution
def main():
    print("The greatest glory in living lies not in never failing, but in rising every time we fall.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes)

    if __name__ == "__main__":
        main()