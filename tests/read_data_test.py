import pandas as pd

def main():
    df = pd.read_csv("D:\\Documents\\Research\\UCR\\PiLabs\\MedicalWebsiteDetection\\datasets\\scraped_preprocessed_fulltext.csv", nrows=10)
    
    print(df.head())

if __name__ == "__main__":
    main()