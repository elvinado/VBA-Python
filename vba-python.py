import argparse
from pathlib import Path
import time

def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("-i","--inputXlFile", required=True,help="Input Excel File")
    ap.add_argument("-o","--outputPath", required=False,help="Output Path")
    
    args = vars(ap.parse_args())

    input_xl_file = args['inputXlFile']

    if args['outputPath'] is None:
        p = Path(input_xl_file)
        output_path = str(p.parent)
    else:
        output_path = args['outputPath']


    print(f"Input Excel File: {input_xl_file}\nOutput Path: {output_path}")
    for i in range(5):
        print("Doing stuff...")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
