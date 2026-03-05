# dictionary to store nepali letters with romanised translation
nepali_letters = {
    "ka": "क", "kha": "ख", "ga": "ग", "gha": "घ", "nga": "ङ",
    "cha": "च", "chha": "छ", "ja": "ज", "jha": "झ", "yna": "ञ",
    "Ta": "ट", "Tha": "ठ", "Da": "ड", "Dha": "ढ", "nda": "ण",
    "ta": "त", "tha": "थ", "da": "द", "dha": "ध", "na": "न",
    "pa": "प", "pha": "फ", "ba": "ब", "bha": "भ", "ma": "म",
    "ya": "य", "ra": "र", "la": "ल", "wa": "व", "sha": "श",
    "shha": "ष", "sa": "स", "ha": "ह", "ksha": "क्ष", "tra": "त्र",
    "gya": "ज्ञ"
}

# function to ask user for romanised words and translate to nepali
def romanised2nepali():
    # ask for input and store each romanised words in a list
    romanised_text = input("Enter Romanised Nepali text (as 'ka kha ga'): ")
    roman_letters = romanised_text.split()

    # look for subsequent nepali letters in dictionary and join it  
    nepali_text = "".join(nepali_letters.get(letter, letter) for letter in roman_letters)
    
    print("Nepali Unicode text:", nepali_text)

# main 
def main():
    romanised2nepali()

# only executes if this program is run
if __name__ == "__main__":
    main()
